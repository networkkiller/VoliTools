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
                'comando': 'git clone https://github.com/networkkiller/PainFile.git',
            },
            '2': {
                'texto': f'{Fore.GREEN}Keyloger{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/repo1_2.git',
            },
            '3': {
                'texto': f'{Fore.GREEN}MalwareSourceCode{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/vxunderground/MalwareSourceCode.git',
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
    '4': {
        'texto': f'{Fore.CYAN}Hacking WEb{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.CYAN}Dirsearch{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/maurosoria/dirsearch.git',
            },
            '2': {
                'texto': f'{Fore.CYAN}Scout2{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/nccgroup/Scout2.git',
            },
            '3': {
                'texto': f'{Fore.CYAN}Sqlmap{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/sqlmapproject/sqlmap.git',
            },
             '4': {
                'texto': f'{Fore.CYAN}Wpsploit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/espreto/wpsploit.git',
            },
            '5': {
                'texto': f'{Fore.CYAN}WS-Attacker{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/RUB-NDS/WS-Attacker.git',
            },
            '6': {
                'texto': f'{Fore.CYAN}Wpscan{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/wpscanteam/wpscan.git',
            },
            '7': {
                'texto': f'{Fore.CYAN}Timing_Attack{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/ffleming/timing_attack.git',
            },
            '8': {
                'texto': f'{Fore.CYAN}angularjs-csti-scanner{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/tijme/angularjs-csti-scanner.git',
            },
            '9': {
                'texto': f'{Fore.CYAN}WhatWeb{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/urbanadventurer/WhatWeb.git',
            },
            '10': {
                'texto': f'{Fore.CYAN}Git-Scanner{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/HightechSec/git-scanner.git',
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
