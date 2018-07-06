import tempfile

# Create a temporary file and write some date to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world')
# Read data from file
fp.seek(0)
print(fp.read())
# Close the file, it will be removed
fp.close()

# Create a temporary file using a context manager
with tempfile.TemporaryFile() as f_p:
    f_p.write(b'Hello')
    f_p.seek(0)
    print(f_p.read())
# File is now closed and removed

#  Create a temporary directory using context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
#  Directory and contents have been removed
