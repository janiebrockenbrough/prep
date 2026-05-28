## Phase 0 — Project Structure
Read AGENTS.md before doing anything else. Once you have read it, tell me:
- What this project is in one sentence
- What phase we are on
- What the three source modules are and what each one is responsible for

Do not write any code until you have confirmed the above.

Task: Phase 0, Session 1.

1. Create the following folder and file structure in the current directory:

   src/
     scanner/
       oarm_scanner.py
     imaging/
       image_reconstructor.py
     navigation/
       spatial_tracker.py
     main.py
   tests/
     test_scanner.py
     test_reconstructor.py
     test_tracker.py
   requirements.txt
   README.md

2. Every .py file must have:
   - A one-sentence comment at the top explaining its purpose
   - An import for numpy as np
   - A placeholder class with the correct name (OArmScanner, ImageReconstructor, SpatialTracker)
   - A docstring on the class explaining what it will do when fully implemented
   - A pass statement inside the class so Python does not error

3. requirements.txt must list: numpy, scipy, matplotlib, pytest

4. README.md must have:
   - A title: "O-arm Surgical Imaging Simulator"
   - One paragraph explaining what the O-arm is and what this simulator does
   - A "Project Structure" section listing every folder and its responsibility
   - A "How to Run" section with the command to run main.py and the command to run tests
   - A phase completion checklist matching the one in AGENTS.md

5. After creating everything, explain:
   - Why we separate code into scanner/, imaging/, and navigation/ instead of one big file
   - What "separation of concerns" means and give one example from this project
   - What a placeholder class is and why we create structure before logic


## Phase 1 - Building O-arm scanner 

Read AGENTS.md before doing anything else. Confirm:
- What phase we are on
- What OArmScanner is responsible for (one sentence)
- What a "projection" is in X-ray imaging (explain it to me before writing code)

Task: Phase 1, Session 1.

Work only in src/scanner/oarm_scanner.py.

1. Create a Phantom class that represents a simple 2D cross-section of a spine:
   - __init__(self, size: int = 128) creates a numpy array of zeros with shape (size, size)
   - _build() populates the array with simple shapes representing bone:
     - A filled rectangle in the center (vertebra body)
     - Two smaller rectangles on the sides (pedicles)
     - Use values between 0.0 and 1.0 where higher = denser tissue
   - project(self, angle: float) -> np.ndarray rotates the phantom by the given angle
     using scipy.ndimage.rotate, then sums along axis=0 to produce a 1D projection array
   - get_image(self) -> np.ndarray returns the raw phantom array for visualization

2. Create an OArmScanner class:
   - __init__(self, num_projections: int = 180, noise_std: float = 0.02)
     stores both as instance variables
   - scan(self, phantom: Phantom) -> list[np.ndarray]:
     - Generates angles evenly spaced from 0 to 360 degrees using numpy linspace
     - At each angle, calls phantom.project(angle) to get a clean projection
     - Adds Gaussian noise using numpy random.normal with std=self.noise_std
     - Stores and returns all noisy projections as a list
   - get_angles(self) -> np.ndarray returns the angle array used in the last scan
   - get_projections(self) -> list[np.ndarray] returns the stored projections

3. Update main.py to:
   - Create a Phantom and an OArmScanner
   - Run a scan
   - Plot 4 sample projections (at angles 0, 45, 90, 135 degrees) side by side
     in a single matplotlib figure with titles showing the angle
   - Plot the original phantom image in a separate figure

4. After writing the code, explain line by line:
   - What scipy.ndimage.rotate does and why we need it
   - Why we sum along axis=0 to get a projection
   - What numpy linspace does and why it is better than range() here
   - Why we add noise after projecting instead of before

Do not run any tests yet — that is Session 2.


