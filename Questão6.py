#Questão 6
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
    
if media<6.0:
        print('Reprovado')
elif media>=4:
 print ("Exame")
else:
 print ("Reprovado")