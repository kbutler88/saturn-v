import os

# Just playing with the os module to see what it can do
#print(os.name)
#print(os.uname())

# os.uname() returns a tuple of data; tuples can be displayed via dot-notation
os_data = os.uname()
# Access tuple directly without loading into variable
#print('TESTING:', os.uname().sysname)
print('Sysname:', os_data.sysname)
print('Nodename:', os_data.nodename)
print('Release:', os_data.release)
print('Version:', os_data.version)
print('Machine:', os_data.machine)
# Like pwd
print('Current workind dir:', os.getcwd())
# Check if file exists
print('os-module.py exists?', os.path.exists('os-module.py'))
print('os_modfalse.py exists?', os.path.exists('os_modfalse.py'))
print(os.path.dirname(os.path.abspath('os-module.py')))
print('os-module.py access time', os.path.getatime('os-module.py'))
print('os-module.py is file?', os.path.isfile('os-module.py'))
print('os-module.py is dir?', os.path.isdir('os-module.py'))

print(os.stat('os-module.py'))
os.chown('os-module.py', 1000, 1000)
# Using "0o" before the octal number signifies that the numbers are meant to be octal; after this is the octal mode value
os.chmod('os-module.py', 0o750)
print(os.stat('os-module.py'))
