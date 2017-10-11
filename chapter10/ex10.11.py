import sys
def bisect(x,y):
 s = []
 index = 0
 for f in x:
  if f == y:
   s.append(index)
  index = index + 1
 print s 
n = int(input("enter the limit : "))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input("enter the string : ")
c = raw_input("enter the element to be searched : ")
bisect(a,c)
if __name__ == "__bisect__":
 bisect(a,c)
