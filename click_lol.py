import pyautogui
import time

def click_botao(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def verificar_tela(tempo_limite):
    tempo_inicial = time.time()
    while True:
        if time.time() - tempo_inicial > tempo_limite:
            print('Tempo excedido')
            return False
        try:
            button_pos = pyautogui.locateOnScreen("aceitar.png", confidence=0.7)
            if button_pos is not None:
                click_botao(button_pos.left, button_pos.top)
            return True
        except pyautogui.ImageNotFoundException:
            pass  

def main():
    tempo_limite = 600
    resultado = verificar_tela(tempo_limite)
    if not resultado:
        print('Programa finalizado, nada encontrado!')

main()    