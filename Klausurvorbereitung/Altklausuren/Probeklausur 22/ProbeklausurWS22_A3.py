import numpy as np

A1 = np.array([[1,1,-9,3],[-5,3,8,-2],[-10,-5,1,-8],[0,-4,4,5]])
b1 = np.array([11,97,-19,-18])

A2 = np.array([[-3,5,10],[-2,7,14],[-3,1,2]])
b2 = np.array([34,0,95])

#print(A1,b1)
#print(A2,b2)

def LGScheck(A):
    lsg = 0
    if np.isfinite(np.linalg.cond(A)):
        #B = np.linalg.inv(A)
        det = np.linalg.det(A)
        lsg=1
    else:
        lse=0
    return lsg, det

def LGSsolve(A,b):
    try:
        #I=np.dot(A, np.linalg.inv(A))
        Lösung = np.linalg.solve(A,b)
        lösbar=True
    except:
        Lösung=np.linalg.lstsq(A,b,rcond=1)
        Lösbar=False
    return lösbar, Lösung


lösbar1, det1 = LGScheck(A1)
lösbar2, det2 = LGScheck(A2)

print(f'Das Gleichungssystem hat eine (1) bzw. keine (0) Lösung: {lösbar1}. \nmit der Determinante von A: {det1:00.4}')
print(f'Das Gleichungssystem hat eine (1) bzw. keine (0) Lösung: {lösbar2}. \nmit der Determinante von A: {det2:00.4}')

Lösbar1, Lösung1 = LGSsolve(A1,b1)
Lösbar2, Lösung2 = LGSsolve(A2,b2)

