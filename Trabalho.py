# Conversor de unidades
import time
# Variaves
espace = ' '
# Funções
def units():
  print(f'Qual a unidade de comprimento que será convertida?\n(1)Metro{espace * 10}(4)Polegada\n(2)Centíemtro{espace * 5}(5)Milha\n(3)pé')
# Unidades fundamentais
def fund_selector ():
  time.sleep(2)
  print('\n\nEscolha qual unidade fundamental deseja converter')
  time.sleep(0.5)
  print(f'(1)Comprimento{espace*5}(3)Temperatura\n(2)Tempo{espace*11}(4)Massa')
  tipo1 = (int(input()))
  if tipo1 == 1:
    comprimento()
# Unidades múltiplas
def mult_selector():
  time.sleep(2)
  print('Escolha qual unidade múltipla deseja converter')
  time.sleep(0.5)
  print(f'\n\n(1)Nano{espace*5}(4)Quilo\n(2)Micro{espace*4}(5)Mega\n(3)Mili{espace*5}(6)Giga')
# Unidades derivadas
def deri_selector ():
  time.sleep(2)
  print('Escolha qual derivada deseja converter')
  time.sleep(0.5)
  print(f'(1)Volume{espace*5}(4)Energia\n(2)Força{espace*6}(5)Potência\n(3)Pressão')
#Comprimento
def comprimento ():
  units()
  unit_class = int(input())
  print('Para qual unidade deseja converter?')
  units()
  unit_class_2 = int(input())
  if unit_class == unit_class_2:
    time.sleep(0.5)
    print('\nSelecione uma unidade diferente da atual')
    time.sleep(1.5)
    return comprimento()
  elif unit_class == 1 and unit_class_2 == 2:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value*100} cm')
  elif unit_class == 1 and unit_class_2 == 3:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value*3.281} ft')
  elif unit_class == 1 and unit_class_2 == 4:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value*39.37} in')
  elif unit_class == 1 and unit_class_2 == 5:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/1609} mi')
  elif unit_class == 2 and unit_class_2 == 1:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/100}')
  elif unit_class == 2 and unit_class_2 == 1:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/100} m')
  elif unit_class == 2 and unit_class_2 == 3:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/30,48} ft')
  elif unit_class == 2 and unit_class_2 == 4:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/2.54} in')
  elif unit_class == 2 and unit_class_2 == 5:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/160934} mi')
  elif unit_class == 3 and unit_class_2 == 1:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value/3.281} m')
  elif unit_class == 3 and unit_class_2 == 2:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value} cm')
  elif unit_class == 3 and unit_class_2 == 4:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value} in')
  elif unit_class == 3 and unit_class_2 == 5:
    print('Insira o valorda unidade:')
    value = float(input())
    print(f'O valor é de {value} mi')
# Home Page
print('Olá, seja bem-vindo ao programa de conversão de unidades.')
def interaction():
  time.sleep(1.5)
  print('Como deseja ser chamado?')
  time.sleep(0.5)
  name = str(input())
  if len(name) > 30:
    print('Por favor insira um nome de no máximo 30 caracteres')
    return interaction()
  time.sleep(1.5)
  print(f'Então vamos dar inicio aos cálculos, {name[:15]}.')
interaction()
# Selection
def selection_menu ():
  time.sleep(2)
  print('\n\n\nQual o tipo da unidade que será utilizada?')
  time.sleep(0.5)
  print(f'(1)Unidades fundamentais{espace*5}(3)Unidades derivadas\n(2)Unidades múltiplas')
  unit = (int(input()))
  if unit == 1:
      return(fund_selector())
  if unit == 2:
      return(mult_selector())
  if unit == 3:
    (deri_selector())
selection_menu()
