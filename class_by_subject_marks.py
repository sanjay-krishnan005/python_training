name = input("enter the name:")
age = int(input("enter the age:"))
sub1 = int(input("subject 1:"))
sub2 = int(input("subject 2:"))
sub3 = int(input("subject 3:"))
total = sub1 + sub2 + sub3
print("total:", total)
avg = total/3
print("average:", avg)
if avg >= 90:
    print("first class")
elif avg < 89:
    print("second class")
elif avg < 60:
    print("third class")
else:
    print("last class")
