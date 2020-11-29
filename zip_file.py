from pathlib import Path
from zipfile import ZipFile

# Crear un archivo zip con los archivos localizados en el home directory de esta apliccipn python
with ZipFile("files.zip", "w") as zip:
    for path in Path(r"C:\Users\eduardo\PycharmProjects\practica").glob("*.py"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())

zip.extractall("extract")