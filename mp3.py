import numpy as np
import warnings
warnings.simplefilter('ignore', np.RankWarning)
#a = np.array([38,37,66,35,99,51,27,19,4,7])
#b = np.array([99,27,12,5,38,37,83,71,76,24])
a = []
b = []
print("Enter how many experimental points you will use")
n = int(input())
i = 1
while i <= n:
    x = [int(input('Value of x: '))]
    a.extend(x)
    y = [int(input('Value of y: '))]
    b.extend(y)
    i = i + 1
print("x values",a)
print("y values",b)




P1 = np.polyfit (a,b,1)
f1 = np.polyval(P1,a)
e1 = b - f1

P2 = np.polyfit (a,b,2)
f2 = np.polyval(P2,a)   
e2 = b - f2

P3 = np.polyfit (a,b,3)
f3 = np.polyval(P3,a)
e3 = b - f3

P4 = np.polyfit (a,b,4) 
f4 = np.polyval(P4,a)
e4 = b - f4

P5 = np.polyfit (a,b,5)
f5 = np.polyval(P5,a)
e5 = b - f5
    
P6 = np.polyfit (a,b,6)
f6 = np.polyval(P6,a)
e6 = b - f6

P7 = np.polyfit (a,b,7)
f7 = np.polyval(P7,a)
e7 = b - f7
    
P8 = np.polyfit (a,b,8)
f8 = np.polyval(P8,a)
e8 = b - f8

P9 = np.polyfit (a,b,9) 
f9 = np.polyval(P9,a)
e9 = b - f9

P10 = np.polyfit (a,b,10)
f10 = np.polyval(P10,a)
e10 = b - f10

d = np.linalg.norm(e1, 2)
e = np.linalg.norm(e2, 2)
f = np.linalg.norm(e3, 2)
g = np.linalg.norm(e4, 2)
h = np.linalg.norm(e5, 2)
i = np.linalg.norm(e6, 2)
j = np.linalg.norm(e7, 2)
k = np.linalg.norm(e8, 2)
l = np.linalg.norm(e9, 2)
m = np.linalg.norm(e10, 2)

n = [d,e,f,g,h,i,j,k,l,m]
o = min(n)

print("The coefficients are:")
if o == n[0]:
    print(P1)
if o == n[1]:
    print(P2)
if o == n[2]:
    print(P3)
if o == n[3]:
    print(P4)
if o == n[4]:
    print(P5)
if o == n[5]:
    print(P6)
if o == n[6]:
    print(P7)
if o == n[7]:
    print(P8)
if o == n[8]:
    print(P9)
if o == n[9]: 
    print(P10)




