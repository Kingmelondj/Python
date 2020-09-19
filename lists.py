#Lists

a = [3, 10, -1]

a.append(1) #adding 1 to "list a"

a.append("hello")
# you can add strings to the list this way

a.append([1, 2])

a.pop()
#pop is predefined to take away from the list
a.pop()

a[0] = 100
 #this means to find the indeces of the array. 
print(a[0])
print(a)


b = ["banana","apple", "microsoft"]

temp = b[0] 
b[0] = b[2] 
b[2] = temp


