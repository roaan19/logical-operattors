m=10
l=19
r=7

if m>l or r>l:
    print("i am using or operator")
elif l>m and m>r :
    print("i am using and operator")


#not operator
a=10
v=7
c=10

print(a!=v)
print(a!=c)

a="python"
b="coding"

if a!=b:
    print("a and b are different")

a=19
b=18

if (a==1) != (b==18):
    print("hello")

a=int(input("enter the number"))
if a%2!=0:
    print("it is not an even number")

#bmi calculator
height=float(input("enter the height in cm "))
weight=float(input("enter the weight in kg "))

bmi=weight/(height/100)**2

if bmi<=18.4:
    print("u are underweight")
elif bmi<=24.9:
    print("u are healthy ")
elif bmi<=29.9:
    print("u are overweight ")
else:
    print("u are obese")