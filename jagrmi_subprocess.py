import subprocess

# 1
# code = subprocess.call("gedit")
# if code == 0:
#     print("Success!")
# else:
#     print("Error!")

# 2
# code = subprocess.call(["ping", "www.yahoo.com"])

# 3
# program = "gedit"
# process = subprocess.Popen(program)
# code = process.wait()
#
# print(code)  # 0

# 4
# print(subprocess.Popen(["ls", "-l"]))

# 5
args = ["ping", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)
