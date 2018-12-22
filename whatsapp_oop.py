from selenium.webdriver.common.keys import Keys
from time import sleep
import os, sys
import code

from bot import Bot

def REPL():
	# Para debug
	variables = globals().copy()
	variables.update(locals())
	shell = code.InteractiveConsole(variables)
	shell.interact()



with Bot() as b:
    while True:
        # Pede o nome da pessoa
        nome = input("Digite o nome do grupo/pessoa: ").lower()

        # Se o nome da pessoa for exec ou repl, entrar em debug mode
        if nome == 'exec' or nome == 'repl':
            REPL()
            continue

        # Se o nome da pessoa for exit, para o programa
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
                    for j, i in enumerate(possiveis_nomes):
                        print(f'{j+1} - {i[0].text}')
                    name_index = input("Digite o número da pessoa/grupo: ")
                    name_index = int(name_index) - 1

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
                    cond = True
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
                        for j, i in enumerate(possiveis_nomes):
                            print(f'{j+1} - {i.text}')
                        name_index = int(input("Digite o número da pessoa/grupo")) + 1
                        elem[name_index].click()
                        print(f'{elem[name_index].text} foi selecionado')
                        cond = True
                    except:
                        pass



        msg = input("Digite a mensagem ou 'foto': ")



        if msg == 'exit':
            break
        elif msg == 'change':
            continue

        if msg != 'foto':
            modo = input("0- Várias mensagens\n1- Letra por letra\n> ")

            try:
                txtBox = b.find_elements_by_class_name('_2S1VP')[0] # Caixa de texto
                if modo == "0":
                    try:
                        nvezes=int(input("Digite o número de vezes: "))
                        cond = True
                        txtBox.clear()

                        if '@' not in msg:
                            txtBox.send_keys(msg)
                        else:
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
        else:
            print('Foto')

            # try:
            # 	txtBox = b.find_elements_by_class_name('_2S1VP')[0] # Caixa de texto
            # 	from PIL import Image
            # 	from io import BytesIO
            # 	import win32clipboard
            # 	try:
            # 		nvezes = int(input("Digite o número de vezes: "))
            # 		cond = True
            # 		path = input("Path da photo: ")
            # 		path = rf'{path}'

            # 		# copiar imagem pro clipboard
            # 		def send_to_clipboard(clip_type, data):
            # 		    win32clipboard.OpenClipboard()
            # 		    win32clipboard.EmptyClipboard()
            # 		    win32clipboard.SetClipboardData(clip_type, data)
            # 		    win32clipboard.CloseClipboard()

            # 		image = Image.open(path)

            # 		output = BytesIO()
            # 		image.convert("RGB").save(output, "BMP")
            # 		data = output.getvalue()[14:]
            # 		output.close()

            # 		send_to_clipboard(win32clipboard.CF_DIB, data)

            # 		for i in range(nvezes):
            # 			# Cola a imagem e manda
            # 			txtBox.send_keys(Keys.CONTROL, 'v')
            # 			txtBox.send_keys('.')
            # 			sleep(0.5)
            # 			enterbox = b.find_elements_by_class_name('_2S1VP')[0]
            # 			enterbox.send_keys(Keys.ENTER)
            # 			sleep(1.5)
            # 	except:
            # 		pass
            # except KeyboardInterrupt:
            # 	pass


b.close()
b.quit()
sys.exit()

# C:\Users\thoma\Downloads\amoeba.jpg
