
import numpy as np
import math 
x1,y1 = (input('Input first (x,y) coordinates separated by a comma: ').split(","))
x2,y2 = (input('Input second (x,y) coordinates separated by a comma: ').split(","))
x3,y3 = (input('Input third (x,y) coordinates separated by a comma: ').split(","))
x1 = int(x1) 
y1 = int(y1) 
x2 = int(x2) 
y2 = int(y2) 
x3 = int(x3) 
y3 = int(y3)

x1a = (x1*x1) + (y1*y1)
x2a = (x2*x2) + (y2*y2)
x3a = (x3*x3) + (y3*y3)

C = np.array([(x1, y1, 1), (x2, y2, 1), (x3, y3, 1)])
D = -np.array([(x1a, y1, 1), (x2a,y2, 1), (x3a, y3, 1)])
E = np.array([(x1a, x1, 1), (x2a,x2, 1), (x3a, x3, 1)])
F = -np.array([(x1a, x1, y1), (x2a,x2, y2), (x3a, x3, y3)])
   
h = -((round(np.linalg.det(D))) / (2*round(np.linalg.det(C))))
k = -((round(np.linalg.det(E))) / (2*round(np.linalg.det(C))))
D = (round(np.linalg.det(D)))/ (round(np.linalg.det(C)))
E = (round(np.linalg.det(E))) / (round(np.linalg.det(C)))
F = (round(np.linalg.det(F))) / (round(np.linalg.det(C)))    
r = (math.sqrt((h - x1)**2 + (k - y1)**2))   
roundr = round(r,3)

print('Center:',(h,k))
print('Radius:',roundr)
print('Vector:', [D,E,F])