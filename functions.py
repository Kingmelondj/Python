# a collection of instructions
# a Collection of code

def function1():
    print("ahhhh")
    print("ahhhhh 2")
print("this is outside the function")

function1()
function1()

#a mapping
#input or an argument
def function2(x):
    return 2*x
a = function2(3)
#return value or output = a
print (a)

b = function2(4)
print (b)

c = function2(5)
print(c)


def function3(x, y):
    return x + y
e = function3(1, 2)
print (e)


def function4(x):
    print (x)
    print("still in this function")
    return 3*x
f = function4(4)
print(f)


def function5(some_argument):
    print(some_argument)
    print("weeee")
function5(4)

#KM to Mile converter
#collect input from the user
kilometers = float(input('How many kilometers?: '))

#conversion factor
conv_fac = 0.62137

#calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers, miles))


#BMI CALCULATOR
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's Sister"
height_m1 = 1.8
weight_kg2 = 70

name3 = "YK's Brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2 )
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
    
result1 = bmi_calculator(name1, height_m1, weight_kg1)
print(result1)
print(bmi_calculator)


