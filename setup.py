import sys
from cx_Freeze import setup , Executable

setup(
    name ="ImagesDownloader",
    version = "0.1",
    description = "Python Script for downloading images on a website.",
    executables = [Executable("main.py")]
)
