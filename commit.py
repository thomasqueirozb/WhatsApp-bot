from subprocess import call
from os import getcwd

path = getcwd()

print(f'>>> cd {path}')
call(f'cd {path}', shell = True)

msg = input("Commit message: ")


if msg == '':
    msg = 'Auto'

if msg.lower() not in ['exit', 'quit', 'q']:
    print('>>> git add *')
    call('git add *')
    
    print(f'>>> git commit -m {msg}')
    call(f'git commit -m "{msg}"')

    print('>>> git push')
    call('git push')
