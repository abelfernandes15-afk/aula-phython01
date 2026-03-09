import subprocess
import os 

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print('erro ao executar codico:')

def informaçao_sistema():
        executar_comando('systeminfo')


def scanear_sitema():
        executar_comando('sfc /scannow')


def reiniciar_pc():
        executar_comando('shutdow /r')

def mostar_conexao_rede():
    executar_comando('netstat -an') 

def mudar_cor():
    executar_comando('color/')

def partiçao_disco():
    executar_comando('diskpart')

def testador_dns():
    executar_comando('nslookup ')

def mapeamento_rede():
    executar_comando('arp -a')

def endereço_mac():
    executar_comando('getmac /v')

def criar_pasta():
    executar_comando('mkdir pasta nova')


def ping_host():
    host = input('digite o ip ou hostname')
    executar_comando(f'ping {host} ') 

def menu():
      while True:
            print('\n======= FERRAMENTA DE REDE ==========')
            print('1 INFORMÇAO DO SISTEMA')
            print('2 FAZER SCANNER DO SISTEMA ')
            print('3 REINICIAR PC')
            print('4 MOSTAR CONEXAO E REDE')
            print('5 MUDAR COR PROMPT ')
            print('6 PARTICIONAR DISCO')
            print('7 TESTAR CONEXAO DNS')
            print('8 MAPEAMENTO DA REDE')
            print('9 MOSTRAR ENDREÇO MAC')
            print('10 CRIAR PASTA')
            print('11 MOSTAR CONEXAO DE REDE')
            print('0 SAIR')
            print('============== criado por Douglas===========')
            opçao = str(input(' escolha '))

            match opçao:
                  case '1':
                   informaçao_sistema()
                  case '2':
                   scanear_sitema()
                  case '3':
                   reiniciar_pc()
                  case '4':
                   mostar_conexao_rede()
                  case '5':
                    mudar_cor()
                  case '6':
                    partiçao_disco()
                  case '7':
                    testador_dns()
                  case '8':
                    mapeamento_rede()
                  case '9':
                    endereço_mac()
                  case '10':
                   criar_pasta()
                  case '11':
                   mostar_conexao_rede()
                  case '0':
                   
                   print('saindo')
                   break
                  case _:
                    print('eita sabido')
if __name__== "__main__":
    menu()