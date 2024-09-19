#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

lista_um_a_dez = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Leonardo','Pedro','João','Jean']
lista_anos = [2000,2024]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for numero in lista_um_a_dez:
    print (f'.{numero}')
    
#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma_impares = 0
for i in range(1, 11, 2): #primeiro argumento é o inicio, segundo argumento é o final e o terceiro argumento é o tamanho do intervalo que deve ser passado
    soma_impares += i
print(soma_impares)

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10, 0, -1):
    print(i)
    
#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")