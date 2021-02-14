
import array 
import numpy as np

bus=array.array("i",[23,14,425,26,24,2,6326,37,4])
print(bus)


# bus.append(int(input ("enter the value to add to array")))
# print(bus)
# bus.pop()
# bus.remove(int(input("enter value to be removed")))
# print(bus)


a =array.array("i",[231,41,4,51,6,37,7])
print(a)

a=np.array([[23,434,56,63,325,45,423],[1,23,21,4,2,1]])
print(type(a))
print(a)

a= np.ones(3,int)
print(a)
b=np.array([1,2,4,56,6])
print(a*3)
c=np.concatenate([a,b])
print(c)
print(np.log(c))
print(np.sin(c))
print(sum(c))
print(max(c))
print(min(c))

d=c.view()
e=c.copy()

c[3]=200
print(c)
print(d)
print(e)
print(id(c))
print(id(d))
print(id(e))



x=np.array([[2,4,5,67,32,8],[32,4,42,5,3,643]])
print(x.size)
print(x.ndim)
print(x.shape)
print(x[1][3])

print(x)
y=x.flatten()
y=y.reshape(3,4)
print(y)
x=x.flatten()
print(x)

z = x.reshape(6,2)
print(z)

m=np.matrix('1 2 34 4 ; 3 5 3 6 ;12 3 4 42')
print("same mat : ",m)

m=np.matrix('1 2 3.4 4 ; 3 5 3 6 ;12 3 4 42')
print("same mat : ",m)
m=np.matrix('1,2,34,4 ; 3,5,3,6 ;12,3,4,42;2,4,5,63')
print("same mat : ",m)
print( "diagonal",m.diagonal())
print(m.max())
