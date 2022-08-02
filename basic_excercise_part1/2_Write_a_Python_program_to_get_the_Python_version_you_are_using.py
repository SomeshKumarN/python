# Write a Python program to get the Python version you are using.

# Solution
import subprocess
javaVersion = subprocess.check_output(['python','-V'],stderr=subprocess.STDOUT);
print(javaVersion)
 