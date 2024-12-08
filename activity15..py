#Write a program to illustrate the use of 'is' identity operator.

py1=1
py2=2
py3=3
py4=3
print(py3 is not py4)
print(py1 is not py2)
print(py3 is py4)

if (type(py4)is int):
    print("It is working.")
if (type(py1)is not float):
    print("It is working.")
