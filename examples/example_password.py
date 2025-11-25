import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.value_objects import Password

password = Password.from_string("hfhjsdkhjf34!")
print(password)

password.value = "hkljsjdf"