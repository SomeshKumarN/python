# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# from platform import architecture, platform 
from platform import architecture, platform
import struct
print(struct.calcsize('P')*8)

print(architecture())