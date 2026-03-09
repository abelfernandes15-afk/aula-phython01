#
import subprocess
import os 

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print('erro ao executar codico:')

def mostar_ip():
        executar_comando('ipconfig')


def renovar_ip():
        executar_comando('ipconfig /renew')


def mostar_ip_completo():
        executar_comando('ipconfig / all')


def ping_host():
    host = input('digite o ip ou hostname')
    executar_comando(f'ping {host} ') 

def menu():
      while True:
            print('\n======= FERRAMENTA DE REDE ==========')
            print('1 MOSTAR IP')
            print('2 MOSTAR CONFIGURAÇAO DE REDE COMPLETA ')
            print('4 PING')
            print('0 SAIR ')
            print('============== criado por Douglas===========')
            opçao = str(input(' escolha '))

            match opçao:
                  case '1':
                   mostar_ip()
                  case '2':
                   renovar_ip()
                  case '3':
                   mostar_ip_completo()
                  case '4':
                   ping_host()
                  case '0':
                   print('saindo')
                   break
                  case _:
                    print('eita sabido')
if __name__== "__main__":
    menu()