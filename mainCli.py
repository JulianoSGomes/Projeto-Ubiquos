import jabutiGPIO
import sys 



controle = jabutiGPIO.motor(11, 7)


recived = sys.argv[1]


for item in recived:
    print (item)
    if item  == "f":
        controle.move(4, 8, 1)  #frente 
        print("chama a função  frente")
    elif item  == "t":
        controle.move(8, 4, 1)  #reh
        print("chama a função  back")
    elif item  == "d":
        controle.move(8, 8, 0.7)  #direita
        print("chama a função  direita")
    elif item  == "e":
        controle.move(4, 4, 0.7)  #direita
        print("chama a função  esquerda")




# controle.direcao(4, 8, 1)  #frente 
# controle.direcao(8, 4, 1)  #reh
# controle.direcao(8, 8, 0.7)  #direita
#controle.direcao(4, 4, 0.63)  #esquerda







controle.gpioCleanup()
