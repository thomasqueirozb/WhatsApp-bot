from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import system
import code

# Abrir o Chrome driver
b = webdriver.Chrome("./chromedriver.exe")

# Entrar no Whatsapp Web
b.get('http://web.whatsapp.com')


def REPL():
	# Para debug
	variables = globals().copy()
	variables.update(locals())
	shell = code.InteractiveConsole(variables)
	shell.interact()



def clear():
	# Limpar o console
	_ = system('cls')


while True:

	nome = input("Digite o nome do grupo/pessoa: ").lower()

	if nome == 'exec' or nome == 'repl':
		REPL()
		continue
	elif nome == "exit":
		break

	elem = b.find_elements_by_class_name("_25Ooe") # Chats
	cond = False

	possiveis_nomes = []


	for i in range(len(elem)):
		if elem[i].text.lower() == nome:
			cond = True
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
		searchBox = b.find_elements_by_class_name("jN-F5")[0]

		searchBox.click()
		searchBox.clear()
		searchBox.send_keys(nome)

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
					name_index = int(input("Digite o número da pessoa/grupo")) + 1
					elem[name_index].click()
					print(f'{elem[name_index].text} foi selecionado')
					cond = True
				except:
					pass



	msg = input("Digite a mensagem: ")

	if msg == "exit":
		break
	elif msg == 'change':
		continue


	modo = input("0- Várias mensagens\n1- Letra por letra\n> ")



	try:
		txtBox = b.find_elements_by_class_name('_2S1VP')[0] # Caixa de texto
		if modo == "0":
			try:
				nvezes=int(input("Digite o número de vezes: "))
				cond = True

				if '@' not in msg:
					txtBox.clear()
					txtBox.send_keys(msg)
				else:
					txtBox.clear()
					msg = msg.split('@')
					firstPart = msg.pop(0)
					txtBox.send_keys(firstPart)
					for part in msg:
						part = part.split()
						txtBox.send_keys('@' + part.pop(0))
						txtBox.send_keys(Keys.TAB)
						part = ' '.join(part)
						txtBox.send_keys(part + " ")

				# Seleciona e copia
				txtBox.send_keys(Keys.CONTROL, 'a')
				txtBox.send_keys(Keys.CONTROL, 'c')
				for i in range(nvezes):
					# Cola
					txtBox.send_keys(Keys.CONTROL, 'v')
					txtBox.send_keys(Keys.ENTER)

			except KeyboardInterrupt:
				pass

		elif modo == "1":
			msg = msg.replace(" ","")
			for i in msg:
				txtBox.send_keys(i)
				txtBox.send_keys(Keys.ENTER)

		clear()

	except:
		print("Caixa de texto não encontrada")

from sys import exit
exit()
