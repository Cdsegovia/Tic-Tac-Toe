from machine import Pin
import time

# CONSTANTS
KEY_UP = const(0)
KEY_DOWN = const(1)
keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"],
]

# PIN NAMES
rows = [2, 3, 4, 5]
cols = [6, 7, 8, 9]
filas1 = [10, 11, 12]
cols1 = [13, 14, 15]
filas2 = [16, 17, 18]
cols2 = [19, 20, 21]
filas3 = [0, 1, 22]
cols3 = [26, 27, 28]

# Variables
filas_alternas1 = []
cols_alternas1 = []
filas_prueba1 = []
cols_prueba1 = []
filas_alternas2 = []
cols_alternas2 = []
filas_prueba2 = []
cols_prueba2 = []
Board1 = set()
Board2 = set()
Tablero1 = set()
Tablero_Empate = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
jugador = True

# Set raw pins of keypad as outputs
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]
# Set col pins of keypad as inputs
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]

# Set pins of leds as outputs
led_pinsR1 = [Pin(led_name, mode=Pin.OUT) for led_name in filas1]
led_pinsR2 = [Pin(led_name, mode=Pin.OUT) for led_name in filas2]
led_pinsC1 = [Pin(led_name, mode=Pin.OUT) for led_name in cols1]
led_pinsC2 = [Pin(led_name, mode=Pin.OUT) for led_name in cols2]
led_pinsR3 = [Pin(led_name, mode=Pin.OUT) for led_name in filas3]
led_pinsC3 = [Pin(led_name, mode=Pin.OUT) for led_name in cols3]

# Scan the keypad
def scan(row, col):
    row_pins[row].high()
    key = None

    # Check the key pressed
    if col_pins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if col_pins[col].value() == KEY_UP:
        key = KEY_UP
    row_pins[row].low()
    return key


def limpiar_tablero():
    for row in range(3):
        led_pinsR1[row].low()
        led_pinsR2[row].low()
        led_pinsR3[row].low()
    for col in range(3):
        led_pinsC1[col].high()
        led_pinsC2[col].high()
        led_pinsC3[col].high()

    filas_alternas1.clear()
    cols_alternas1.clear()
    filas_prueba1.clear()
    cols_prueba1.clear()
    filas_prueba2.clear()
    cols_prueba2.clear()
    filas_alternas2.clear()
    cols_alternas2.clear()
    Board1.clear()
    Board2.clear()
    Tablero1.clear()
    jugador = True


# Probar los Leds Azules
def prueba_leds1(a, b):
    led_pinsR1[a].high()
    led_pinsC1[b].low()
    led_pinsR1[a].low()
    led_pinsC1[b].high()


# Probar los Leds Rojos
def prueba_leds2(a, b):
    led_pinsR2[a].high()
    led_pinsC2[b].low()
    led_pinsR2[a].low()
    led_pinsC2[b].high()


# Prender los Leds Azules
def prender_leds1():
    for i in range(len(filas_alternas1)):
        led_pinsR1[filas_alternas1[i]].high()
        led_pinsC1[cols_alternas1[i]].low()
        led_pinsR1[filas_alternas1[i]].low()
        led_pinsC1[cols_alternas1[i]].high()


# Prender los Leds Rojos
def prender_leds2():
    for i in range(len(filas_alternas2)):
        led_pinsR2[filas_alternas2[i]].high()
        led_pinsC2[cols_alternas2[i]].low()
        led_pinsR2[filas_alternas2[i]].low()
        led_pinsC2[cols_alternas2[i]].high()


# Comprobar ganador
def comprobar_ganador():
    # Leds Azules. Por las Filas
    if "1" in Board1 and "2" in Board1 and "3" in Board1:
        print("El jugador 1 es el ganador")
        led_pinsR3[0].high()
        for i in range(3):
            led_pinsC3[i].low()

    elif "4" in Board1 and "5" in Board1 and "6" in Board1:
        print("El jugador 1 es el ganador")
        led_pinsR3[1].high()
        for i in range(3):
            led_pinsC3[i].low()

    elif "7" in Board1 and "8" in Board1 and "9" in Board1:
        print("El jugador 1 es el ganador")
        led_pinsR3[2].high()
        for i in range(3):
            led_pinsC3[i].low()

    # Por las Columnas
    if "1" in Board1 and "4" in Board1 and "7" in Board1:
        print("El jugador 1 es el ganador")
        led_pinsC3[0].low()
        for i in range(3):
            led_pinsR3[i].high()

    elif "2" in Board1 and "5" in Board1 and "8" in Board1:
        print("El jugador 1 es el ganador")
        led_pinsC3[1].low()
        for i in range(3):
            led_pinsR3[i].high()

    elif "3" in Board1 and "6" in Board1 and "9" in Board1:
        print("El jugador 1 es el ganador")
        led_pinsC3[2].low()
        for i in range(3):
            led_pinsR3[i].high()

    # Por las diagonales
    if "1" in Board1 and "5" in Board1 and "9" in Board1:
        print("El jugador 1 es el ganador")
        for i in range(3):
            led_pinsR3[i].high()
            led_pinsC3[i].low()
            led_pinsR3[i].low()
            led_pinsC3[i].high()

    elif "7" in Board1 and "5" in Board1 and "3" in Board1:
        print("El jugador 1 es el ganador")
        i1 = 0
        i2 = 2
        while i1 <= 2 and i2 >= 0:
            led_pinsR3[i1].high()
            led_pinsC3[i2].low()
            led_pinsC3[i2].high()
            led_pinsR3[i1].low()
            i1 += 1
            i2 -= 1

    # Leds Rojos. Por las Filas
    if "1" in Board2 and "2" in Board2 and "3" in Board2:
        print("El jugador 2 es el ganador")
        led_pinsR3[0].high()
        for i in range(3):
            led_pinsC3[i].low()

    elif "4" in Board2 and "5" in Board2 and "6" in Board2:
        print("El jugador 2 es el ganador")
        led_pinsR3[1].high()
        for i in range(3):
            led_pinsC3[i].low()

    elif "7" in Board2 and "8" in Board2 and "9" in Board2:
        print("El jugador 2 es el ganador")
        led_pinsR3[2].high()
        for i in range(3):
            led_pinsC3[i].low()

    # Por las Columnas
    if "1" in Board2 and "4" in Board2 and "7" in Board2:
        print("El jugador 2 es el ganador")
        led_pinsC3[0].low()
        for i in range(3):
            led_pinsR3[i].high()

    elif "2" in Board2 and "5" in Board2 and "8" in Board2:
        print("El jugador 2 es el ganador")
        led_pinsC3[1].low()
        for i in range(3):
            led_pinsR3[i].high()

    elif "3" in Board2 and "6" in Board2 and "9" in Board2:
        print("El jugador 2 es el ganador")
        led_pinsC3[2].low()
        for i in range(3):
            led_pinsR3[i].high()

    # Por las diagonales
    if "1" in Board2 and "5" in Board2 and "9" in Board2:
        print("El jugador 2 es el ganador")
        for i in range(3):
            led_pinsR3[i].high()
            led_pinsC3[i].low()
            led_pinsR3[i].low()
            led_pinsC3[i].high()

    elif "7" in Board2 and "5" in Board2 and "3" in Board2:
        print("El jugador 2 es el ganador")
        i1 = 0
        i2 = 2
        while i1 <= 2 and i2 >= 0:
            led_pinsR3[i1].high()
            led_pinsC3[i2].low()
            led_pinsC3[i2].high()
            led_pinsR3[i1].low()
            i1 += 1
            i2 -= 1

    # Comprobar Empate
    if Board1 | Board2 == Tablero_Empate:
        print("Se ha producido un empate")


# Valor de Prueba en Leds Azules
def probar_valor1(row, col):
    filas_prueba1.append(row)
    cols_prueba1.append(col)


# Valor de Prueba en Leds Rojos
def probar_valor2(row, col):
    filas_prueba2.append(row)
    cols_prueba2.append(col)


# Guardar valor en Leds Azules
def guardar_valor1(a, b):
    filas_alternas1.append(a)
    cols_alternas1.append(b)
    Board1.add(keys[a][b])


# Guardar valor en Leds Rojos
def guardar_valor2(c, d):
    filas_alternas2.append(c)
    cols_alternas2.append(d)
    Board2.add(keys[c][d])


# Se repitió una jugada
def jugada_repetida(r, c):
    led_pinsR3[r].high()
    led_pinsC3[c].low()
    time.sleep(3)
    led_pinsR3[r].low()
    led_pinsC3[c].high()


# Init of program
def init():
    limpiar_tablero()


# Funcion Principal
def loop():
    while True:
        for row in range(4):
            for col in range(4):
                key = scan(row, col)
                if key == KEY_DOWN:
                    print("Key Pressed: ", keys[row][col])
                    # Leds Azules
                    if len(Tablero1) % 2 == 0:
                        if (
                            keys[row][col] != "A"
                            and keys[row][col] != "B"
                            and keys[row][col] != "C"
                            and keys[row][col] != "D"
                            and keys[row][col] != "#"
                            and keys[row][col] != "0"
                            and keys[row][col] != "*"
                        ):
                            probar_valor1(row, col)
                            a = row
                            b = col
                        if len(filas_prueba1) > 0 and keys[row][col] == "0":
                            guardar_valor1(a, b)
                            Tablero1.add(keys[a][b])
                            time.sleep(1.5)
                    # Leds Rojos
                    else:
                        if (
                            keys[row][col] != "A"
                            and keys[row][col] != "B"
                            and keys[row][col] != "C"
                            and keys[row][col] != "D"
                            and keys[row][col] != "#"
                            and keys[row][col] != "0"
                            and keys[row][col] != "*"
                        ):
                            probar_valor2(row, col)
                            a = row
                            b = col
                        if len(filas_prueba2) > 0 and keys[row][col] == "0":
                            guardar_valor2(a, b)
                            Tablero1.add(keys[a][b])
                            time.sleep(1.5)
                    # Reiniciar partida
                    if keys[row][col] == "*":
                        limpiar_tablero()

        # Probar el LED Azul
        if len(filas_prueba1) > 0:
            f = filas_prueba1.pop()
            c = cols_prueba1.pop()
            filas_prueba1.append(f)
            cols_prueba1.append(c)
            prueba_leds1(f, c)

        # Probar el LED Rojo
        if len(filas_prueba2) > 0:
            f = filas_prueba2.pop()
            c = cols_prueba2.pop()
            filas_prueba2.append(f)
            cols_prueba2.append(c)
            prueba_leds2(f, c)

        # Prender el LED Azul
        if len(filas_alternas1) > 0:
            prender_leds1()

        # Prender el LED Rojo
        if len(filas_alternas2) > 0:
            prender_leds2()

        # Comprobar jugada repetida
        if len(Board1 & Board2) != 0:
            if len(Tablero1) % 2 == 0:
                Board1 = Board1 - Board2
                r = filas_alternas1.pop()
                c = cols_alternas1.pop()
                jugada_repetida(r, c)

            else:
                Board2 = Board2 - Board1
                r = filas_alternas2.pop()
                c = cols_alternas2.pop()
                jugada_repetida(r, c)

        # Determinar si hubo ganador
        comprobar_ganador()


# Inicio del programa
if __name__ == "__main__":
    init()
    loop()
