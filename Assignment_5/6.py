a = int(input("Enter 3 digit Number"))
while a>10:
    rem=a%10
    a=a/10
    a=int(a)
print(rem)