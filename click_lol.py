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
            botao_pos = pyautogui.locateOnScreen("aceitar.png", confidence=0.7)
            if botao_pos is not None:
                click_botao(botao_pos.left, botao_pos.top)
            return True
        except pyautogui.ImageNotFoundException:
            pass  

def main():
    tempo_limite = 600
    resultado = verificar_tela(tempo_limite)
    if not resultado:
        print('Programa finalizado, nada encontrado!')

main()    
