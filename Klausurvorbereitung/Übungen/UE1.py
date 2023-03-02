#import
import numpy as np

#Aufgabe 2.2
pi = 3.141592653589793238462643383279502884197169399375105
print(f'pi={pi:7.6}')

#Aufgabe 2.3
x=[0,1,2,3,4,5,6,7,8,9,10]
print('|  x1 |  x2 |  x3 |  x4 |  x5 |  x6 |  x7 |  x8 |  x9 | x10 |')
print('-------------------------------------------------------------')
print('| ',x[1], ' | ',x[2], ' | ',x[3], ' | ',x[4], ' | ',x[5], ' | ',x[6], ' | ',x[7], ' | ',x[8], ' | ',x[9], ' |',x[10], ' |')

#Aufgabe 2.4

text = '"Python" ist eine tolle Programmiersprache'
print(text)
text.replace('Python','C++')
text_neu = text[0:13] + 'auch' + text[12:]
print(text_neu)

#Aufgabe 2.5
print(f'{float(x[1]):04.1f} | {float(x[3]):04.1f} | {float(x[5]):04.1f} | {float(x[7]):04.1f} | {float(x[9]):04.1f}')

#Aufgabe 2.6
print(np.real(np.exp(1j*np.pi))+1)

#Aufgabe 2.6
def Umfang(d):
    return d*np.pi
print(Umfang(2))

#----------------------------------------------------------------

#Aufgabe 3.1
Stichwort = 'ist'
MyText = 'Python ist eine universelle, üblicherweise interpretierte höhere Programmiersprache. Sie hat den Anspruch, einen gut lesbaren, knappen Programmierstil zu för- dern. So werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch Einrückungen strukturiert. Wegen seiner klaren und übersichtlichen Syntax gilt Python als einfach zu erlernen. Python unterstützt mehrere Programmierparadigmen, z.B. die objektorientierte, die aspektorientierte und die funktionale Programmierung. Ferner bietet es eine dynamische Typisierung. Wie viele dynamische Sprachen wird Py- thon oft als Skriptsprache genutzt. Die Sprache weist ein offenes, gemeinschaftsbasier- tes Entwicklungsmodell auf, das durch die gemeinnützige Python Software Foundation gestützt wird, die de facto die Definition der Sprache in der Referenzumsetzung CPython pflegt.'

x = MyText.find(Stichwort)
count = MyText.count(Stichwort)

print(x)
if x== -1:
    print('Das Stichwort wurde nicht gefunden!')

else:
    print('Das Stichwort \'', Stichwort, '\' wurde ', count, 'mal gefunden. Die erste Fundstelle war an Position ', x)


#Aufgabe 3.2
x = input('In welcher Sprache möchten Sie begrüßt werden?')

if x == 'deutsch':
    print('Hallo')
elif x == 'englisch':
    print('hello')
elif x == 'spanisch':
    print('Hola')
elif x == 'chnesishc':
    print('Ni hao')
elif x == 'arabisch':
    print('Marhabaan')  
elif x == 'hindi':
    print('Abhinandan')     
else:
    print('Sprache nicht enhalten :(')
