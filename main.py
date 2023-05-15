from controles import cargar
from pynput.keyboard import Controller
import serial as s

controlador = Controller()

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
                    controlador.press(controles['arriba'])
                    controlador.release(controles['arriba'])
                elif cadena == "abajo":
                    controlador.press(controles['abajo'])
                    controlador.release(controles['abajo'])
                elif cadena == "izquierda":
                    controlador.press(controles['izquierda'])
                    controlador.release(controles['izquierda'])
                elif cadena == "derecha":
                    controlador.press(controles['derecha'])
                    controlador.release(controles['derecha'])
                elif cadena == "seleccionar":
                    controlador.press(controles['select'])
                    controlador.release(controles['select'])
                elif cadena == "iniciar":
                    controlador.press(controles['start'])
                    controlador.release(controles['start'])
                elif cadena == "A":
                    controlador.press(controles['botonA'])
                    controlador.release(controles['botonA'])
                elif cadena == "B":
                    controlador.press(controles['botonB'])
                    controlador.release(controles['botonB'])
                elif cadena == "apagar":
                    arduino.close()
                    print("desconectado")
                    break
        except Exception as error:
            print(error)

