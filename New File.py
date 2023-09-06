#1.1 Implement a recursive function to calculate the factorial of a given nude.
"""
1!=1A-1
2!=2A-1!
3!=3Ã-2!
.
.
10!=10Ã-9!
"""

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
   return n*fact_rec(n-1) 
number = int(input("Enter a value:")) 
res = fact_rec (number)
print("The factorial of {} is {}.".format(number,res))
                                         

