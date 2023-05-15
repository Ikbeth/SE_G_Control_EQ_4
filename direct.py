from controles import cargar
import pydirectinput as k
import serial as s

k.PAUSE = 0


if __name__ == '__main__':
    controles = cargar()

    try:
        arduino = None
        puerto = 'COM' + controles['puerto']
        arduino = s.Serial(puerto, baudrate=9600, timeout=0.5)
        if arduino.isOpen() == True:
            print("conectado")
    except Exception as error:
        print(error)

    while True:
        try:
            if arduino.isOpen() == True:
                cadena = arduino.readline().decode()
                cadena = cadena.replace("\n", "")
                cadena = cadena.replace("\r", "")

            if not cadena == "":
                if cadena == "arriba":
                    k.keyDown(controles['arriba'])
                    k.keyUp(controles['arriba'])2
                elif cadena == "abajo":
                    k.keyDown(controles['abajo'])
                    k.keyUp(controles['abajo'])
                elif cadena == "izquierda":
                    k.keyDown(controles['izquierda'])
                    k.keyUp(controles['izquierda'])
                elif cadena == "derecha":
                    k.keyDown(controles['derecha'])
                    k.keyUp(controles['derecha'])
                elif cadena == "seleccionar":
                    k.keyDown(controles['select'])
                    k.keyUp(controles['select'])
                elif cadena == "iniciar":
                    k.keyDown(controles['start'])
                    k.keyUp(controles['start'])
                elif cadena == "A":
                    k.keyDown(controles['botonA'])
                    k.keyUp(controles['botonA'])
                elif cadena == "B":
                    k.keyDown(controles['botonB'])
                    k.keyUp(controles['botonB'])
                elif cadena == "apagar":
                    arduino.close()
                    print("desconectado")
                    break
        except Exception as error:
            print(error)

