#01 Average of three numbers

n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
avg=(n1+n2+n3)/3
print("Average of three numbers",avg)

#02 Income Tax

Gross_income=int(input("Enter Gross Income"))
dependent=int(input("Number of dependents"))
Tax_income=Gross_income-10000-(dependent*3000)
Tax=0.2*Tax_income
print("The person has to pay",Tax,"to income tax officer")

#03 List

n1=int(input("No. of Students"))
afk=["SID","Name","Gender","Course Name","CGPA"]
for k in range(n1):
    brb=[]
    SID=int(input("Enter SID:"))
    Name=input("Enter Name")
    Gender=input("Enter Gender") #Gender should be F/M and U for unknown
    Course_Name=input("Enter the course:")
    CGPA=float(input("Enter CGPA:"))
    brb.append(SID)
    brb.append(Name)
    brb.append(Gender)
    brb.append(Course_Name)
    brb.append(CGPA)
    print(afk)
    print(brb)

#04 Marks of Students

s1=float(input("Enter marks of First Student="))
s2=float(input("Enter marks of Second Student="))
s3=float(input("Enter marks of Third Student="))
s4=float(input("Enter marks of Fourth Student="))
s5=float(input("Enter marks of Fifth Student="))
slst=[s1,s2,s3,s4,s5]
slst.sort()
print(slst)

#05

    #(a)
color=["Red","Green","White","Black","Pink","Yellow"]
color.pop(3)
print(color)

     #(b)
color[3]="Purple"
print(color)