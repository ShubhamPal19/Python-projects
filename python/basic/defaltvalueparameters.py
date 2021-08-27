


from typing import final


def knock(name, numberoftimes=2):
    for i in range(0,numberoftimes):
        print("knock Knock {}" .format(name))


knock("rohan")
knock("Shubham",5)




# finally block in python


def div(a,b):
    try:
        return a/b
    except:
        print("error , division by zero")
    finally:
        print("Wrapping up, this block will be executed even if the return statement is encountered in above code snippet.") 


print("\n")
print("\n")
print(div(23,3))
print("\n")

#
print(div(1,0))
print("\n")

