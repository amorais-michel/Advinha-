import random# biblioteca random 

#escolhendo um numero random de 0 a 100
numero_aleatorio = random.randint(0,100)



print(numero_aleatorio)
tentativas = 0 # variavel que vai guardar o numero de tentativas feitas pelo usuario

while True:
	chute = int(input("\nAdvinhe o numero que eu escolhi:"))
	
	tentativas = tentativas + 1 # armazena o numero de tentativas
	
	if chute > numero_aleatorio: #dizendo se o chute é maior que o numero escolhido pelo Pc
		print("\nSeu chute è maior que o numero que eu estou pensando!")
	elif chute < numero_aleatorio: #dizendo se o chute é menor que o numero escolhido pelo Pc
		print("\nSeu chute é menor do que o numero que eu estou pensando")
		
	
	elif chute == numero_aleatorio: # se o chute for igual ao numero escolhido pelo Pc, o.usuario passa
		print("\nParabens, você acertou!\nVocê fez :", tentativas, "tentivas", "\nO número que eu pensei é:", numero_aleatorio, "\nTu digitou o numero:", chute, "e acertou")
		
		#encerrando o programa
		exit()
	    