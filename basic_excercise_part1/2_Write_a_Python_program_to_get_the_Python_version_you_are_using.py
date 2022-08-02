# Write a Python program to get the Python version you are using.

# Solution:

import subprocess
import sys

javaVersion = subprocess.check_output(['python','-V'],stderr=subprocess.STDOUT);
print("using subprocess module:\n",javaVersion)
print("\nusing sys module:\n",sys.version)
print("\nusing sys module:\n",sys.version_info)
