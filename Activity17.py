#Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?

science=int(input("enter your marks."))
english=int(input("enter your marks."))
maths=int(input("enter your marks."))
computer=int(input("enter your marks."))
sst=int(input("enter your marks."))

sag= (science+english+maths+computer+sst)/5

print("average ",sag)

if sag>=91 and sag<=100:
    print("you have A1 grade")

elif sag>=81 and sag<=90:
    print("you have A2 grade")
elif sag>=71 and sag<=80:
    print("you have b1 grade")
else:
    print("you got E2")