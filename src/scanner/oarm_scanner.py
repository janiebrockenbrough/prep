# Simulates the O-arm gantry rotating around a patient and capturing 2D X-ray projections.

import numpy as np
from scipy.ndimage import rotate

DEFAULT_SIZE = 128
DEFAULT_PROJECTIONS = 180
DEFAULT_NOISE_STD = 0.02

VERTEBRA_DENSITY = 0.8
PEDICLE_DENSITY = 0.6


class Phantom:
    """
    Represents a simplified 2D cross-section of a spine for simulation purposes.

    The phantom is a 2D numpy array where each value represents tissue density
    from 0.0 (air) to 1.0 (dense bone). The project() method simulates an X-ray
    taken at a given gantry angle by rotating the image and summing along one axis.
    """

    def __init__(self, size: int = DEFAULT_SIZE) -> None:
        """Creates a blank phantom array of the given size and populates it with spine shapes."""
        self.size = size
        self.image = np.zeros((size, size))
        self._build()

    def _build(self) -> None:
        """Populates the phantom with a vertebra body (center) and two pedicles (sides)."""
        center = self.size // 2
        half = self.size // 8

        self.image[
            center - half : center + half,
            center - half : center + half
        ] = VERTEBRA_DENSITY

        pedicle_w = self.size // 16
        pedicle_h = self.size // 8

        self.image[
            center - pedicle_h // 2 : center + pedicle_h // 2,
            center - half - pedicle_w * 2 : center - half
        ] = PEDICLE_DENSITY

        self.image[
            center - pedicle_h // 2 : center + pedicle_h // 2,
            center + half : center + half + pedicle_w * 2
        ] = PEDICLE_DENSITY

    def project(self, angle: float) -> np.ndarray:
        """
        Simulates an X-ray projection at the given gantry angle (degrees).

        Rotates the phantom so the beam hits it from a new direction, then sums
        each column top-to-bottom to produce a 1D array of absorbed intensities.
        """
        rotated = rotate(self.image, angle, reshape=False)
        return rotated.sum(axis=0)

    def get_image(self) -> np.ndarray:
        """Returns the raw 2D phantom array for visualization."""
        return self.image


class OArmScanner:
    """
    Simulates the Medtronic O-arm gantry scan process.

    Rotates through evenly spaced angles from 0 to 360 degrees, captures a 1D
    projection at each angle via the phantom, and adds Gaussian noise to each
    projection to model real X-ray detector behavior.
    """

    def __init__(
        self,
        num_projections: int = DEFAULT_PROJECTIONS,
        noise_std: float = DEFAULT_NOISE_STD,
    ) -> None:
        """Stores scan parameters and initializes empty storage for angles and projections."""
        self.num_projections = num_projections
        self.noise_std = noise_std
        self._angles: np.ndarray = np.array([])
        self._projections: list[np.ndarray] = []

    def scan(self, phantom: Phantom) -> list[np.ndarray]:
        """
        Scans the phantom at evenly spaced angles from 0 to 360 degrees.

        At each angle calls phantom.project() to get a clean projection, then
        adds Gaussian noise to simulate real detector behavior. Stores and
        returns all noisy projections as a list.
        """
        self._angles = np.linspace(0, 360, self.num_projections, endpoint=False)
        self._projections = []

        for angle in self._angles:
            clean_projection = phantom.project(angle)
            noise = np.random.normal(0, self.noise_std, size=clean_projection.shape)
            noisy_projection = clean_projection + noise
            self._projections.append(noisy_projection)

        return self._projections

    def get_angles(self) -> np.ndarray:
        """Returns the array of angles (degrees) used in the last scan."""
        return self._angles

    def get_projections(self) -> list[np.ndarray]:
        """Returns the list of noisy projection arrays from the last scan."""
        return self._projections
