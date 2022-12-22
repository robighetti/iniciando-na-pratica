import os

def clear():
    os.system("cls" if os.name == 'nt' else "clear")

def pause():
    input("Pressione ENTER para continuar...")

def header():
    print("**************************************************************")
    print("************** School of Net - Caixa Eletrônico **************")
    print("**************************************************************")
