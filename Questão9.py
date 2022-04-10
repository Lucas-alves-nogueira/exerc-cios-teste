#Questão 9
numero = int(input("Tabuada de:"))
x= 1
print('*' * 18)  
print('Tabuada de {}'.format(numero))  
print('*' * 18)  
while(x <= 10):  
  print('{0} X {1} = {2}'.format(numero, x, (numero * x)))  
  x = x + 1 