import os
import tempfile

print("Building a file name yourself:")
filename = "/tmp/guess_my_name.%s.txt" % os.getpid()
temp = open(filename, 'w+b')
try:
    print(f'temp: {temp}')
    print(f'temp.name: {temp.name}')
finally:
    temp.close()
    # Clean up the temporary file yourself
    os.remove(filename)

print('\nTemporaryFile')
temp = tempfile.TemporaryFile()
try:
    print(f'temp: {temp}')
    print(f'temp.name: {temp.name}')
finally:
    # Automatically cleans up the file
    temp.close()
