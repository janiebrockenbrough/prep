# Takes 2D X-ray projections from the scanner and reconstructs them into a 2D image.

import numpy as np
from scipy.ndimage import rotate

DEFAULT_IMAGE_SIZE = 128


class ImageReconstructor:
    """
    Reconstructs a 2D image from a set of X-ray projections using backprojection.

    Backprojection smears each 1D projection back across a 2D canvas at the angle
    it was captured, accumulating contributions from all angles to recover the
    approximate original image. The result is blurry but structurally correct.
    Filtered backprojection (Session 2) will sharpen it by pre-filtering projections.
    """

    def __init__(self, image_size: int = DEFAULT_IMAGE_SIZE) -> None:
        """Stores the output image size used when allocating the reconstruction canvas."""
        self.image_size = image_size

    def backproject(self, projections: list, angles: np.ndarray) -> np.ndarray:
        """
        Reconstructs a 2D image from a list of 1D projections and their capture angles.

        For each projection, tiles it into a 2D array of vertical stripes, rotates
        those stripes back by the negative capture angle, and accumulates onto the
        output canvas. Divides by the number of projections to normalize the result.
        """
        output = np.zeros((self.image_size, self.image_size))

        for projection, angle in zip(projections, angles):
            tiled = np.tile(projection, (self.image_size, 1))
            rotated_back = rotate(tiled, -angle, reshape=False)
            output += rotated_back

        output /= len(projections)
        return output
