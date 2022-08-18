"""Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS."""

#Solution:

import platform

print(platform.processor())
print(platform.architecture())
