from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "sys"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Ping IP",
    version="0.1",
    description="Verifica ip com ping !",
    options={"build_exe": build_exe_options},
    executables=[Executable("teste.py", base=base)]
)
