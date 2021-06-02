from array import *

# user input
no_of_elements = int(input("enter number of elements : "))
list_items = []
for i in range(no_of_elements):
    element = int(input("element-{} : ".format(i+1)))
    list_items.append(element)


# function for conversion of array
# into bytes format
def array_to_bytes(items):
    array_values = array('i', items)
    bytes_converted = array_values.tobytes()
    return bytes_converted

output = array_to_bytes(list_items)
print("bytes representation : {}".format(output))
