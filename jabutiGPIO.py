import RPi.GPIO as GPIO
import  time

class motor(object):
    def  __init__(self, pinDireita, pinEsquerda):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinEsquerda,GPIO.OUT) 
        GPIO.setup(pinDireita,GPIO.OUT) 

        self.motorEsquerda = GPIO.PWM(pinEsquerda,50)
        self.motorDireita = GPIO.PWM(pinDireita,50)
        self.motorEsquerda.start(7.5)	
        self.motorDireita.start(7.5)	
        self.stop()

    def move(self, motorEsquerdo, motorDireito, tempo):
        self.motorEsquerda.ChangeDutyCycle(motorEsquerdo)
        self.motorDireita.ChangeDutyCycle(motorDireito)
        time.sleep(tempo)
        self.stop()
    
    def stop(self):
        self.motorEsquerda.ChangeDutyCycle(0)
        self.motorDireita.ChangeDutyCycle(0)

    def gpioCleanup(self):
        GPIO.cleanup()

    def queue(self,  comando):
        print(comando)
        for item in comando:
            print(item)
            if item  == "frente":
                self.move(4, 12, 1)  #frente 
            elif item  == "re":
                self.move(8, 4, 1)  #reh
            elif item  == "direita":
                self.move(10, 10, 0.7)  #direita
            elif item  == "esquerda":
                self.move(4, 4, 0.63)  #esquerda
        