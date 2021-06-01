# Python program to 
# read files line by line

#user input
file_name = input("enter file name:")

#opening file
f = open(file_name, "r")
count = 0
l = []

while True:
    count += 1
    # Get next line from file
    line = f.readline()

    #end of lines/file
    if not line:
        break
    l.append("Line{}: {}".format(count, line.strip()))
    print(l[-1])
f.close()