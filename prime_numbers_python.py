start=int(input("enter the start value: \n"))
end=int(input("enter the ending values: \n"))
print("the prime number is",start,"and",end,"between:")
for num in range(start,end+1):
   if num>1:
      for i in range(2,num):
         if(num%i)==0:
            break
      else:
         print(num)
