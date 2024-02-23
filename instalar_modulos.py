# Instalar Módulos Novos

# Abrir o terminal;
# Instalar usando o pip;
# Reiniciar a IDE.

"""
Tive que importar a biblioteca webbrowser, pois minha IDE não é dentro do próprio navegador, sendo assim, precisando abrir
o navegador primeiro.
"""

import keyboard
import webbrowser

webbrowser.open("https://www.google.com")
keyboard.press_and_release('ctrl+t')
keyboard.write('hashtagtreinamentos.com')
keyboard.press_and_release('enter')