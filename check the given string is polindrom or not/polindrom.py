def polindrom(s):

    return s==s[::-1]


s=input("enter the string \n")
ans=polindrom(s)

if ans:
    print("yes")
else:
    print("no")