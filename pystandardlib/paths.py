from pathlib import Path

path = Path("ecommerce/__init__.py")
path.exists() #check if files exist
path.is_file() #check if path represents file
path.is_dir()
print(path.name) #filename
print(path.stem) #filename without extension
print(path.suffix) #returns only extension
print(path.parent) #returns parent
path.with_name() #creates new file with name and extension
print(path.absolute) #absolute value of path