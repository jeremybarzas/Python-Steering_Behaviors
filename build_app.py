from distutils.core import setup
import py2exe
import sys

target = "app.py"
setup(console = [str(target)])