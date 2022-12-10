#Mundo 1 - Aula 6 - Ex04
#Métodos de string
n1 = input("Digite algo:")
print("O tipo primitivo desse valor é: {}".format(type(n1)))
print("Só digitou espaços? {}".format(n1.isspace()))
print("Só digitou números? {}".format(n1.isnumeric()))
print("Só digitou letras e números? {}".format(n1.isalnum()))
print("Só está em maiúsculas? {}".format(n1.isupper()))
print("Só está em maiúsculas? {}".format(n1.islower()))
print("Só está capitalizada? {}".format(n1.istitle()))
