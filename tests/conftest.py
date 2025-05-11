import sys
from pathlib import Path

# Добавляем src в PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir / "src"))
