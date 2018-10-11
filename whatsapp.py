from selenium import webdriver

b = webdriver.Chrome("C:/Users/thoma/Documents/Python/chromedriver.exe")
# Requesting the web version of whatsapp
b.get('http://web.whatsapp.com')
from time import sleep

from selenium.webdriver.common.keys import Keys
from os import system
def REPL():
	while True:
	    command=input(">>> ")
	    if command in ["exit","exit()","quit","quit()"]:
	        break
	    try:
	        exec(command)
	        try:
	            print(eval(command))
	        except:
	            pass
	    except:
	        print("fudeu bro")



def clear():
	_ = system('cls')

while True:
	nome = input("Digite o nome do grupo/pessoa: ").lower()
	if nome=='exec':
		REPL()
		continue
	elem = b.find_elements_by_class_name("_25Ooe")#nome
	cond=False

	possiveis_nomes=[]


	for i in range(len(elem)):
		if elem[i].text.lower() == nome:
			cond=True
			elem[i].click()
			break
		elif nome in str(elem[i].text.lower()):
			possiveis_nomes.append([elem[i],i])

	else:
		if len(possiveis_nomes) == 1:
			# print(possiveis_nomes)
			elem[possiveis_nomes[0][1]].click()
			print(f'{possiveis_nomes[0][0].text} foi selecionado')
			cond = True

		elif len(possiveis_nomes) > 1:
			try:
				for i,j in zip(possiveis_nomes,range(len(possiveis_nomes))):
					print(f'{j+1} - {i[0].text}')
				name_index = int(input("Digite o número da pessoa/grupo: ")) - 1
				elem[name_index][1].click()
				print(f'{elem[name_index][0].text} foi selecionado')
				cond = True
			except:
				pass

	if not cond:
		search = b.find_elements_by_class_name("jN-F5")

		search[0].click()
		search[0].clear()
		search[0].send_keys(nome)

		try:
			sleep(2)

			elem = b.find_elements_by_class_name("_25Ooe")
		except:
			continue

		if len(elem) == 0:
			continue

		for i in range(len(elem)):
			if elem[i].text.lower() == nome:
				cond=True
				elem[i].click()
				break
			elif nome in elem[i].text.lower():
				possiveis_nomes.append(elem[i])

		else:
			if len(possiveis_nomes) == 1:
				elem[i].click()
				print(f'{elem[i].text} foi selecionado')
				cond = True

			elif len(possiveis_nomes) > 1:
				try:
					for i,j in zip(possiveis_nomes,range(len(possiveis_nomes))):
						print(f'{j+1} - {i.text}')
					name_index=int(input("Digite o número da pessoa/grupo"))+1
					elem[name_index].click()
					print(f'{elem[name_index].text} foi selecionado')
					cond = True
				except:
					pass



	msg=input("Digite a mensagem: ")

	if msg=="exit":
		break
	elif msg=='change':
		continue

	modo=input("0- Várias mensagens\n1- Letra por letra\n")



	try:
		elem1 = b.find_elements_by_class_name('_2S1VP')#texto
		# print(dir(elem1[0]))
		if modo == "0":
			try:
				nvezes=int(input("Digite o número de vezes: "))

				cond=True
				for i in range(nvezes):
					elem1[0].send_keys(msg)
					s=b.find_elements_by_class_name("_35EW6")
					s[0].click()
			except KeyboardInterrupt:
				pass

		elif modo == "1":
			msg=msg.replace(" ","")
			for i in msg:
				elem1[0].send_keys(i)
				s=b.find_elements_by_class_name("_35EW6")
				s[0].click()

		clear()
	except:
		print("Caixa de texto não encontrada")
from sys import exit
exit()
