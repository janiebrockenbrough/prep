# Entry point — runs the full O-arm simulation pipeline end to end.

import numpy as np
import matplotlib.pyplot as plt

from scanner.oarm_scanner import OArmScanner, Phantom
from imaging.image_reconstructor import ImageReconstructor


def main() -> None:
    """Runs a full scan, reconstructs the image, and plots the phantom and reconstruction side by side."""
    phantom = Phantom()
    scanner = OArmScanner()
    reconstructor = ImageReconstructor()

    projections = scanner.scan(phantom)
    angles = scanner.get_angles()

    reconstructed = reconstructor.backproject(projections, angles)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(phantom.get_image(), cmap="gray")
    axes[0].set_title("Original Phantom (Ground Truth)")
    axes[0].axis("off")

    axes[1].imshow(reconstructed, cmap="gray")
    axes[1].set_title("Reconstructed Image (Backprojection)")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
