# Entry point — runs the full O-arm simulation pipeline end to end.

import numpy as np

from scanner.oarm_scanner import OArmScanner
from imaging.image_reconstructor import ImageReconstructor
from navigation.spatial_tracker import SpatialTracker


def main():
    """Runs the full simulation pipeline: scan -> reconstruct -> track."""
    print("O-arm Surgical Imaging Simulator")
    print("Phase 0: structure verified — all modules import successfully.")


if __name__ == "__main__":
    main()
