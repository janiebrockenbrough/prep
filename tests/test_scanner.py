# Tests for Phantom and OArmScanner classes in oarm_scanner.py.

import numpy as np
import pytest
from src.scanner.oarm_scanner import OArmScanner, Phantom


def test_projection_shape():
    """Assert that project() returns a 1D array whose length equals the phantom size."""
    phantom = Phantom(size=64)
    projection = phantom.project(0)
    assert projection.ndim == 1
    assert len(projection) == 64


def test_scan_returns_correct_count():
    """Assert that scan() produces exactly num_projections projections."""
    scanner = OArmScanner(num_projections=36)
    phantom = Phantom()
    scanner.scan(phantom)
    assert len(scanner.get_projections()) == 36


def test_noise_is_added():
    """Assert that stored projections differ from the clean projection (noise was applied)."""
    phantom = Phantom()
    clean_projection = phantom.project(0)
    scanner = OArmScanner()
    scanner.scan(phantom)
    first_stored = scanner.get_projections()[0]
    assert not np.array_equal(clean_projection, first_stored)


def test_noise_is_unbiased():
    """Assert that noise averages to near zero across 500 scans (Gaussian noise is centered at 0)."""
    phantom = Phantom(size=64)
    clean_projection = phantom.project(0)
    scanner = OArmScanner(num_projections=1, noise_std=0.02)

    differences = []
    for _ in range(500):
        scanner.scan(phantom)
        noisy_projection = scanner.get_projections()[0]
        differences.append(noisy_projection - clean_projection)

    mean_error = float(np.mean(differences))
    assert abs(mean_error) < 0.01


def test_angles_cover_full_rotation():
    """Assert that scan angles span from 0 to near 360 degrees with exactly 180 values."""
    scanner = OArmScanner(num_projections=180)
    phantom = Phantom()
    scanner.scan(phantom)
    angles = scanner.get_angles()

    assert len(angles) == 180
    assert angles[0] == pytest.approx(0.0)
    assert angles[-1] > 350
