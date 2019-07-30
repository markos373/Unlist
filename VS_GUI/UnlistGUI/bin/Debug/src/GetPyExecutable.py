import sys
file = open("pypath.txt", "w")
file.write(sys.executable)
print(sys.executable)
file.close()