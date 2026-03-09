while True:
    escolha = str(input('confirmar opçao'))
    match escolha:
    case "sim"| 'yes'| 'y'
      print('confirmado')
      break
    case "nao"| "no"|"nope"
      print('rejeitado')
      break
    case _ :
      print('selecione novamente')