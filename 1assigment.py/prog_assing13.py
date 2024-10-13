"""
13)write a python program that will return true if the two given integer values are equal 
or their sum or diffrent is 5.

5,5=true
2+3=true
10-5=true

abs means jo bhi negative integer aa raha use positive karne ka kam karta hai 
"""
def test(x,y):
    if x==y or x+y==5 or x-y==5:
        print("the return will be true:")

    else:
        print("the return value is not true:")

print(test(7,2))
print(test(3,2))
print(test(27,53))
    