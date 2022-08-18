# Write a Python program to get OS name, platform and release information.
import platform

print('OS Name :',platform.system())
print('platform :',platform.platform())
print('release :',platform.release())

print('release :',platform.uname())
# print('release :',platform.version())
# print('release :',platform.architecture())
# print('release :',platform.machine())
# print('release :',platform.node())
