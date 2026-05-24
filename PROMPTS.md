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
