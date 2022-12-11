n1=int(input("Enter input1:"))
n2=int(input("Enter input2:"))
n3=int(input("Enter input3:"))
n4=int(input("Enter input4:"))
n5=int(input("Enter input5:"))
if (n1<0) or (n2<0) or (n3<0) or (n4<0) or (n5<0):
    print("error,there are negative number")
else:
    n = n1+n2+n3+n4+n5
    print("total:",n)
