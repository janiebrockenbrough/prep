# Entry point — runs the full O-arm simulation pipeline end to end.

import numpy as np
import matplotlib.pyplot as plt

from scanner.oarm_scanner import OArmScanner, Phantom

SAMPLE_ANGLES = [0, 45, 90, 135]


def main() -> None:
    """Creates a phantom, runs a scan, and plots the phantom and four sample projections."""
    phantom = Phantom()
    scanner = OArmScanner()

    projections = scanner.scan(phantom)
    angles = scanner.get_angles()

    plt.figure(figsize=(5, 5))
    plt.imshow(phantom.get_image(), cmap="gray")
    plt.title("Phantom: Spine Cross-Section")
    plt.colorbar(label="Tissue Density")
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, target_angle in zip(axes, SAMPLE_ANGLES):
        index = int(np.argmin(np.abs(angles - target_angle)))
        ax.plot(projections[index])
        ax.set_title(f"Projection at {target_angle}°")
        ax.set_xlabel("Detector Position")
        ax.set_ylabel("Absorbed Intensity")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
