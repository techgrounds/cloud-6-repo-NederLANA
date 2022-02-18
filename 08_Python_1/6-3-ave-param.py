"""
Create a new script with the following script:
- def avg():
    #write your code here
- x = 128
- y = 255
- z = avg(x,y)
print ("The average of",x,"and", y, "is", z)
- Write the custom function avg() so that it returns the average of the given parameters.
"""
def avg(x,y):
   return ((x+y)/2) #when z calls on the ave(x,y), it'll call on this return value.
x = 128
y = 255
z = avg(x,y) 
print ("The average of",x,"and", y, "is", z)