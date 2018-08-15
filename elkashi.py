from math import sqrt, cos

# C²= A²+B²-2ABcos(c)

A= float(input("A? "))
B= float(input("B? "))
c= float(input("c? "))

C= sqrt(A*A+B*B-2*A*B*cos(c))

print(C)