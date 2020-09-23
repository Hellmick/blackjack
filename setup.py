import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(name='blackjack', version='0.1', description='Blackjack game', executables=[Executable("blackjack.py", base=base)])