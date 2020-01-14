"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""


import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("Number of arguments", len(sys.argv))

# Print out the OS platform you're using:
print("Windows Version", sys.getwindowsversion())

# Print out the version of Python you're using:
print("Python Version", sys.implementation)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current process ID", os.getpid())

# Print the current working directory (cwd):
print("Current Working Dirctory", os.getcwd())

# Print out your machine's login name
print("Machine Login Name", os.getlogin())
