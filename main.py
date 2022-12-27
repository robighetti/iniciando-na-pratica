from utils import clear, header
from console import CashMachineConsole

def main():
  clear()

  header()

  CashMachineConsole.get_menu_options_typed()

  #logica do cx eletronico

if __name__ == '__main__':
  while True:
    main()

    input("Pressione <Enter> para continuar...")