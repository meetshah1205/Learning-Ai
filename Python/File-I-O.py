# s = "Hehehehe this is automatically written from a python code\n"  # \n is needed for new line

# # We can even perform arithmetic operations
# x = 2 + 2
# y = str(s) + str(x)

# Writing to a file
z = input("Some text:\n")
n = input("Name of file:\n")
n += ".txt"
y = "\n" + str(z)
with open(n, "w") as f:
    f.write(f"{y}")

# To confirm everything worked
print("The text has been written to a file. Check test.txt")

"""
"w" mode to write things to the file.
"r" mode to read things from the file.

When opening a file in "w" mode, if the file already exists, it will be overwritten.

"r" mode will throw an error if the file doesn't exist.

"w" mode clears the existing contents of the file.
 So we use "a" mode to append everything incrementally to the file.
"""

# Reading from a file
with open("test.txt", "r") as f:
    content = f.read()

print("Content of the file:" + content)
