from pathlib import Path

path = Path("ecommerce")
#path.exists()
#path.mkdir() #create directory
#path.rmdir() #remove directory
#path.rename() #rename directory

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(py_files)