# AGENTS.md

Read this file completely at the start of every session before doing anything else.
Do not write a single line of code until you have read this entire file.

---

## Who I am

I am a software engineering intern starting at Medtronic this summer. I will be working
on the next-generation O-arm surgical imaging system simulator. This project is my prep
work before the internship begins.

I am learning as I build. I am not an expert yet. Every time you write code, you must
explain what it does line by line in plain English. Do not assume I know what something
means — if you use a new concept, library, or pattern, explain it before moving on.

---

## How you must behave in every session

- Explain everything step by step as if I am new to software engineering
- Never write code without explaining what each part does and why
- Never move to the next phase until I confirm the current one is working and I understand it
- If I ask "why", give me a real answer — not just "it's best practice"
- If something could be done multiple ways, tell me the options and why we are choosing one
- Always tell me what terminal command or VS Code action to take after generating code
- Keep the code clean, readable, and commented — this is prep for a professional environment

---

## Git workflow

At the start of each session:
1. Check what branch we are on
2. Create a new branch named `session-N` (e.g. `session-1`, `session-2`)
3. Do all work for that session on that branch
4. Explain all of the steps thoroughly before asking me to commit 
5. Commit regularly with meaningful messages (see commit format below)
6. Do not merge into main — leave that to me

Commit message format: `type(scope): short description`
Examples:
- `feat(scanner): add OArmScanner class with projection simulation`
- `test(scanner): add unit tests for noise calibration`
- `docs(readme): update project structure section`
- `fix(imaging): correct backprojection array shape`

---

## What this project is

A Python-based simulator for the Medtronic O-arm surgical imaging system. The O-arm is
a mobile intraoperative 2D/3D X-ray imaging system used in spine, cranial, and orthopedic
surgery. It rotates its gantry around the patient to collect 2D X-ray projections at
multiple angles, then reconstructs them into a 3D image for real-time surgical guidance.

This simulator models that behavior in software so engineers can develop and test
navigation logic without needing physical hardware. The real Medtronic simulator is
Java-based with a Docker container. This prep version is Python-based.

---

## Project structure

```
oarm-simulator/
├── src/
│   ├── scanner/
│   │   └── oarm_scanner.py        # Simulates O-arm gantry rotation and X-ray projection capture
│   ├── imaging/
│   │   └── image_reconstructor.py # Reconstructs 3D image from 2D projections (backprojection)
│   ├── navigation/
│   │   └── spatial_tracker.py     # Tracks surgical tool position relative to scan image
│   └── main.py                    # Entry point — runs the full simulation pipeline
├── tests/
│   ├── test_scanner.py
│   ├── test_reconstructor.py
│   └── test_tracker.py
├── requirements.txt
├── README.md
├── AGENTS.md                      # This file — read before every session
└── PROMPTS.md                     # Phase-by-phase build roadmap
```

Every module has exactly one responsibility. Do not mix concerns across files.
Never put imaging logic in the scanner module, never put scanner logic in navigation, etc.

---

## Architecture rules

### The simulation pipeline
Data flows in one direction only:

```
OArmScanner → projections → ImageReconstructor → image → SpatialTracker → tool position
```

Each module takes input, does its job, and passes output to the next. They do not reach
into each other's internals.

### Class responsibilities

**OArmScanner** (`src/scanner/oarm_scanner.py`)
- Simulates the gantry rotating and capturing 2D X-ray projections
- Adds Gaussian noise to simulate real detector behavior
- Manages gantry state (IDLE, POSITIONING, SCANNING, PROCESSING, ERROR)
- Does not know anything about reconstruction or navigation

**ImageReconstructor** (`src/imaging/image_reconstructor.py`)
- Takes projections from OArmScanner and reconstructs a 2D/3D image
- Implements backprojection and filtered backprojection
- Attaches metadata (scan ID, timestamp, parameters) to every output
- Does not know anything about the scanner or navigation

**SpatialTracker** (`src/navigation/spatial_tracker.py`)
- Registers the reconstructed image to physical space using fiducial markers
- Tracks surgical tool position relative to the image
- Computes distance to target and detects safety zone violations
- Does not know anything about scanning or reconstruction

---

## Code style rules

- Every file must have a one-sentence comment at the top explaining its purpose
- Every class and method must have a docstring explaining what it does
- Every function parameter must have a type hint (e.g. `def scan(self, phantom: np.ndarray) -> list`)
- Use named constants for all magic numbers at the top of each file
  (e.g. `DEFAULT_PROJECTIONS = 180` not just `180` buried in code)
- Never use single-letter variable names except loop counters (`i`, `j`)
- Keep functions short — if a function is longer than 20 lines, it probably does too much

---

## Testing rules

- Use pytest for all tests
- Every class must have a corresponding test file in tests/
- Every method must have at least one test
- Tests must be run and passing before a phase is considered complete
- To run tests: `pytest tests/` from the project root

---

## Key concepts to understand (ask me to explain any of these)

| Term | What it means in this project |
|---|---|
| Projection | A 1D shadow/slice of the 3D object captured at one gantry angle |
| Backprojection | Smearing projections back at their angles to reconstruct the original image |
| Gaussian noise | Random error added to sensor readings — models real X-ray detector behavior |
| State machine | Enforces valid gantry states and prevents illegal transitions |
| Fiducial marker | A known landmark used to align image coordinates with physical space |
| Image registration | Mapping between the scan's coordinate system and real-world coordinates |
| DICOM | Medical imaging standard — every real scan has metadata attached |
| IEC 62304 | Medical device software standard — requires tests, traceability, and reviews |

---

## Phase completion tracker

- [ ] Phase 0 — Project structure and placeholder files
- [ ] Phase 1 — OArmScanner: gantry scan and projection simulation
- [ ] Phase 2 — ImageReconstructor: backprojection and filtered backprojection
- [ ] Phase 3 — Gantry state machine
- [ ] Phase 4 — DICOM-style scan metadata
- [ ] Phase 5 — SpatialTracker: image registration and tool navigation
- [ ] Phase 6 — Unit tests for all modules
- [ ] Phase 7 — Java familiarization (rewrite OArmScanner in Java)
- [ ] Phase 8 — Docker containerization

Update this list by changing `[ ]` to `[x]` when a phase is complete and all tests pass.

---

## Current status

Phase 0 complete — project structure created.
Starting Phase 1: OArmScanner class.