# O-arm Surgical Imaging Simulator

The Medtronic O-arm is a mobile intraoperative imaging system used in spine, cranial, and orthopedic surgery. It rotates a gantry (a ring-shaped X-ray arm) around the patient, capturing 2D X-ray images from multiple angles, then combines those images into a 3D volume that surgeons use for real-time guidance. This simulator models that process entirely in Python — generating synthetic projections, reconstructing them into an image, and tracking a virtual surgical tool's position relative to the scan — so that navigation logic can be developed and tested without physical hardware.

## Project Structure

| Folder | Responsibility |
|---|---|
| `src/scanner/` | Simulates the O-arm gantry rotating and capturing 2D X-ray projections at each angle |
| `src/imaging/` | Reconstructs a 2D/3D image from the set of projections using backprojection algorithms |
| `src/navigation/` | Registers the reconstructed image to physical space and tracks surgical tool position |
| `src/` | Contains `main.py`, the entry point that runs the full simulation pipeline |
| `tests/` | Contains pytest unit tests for each module |

## How to Run

Run the full simulation pipeline:
```
python src/main.py
```

Run the test suite:
```
pytest tests/
```

## Phase Completion Checklist

- [ ] Phase 0 — Project structure and placeholder files
- [ ] Phase 1 — OArmScanner: gantry scan and projection simulation
- [ ] Phase 2 — ImageReconstructor: backprojection and filtered backprojection
- [ ] Phase 3 — Gantry state machine
- [ ] Phase 4 — DICOM-style scan metadata
- [ ] Phase 5 — SpatialTracker: image registration and tool navigation
- [ ] Phase 6 — Unit tests for all modules
- [ ] Phase 7 — Java familiarization (rewrite OArmScanner in Java)
- [ ] Phase 8 — Docker containerization
