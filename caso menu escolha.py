 
escolha= int(input ('digite sua escolha 1 ao 4:'))
match escolha:
  case 1:
   print('PC ESCRITORIO :\ncore i3, ddr3 8 mram,hd500 giga, monitor 15 polegada,fonte 500 wts')
  case 2:
    print('PC GAMER:\nryser7 ,placa de video 4090, ddr4 32gram,1t memoria,monitor 19 polegada, fonte 850wts ')
  case 3:
    print('PC DOMESTICO: \ncore i3, hd 250g, ddr2 4 gram,monitor 14 polegada,fontes 450wts')
  case 4:
    print('PC PROJETOS:\nryzer9,ddr5 64gram,ssd 2trb,water coller,placa de video 5090ti,fonte 1000wts')
  case _:
    print('escolha outra opçao')