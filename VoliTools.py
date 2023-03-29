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
                'texto': f'{Fore.GREEN}ip-keyloger(need to allow lesssecureapps ){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/shiky8/ip-keyloger.git',
            },
            '3': {
                'texto': f'{Fore.GREEN}MalwareSourceCode{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/vxunderground/MalwareSourceCode.git',
            },
            '4': {
                'texto': f'{Fore.GREEN}AdWare{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/SKocur/Simple-Adware.git',
            },
             '5': {
                'texto': f'{Fore.GREEN}RAMtester{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/SKocur/Malware-Collection/blob/master/h3wroMemoryLeaker.c',
            },
            '6': {
                'texto': f'{Fore.GREEN}RemoteClient{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/SKocur/Malware-Collection/blob/master/h3wroRemoterClient.cpp',
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
            '3':{
                'texto': f'{Fore.YELLOW}XploitSPY{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/XploitWizer-Community/XploitSPY.git'
            },
            '4':{
                'texto': f'{Fore.YELLOW}ADB-Xploit(usaras una dork en shodan2){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/henry-richard7/ADB-Xploit.git'
            }
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
             '11': {
                'texto': f'{Fore.CYAN}JwrXploiter{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/DontPanicO/jwtXploiter.git',
            },
             '11': {
                'texto': f'{Fore.CYAN}ToxSin{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/t3l3machus/toxssin.git',
            },
             '12': {
                'texto': f'{Fore.CYAN}Xless{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/r3curs1v3-pr0xy/xless.git',
            },
            '13': {
                'texto': f'{Fore.CYAN}Xsshunter-Express(Uso de Docker){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/r3curs1v3-pr0xy/xsshunter-express.git',
            },
            '14': {
                'texto': f'{Fore.CYAN}Sub404{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/r3curs1v3-pr0xy/sub404.git',
            },
        }
        
    },
    '5': {
        'texto': f'{Fore.BLUE}Cibersecurity{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.BLUE}hijackthis{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/dragokas/hijackthis.git',
            },
            '2': {
                'texto': f'{Fore.BLUE}apache-ultimate-bad-bot-blocker{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/mitchellkrogza/apache-ultimate-bad-bot-blocker.git',
            },
             '3': {
                'texto': f'{Fore.BLUE}SecurityXploit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/PhHitachi/SecurityXploit.git',
            },
             '4': {
                'texto': f'{Fore.BLUE}FazScan{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/mfazrinizar/FazScan.git',
            },
            '5': {
                'texto': f'{Fore.BLUE}Faz-SHC (encriptar el texto que le das a un Shellcode){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/mfazrinizar/Faz-SHC.git',
            },
             '6': {
                'texto': f'{Fore.BLUE}ssh-log-alerta{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/t3l3machus/ssh-log-alert.git',
            },
            '7': {
                'texto': f'{Fore.RED}BruteMySQL{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/S12cybersecurity/BruteMySQL.git',
            },
             '8': {
                'texto': f'{Fore.CYAN}Sub404{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/r3curs1v3-pr0xy/sub404.git',
            },
            '9': {
                'texto': f'{Fore.CYAN}Commix{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/commixproject/commix.git',
            },
            '10': {
                'texto': f'{Fore.CYAN}Dploot{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/zblurx/dploot.git',
            },
            '11': {
                'texto': f'{Fore.CYAN}ServiceDetector{Style.RESET_ALL}',
                'comando': ' git clone https://github.com/tothi/serviceDetector.git',
            },
             '12': {
                'texto': f'{Fore.CYAN}PdfSpeaker{Style.RESET_ALL}',
                'comando': ' git clone https://github.com/Toxic-Noob/PdfSpeaker.git',
            },
            '13': {
                'texto': f'{Fore.CYAN}ProcList{Style.RESET_ALL}',
                'comando': ' git clone https://github.com/S12cybersecurity/ProcList.git',
            },
             '14': {
                'texto': f'{Fore.CYAN}Hopper-Scripts{Style.RESET_ALL}',
                'comando': ' git clone https://github.com/droe/hopper-scripts.git',
            },
             '14': {
                'texto': f'{Fore.CYAN}Toolies{Style.RESET_ALL}',
                'comando': ' git clonehttps://github.com/expl0itabl3/Toolies',
            },
            
        }
    },
    '6': {
        'texto': f'{Fore.BLUE}Anonimato{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.BLUE}Whoami{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/owerdogan/whoami-project.git',
            },
            '2': {
                'texto': f'{Fore.BLUE}apache-ultimate-bad-bot-blocker{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/mitchellkrogza/apache-ultimate-bad-bot-blocker.git',
            },
        }
    },
    '7': {
        'texto': f'{Fore.BLUE}Obfuscacion{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.BLUE}javascript-obfuscator{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/javascript-obfuscator/javascript-obfuscator.git',
            },
            '2': {
                'texto': f'{Fore.BLUE}python-obfuscator{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/davidteather/python-obfuscator.git',
            },
             '3': {
                'texto': f'{Fore.BLUE}Emcc-obf(Esta basdo en LLVM y Docker){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/HakonHarnes/emcc-obf.git',
            },
            '4': {
                'texto': f'{Fore.BLUE}Chameleon{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/klezVirus/chameleon.git',
            },
            '5': {
                'texto': f'{Fore.BLUE}Boobsnail{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/STMCyber/boobsnail.git',
            },
        }
    },
    '8': {
        'texto': f'{Fore.RED}REDTEAMING{Style.RESET_ALL}',
        'opciones_secundarias': {
            '1': {
                'texto': f'{Fore.RED}Windows_Postex(Leer y editar, no funcionara sino lo editan ){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/A-mIn3/Windows_Postex.git',
            },
            '2': {
                'texto': f'{Fore.RED}gobiovuls(2016-2022){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/gobysec/GobyVuls.git',
            },
            
            '3': {
                'texto': f'{Fore.RED}ROPgadget (solo admite arquitecturas: x86, x64, ARM, ARM64, PowerPC, SPARC, MIPS){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/JonathanSalwan/ROPgadget.git',
            },
             '4': {
                'texto': f'{Fore.RED}Binary-Explotation{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/KazakosVas/Binary-Explotation.git',
            },
             '5': {
                'texto': f'{Fore.RED}Xploit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/shargon/Xploit.git',
            },
             '6': {
                'texto': f'{Fore.RED}AutoXploit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/Yashvendra/AutoXploit.git',
            },
            '7': {
                'texto': f'{Fore.RED}VertXploit(solo para control de acceso HID VertX y EDGE){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/coldfusion39/VertXploit.git',
            },
            '8': {
                'texto': f'{Fore.RED}0Day-Xploit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/maschil/0day-Xploit.git',
            },
             '9': {
                'texto': f'{Fore.RED}FollinaXploit(en caso de encontrar un objetivo sin parcharla aun){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/0xAbbarhSF/FollinaXploit.git',
            },
            '10': {
                'texto': f'{Fore.RED}FazPort{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/mfazrinizar/FazPort.git',
            },
             
             '12': {
                'texto': f'{Fore.RED}ADX{Style.RESET_ALL}',
                'comando': ' git clone https://github.com/djunekz/axd.git',
            },
            '13': {
                'texto': f'{Fore.RED}Villain (Hacer bypass al codeshell, preguntar por el bypass){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/t3l3machus/Villain.git',
            },
            '14': {
                'texto': f'{Fore.RED}Hoaxshell{Style.RESET_ALL}',
                'comando': ' git clone https://github.com/t3l3machus/hoaxshell.git',
            },
            '15': {
                'texto': f'{Fore.RED}WWWtree{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/t3l3machus/wwwtree.git',
            },
            '16': {
                'texto': f'{Fore.RED}PoC for CVE-2023-22960 :) denada{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/t3l3machus/CVE-2023-22960.git',
            },
            '17': {
                'texto': f'{Fore.RED}BabelStrike{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/t3l3machus/BabelStrike.git',
            },
            '18': {
                'texto': f'{Fore.RED}FileExtrator{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/a7t0fwa7/FileExtractor.git',
            },
            '19': {
                'texto': f'{Fore.RED}RedNeuron{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/S12cybersecurity/RedNeuron.git',
            },
            '20': {
                'texto': f'{Fore.RED}Chaos-Rootkit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/ZeroMemoryEx/Chaos-Rootkit.git',
            },
             '21': {
                'texto': f'{Fore.RED}WCE{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/Cyber-Guy1/WCE.git',
            },
             '21': {
                'texto': f'{Fore.RED}RatInject{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/5l1v3r1/RatInject.git',
            },
            '22': {
                'texto': f'{Fore.RED}Windows_LPE_AFD_CVE-2023-21768 (Elevacion de privilegios de procesos(PID) ){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/chompie1337/Windows_LPE_AFD_CVE-2023-21768.git',
            },
            '23': {
                'texto': f'{Fore.RED}Black-Angel-Rootkit{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/XaFF-XaFF/Black-Angel-Rootkit.git',
            },
            '23': {
                'texto': f'{Fore.RED}BruteMySQL{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/S12cybersecurity/BruteMySQL.git',
            },
             '24': {
                'texto': f'{Fore.RED}ExploitDB{Style.RESET_ALL}',
                'comando': 'git clone https://gitlab.com/exploit-database/exploitdb.git',
            },
            '25': {
                'texto': f'{Fore.RED}Boobsnail{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/STMCyber/boobsnail.git',
            },
            '26': {
                'texto': f'{Fore.RED}nosferatu (no funciona en AD){Style.RESET_ALL}',
                'comando': 'git clone https://github.com/kindtime/nosferatu.git',
            },
             '26': {
                'texto': f'{Fore.RED}persistencia en linux and servers{Style.RESET_ALL}',
                'comando': 'git clone https://github.com/Harsh-bash/Linux_Persistence_Techniques.git',
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
