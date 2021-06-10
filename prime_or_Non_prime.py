# Find Prime and Non_prime number

lst=[]
prm=[]
no_prm=[]
l=int(input("Lenght: "))
for i in range(l):
  a=int(input())
  lst.append(a)
for num in lst:
  if num > 1:
    for i in range(2,num):  
        if (num % i) == 0:  
            no_prm.append(num)
            break
    else:
        prm.append(num)
  else:
    no_prm.append(num)
print("Prime:",prm)
print("Non prime:",no_prm)