from pathlib import Path
import sys

# Enables daysinmonth module imports when running tests
context = Path(__file__).resolve().parents[1] / "daysinmonth"
sys.path.insert(0, str(context))
