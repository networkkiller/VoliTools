import os
from colorama import Fore, Style, init
init()
TOOLS_PATH = "tools"

if not os.path.isdir(TOOLS_PATH):
    os.mkdir(TOOLS_PATH)
opciones = {
    '1': {
        'texto': f'{Fore.GREEN}Malwares{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto':  f'{Fore.GREEN}Ramsonware{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/repo1_1.git',
            },
            '2': {
                'texto': f'{Fore.GREEN}Keyloger{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/repo1_2.git',
            },
            '3': {
                'texto': f'{Fore.GREEN}Troyano{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/repo1_2.git',
            },
        }
    },
    '2': {
        'texto': f'{Fore.YELLOW}Hacking Android{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.YELLOW}KitHack{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/AdrMXR/KitHack.git',
            },
            '2': {
                'texto': f'{Fore.YELLOW}AndroidRat{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/repo2_2.git',
            },
        }
    },
    '3': {
        'texto': f'{Fore.RED}Hacking Redes sociales{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.RED}Zphisher{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/htr-tech/zphisher.git',
            },
            '2': {
                'texto': f'{Fore.RED}Pyphisher{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/KasRoudra/PyPhisher.git',
            },
        }
    },
}

def mostrar_opciones_secundarias(opciones_secundarias):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nSeleccione una opción:\n')
    for key, value in opciones_secundarias.items():
        print(f'[{key}] {value["texto"]}')


os.system('cls' if os.name == 'nt' else 'clear')
print("""
     ██████████                                              █████   █████            █████           
░░███░░░░░█                                             ░░███   ░░███            ░░███            
 ░███  █ ░  █████ █████  ██████  ████████  █████ ████    ░███    ░███   ██████   ███████    █████ 
 ░██████   ░░███ ░░███  ███░░███░░███░░███░░███ ░███     ░███████████  ░░░░░███ ░░░███░    ███░░  
 ░███░░█    ░███  ░███ ░███████  ░███ ░░░  ░███ ░███     ░███░░░░░███   ███████   ░███    ░░█████ 
 ░███ ░   █ ░░███ ███  ░███░░░   ░███      ░███ ░███     ░███    ░███  ███░░███   ░███ ███ ░░░░███
 ██████████  ░░█████   ░░██████  █████     ░░███████     █████   █████░░████████  ░░█████  ██████ 
░░░░░░░░░░    ░░░░░     ░░░░░░  ░░░░░       ░░░░░███    ░░░░░   ░░░░░  ░░░░░░░░    ░░░░░  ░░░░░░  
                                            ███ ░███                                              
                                           ░░██████                                               
                                            ░░░░░░                  
                                            𝖌𝖎𝖙𝖍𝖚𝖇 Networkkiller
    """)
print('Seleccione una opción:\n')
for key, value in opciones.items():
    print(f'[{key}] {value["texto"]}')

opcion_principal = input('\nOpción seleccionada: ')

if opcion_principal in opciones:
    opciones_secundarias = opciones[opcion_principal]['opciones_secundarias']
    mostrar_opciones_secundarias(opciones_secundarias)

    opcion_secundaria = input('\nOpción seleccionada: ')

    if opcion_secundaria in opciones_secundarias:
        os.system(opciones_secundarias[opcion_secundaria]['comando'])
        
    else:
        print('Opción no válida')
else:
    print('Opción no válida')

os.system('cls' if os.name == 'nt' else 'clear')
