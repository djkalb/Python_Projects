"""
Your script will need to use Python 3 and the OS module.

Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.

Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.

Your script will need to use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.

Your script will need to print each file ending with a .”txt” file extension and its corresponding mtime to the console.

SETUP INSTRUCTIONS:


You will need to create a new directory on your system, then create 10 different files within this folder.
The files that you create should be a combination of any file types you would like, as long as you include at least two that are
text documents ending with a “.txt” file extension.
This directory will be the one that your script needs to iterate through to complete the assignment.
"""


import os

dir = "C:\\Pyton_Projects"
fileExtension = ".txt"
def fileGetter(dir, ext):
        return [os.path.join(dir, _) for _ in os.listdir(dir) if _.endswith(ext)]
documentsList = fileGetter(dir, fileExtension)

def fileReader(arr):
    for elem in arr:
        file = open(elem, 'r')
        content = file.read()
        print(content)
        file.close()

if __name__ == "__main__":
    print(fileReader(documentsList))





