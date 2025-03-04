from utilita import Ui_Form     #Importa a classe Ui_Form da utilita.py
from sobre import Ui_Form_2     #Importa a classe Ui_Form_2 da sobre.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget #Importa as classes necessarias
from PyQt6.QtCore import Qt #Importa a classe Qt
import subprocess #Importa a biblioteca subprocess

class Sobre(QWidget): #Classe Sobre herda de QWidget
    def __init__(self):
        super().__init__()    #Chama o construtor da classe pai
        self.ui = Ui_Form_2() #Cria um objeto da classe Ui_Form_2
        self.ui.setupUi(self) 
        self.setWindowTitle("Sobre")

class InstaladorUtil(QMainWindow): #Classe InstaladorUtil herda de QMainWindow
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Form()
        self.ui.setupUi(self) #Chama a função setupUi da classe Ui_Form
        self.setWindowTitle("QuickGet App Installer")

        self.Sobre = None 
        self.ui.button_about.clicked.connect(self.abrir_sobre) #Botao Sobre chama a função abrir_sobre
        

        self.mapeamento_softwares = { 
            #preencher os nomes:comando 
            #Browsers"
            "Google Chrome": "Google.Chrome",
            "Brave": "Brave.Brave",
            "Firefox": "Mozilla.Firefox",
            "Opera": "Opera.OperaGX",
            "Tor": "TorProject.TorBrowser",
            "Vivaldi Browser": "VivaldiTechnologies.Vivaldi",
            "Microsoft Edge": "Microsoft.Edge",
            "LibreWolf": "LibreWolf.LibreWolf",
            "Ungoogled Chromium": "Ungoogled.Chromium",
            "Waterfox": "Waterfox.Waterfox",
            "Midori": "Midori.Midori",
            "Pale Moon": "M.C.PaleMoon",
            "Falkon": "Falkon.Falkon",
            "Slimjet": "FlashPeak.Slimjet",
            #Essenciais
            "WinRAR": "RARLab.WinRAR",
            "VLC Media Player": "VideoLAN.VLC",
            "7-Zip": "7zip.7zip",
            "PotPlayer": "Daum.PotPlayer",
            "MPC-HC (Media Player Classic)": "MPC-HC.MediaPlayerClassic",
            "Spotify": "Spotify.Spotify",
            "MalwareBytes": "Malwarebytes.Malwarebytes",
            "BitWarden": "8bit.Bitwarden",
            #Utilitarios
            "NVIDIA": "NVIDIA.NVIDIAControlPanel",
            "CPU-Z": "CPUID.CPUZ",
            "FanControl": "FanControl.FanControl",
            "CPUID HWMonitor": "CPUID.HWMonitor",
            "CCleaner": "Piriform.CCleaner",
            "Revo Uninstaller": "Revo.Uninstaller",
            "Autoruns": "Sysinternals.Autoruns",
            "Visual Studio Code": "Microsoft.VisualStudioCode",
            "Notepad++": "NotepadPlusPlus.NotepadPlusPlus",
            "Deluge Torrent": "Deluge.Deluge",
            #Jogos
            "Steam": "Valve.Steam",
            "Ubisoft": "Ubisoft.UBISOFTCONNECT",
            "EA": "ElectronicArts.Origin",
            "Battle.net": "Blizzard.BattleNet",
            "Epic Games": "EpicGames.EpicGamesLauncher",
            "CurseForge": "CurseLLC.CurseForge",
            }
        self.adicionar_softwares()                                  #CHAMA A FUNÇÃO PARA ADD SOFTWARES
        self.checkbox_lista()                                       #VERIFICA A LISTA SELECIONADO
        self.ui.button_install.clicked.connect(self.executarInst)   #BUTAO CLICKADO CHAMA FUN self.executarInst
    

############################################################
    def adicionar_softwares(self):
        #PREENCHER AS LISTAS COM SOFTWARES
        softwares = {
                self.ui.list_browsers: ["Google Chrome", "Brave", "Firefox", "Opera", "Tor", "Vivaldi Browser", "Microsoft Edge", "LibreWolf", "Ungoogled Chromium", "Waterfox", "Midori", "Pale Moon", "Falkon", "Slimjet", "Otter Browser"],    #Lista de browsers
                self.ui.list_essen: ["WinRAR", "7-Zip", "VLC Media Player", "PotPlayer", "MPC-HC (Media Player Classic)", "Spotify", "MalwareBytes", "BitWarden"],                                             #Lista de essenciais
                self.ui.list_utilita: ["CPU-Z", "FanControl", "CPUID HWMonitor", "CCleaner", "Revo Uninstaller", "Autoruns", "Visual Studio Code", "Notepad++", "Deluge Torent", "Nvidia"],                                   #Lista de utilitarios
                self.ui.list_jogos: ["Steam", "Ubisoft", "EA", "Battle.net", "Epic Games", "CurseForge"],           #Lista de jogos e ou launchers
            }

        for lista, itens in softwares.items():                  #Percorre cada Qlist e a lista de softwares
            for software in itens:                              #Percorre cada item na lista 
                item = QListWidgetItem(software)                #Cria item na lista
                item.setCheckState(Qt.CheckState.Unchecked)     #Cria Checkbox desmarcado
                lista.addItem(item)                             #Adicina item na lista

        """ Comentarios coomo funciona esta func
        for lista, itens in softwares.items():
        softwares.items() retorna pares chave-valor de um dicionário onde:
        A chave (lista) é um QListWidget (ex: self.ui.list_browsers).
        O valor (itens) é uma lista de softwares (ex: ["Google Chrome", "Firefox", "Brave"]).
        O loop percorre cada QListWidget e a sua lista de softwares associada.

        for software in itens:
        Agora percorremos os softwares dentro da lista atual.
        Exemplo: Se estivermos na list_browsers, itens será ["Google Chrome", "Brave", "Firefox", ...].
        O loop vai iterar sobre cada software individualmente.

        item = QListWidgetItem(software)
        Para cada software, cria um item na lista com o seu nome.
        Se o software for "Google Chrome", o item criado terá esse nome.

        item.setCheckState(Qt.CheckState.Unchecked)
        Adiciona um checkbox ao lado do nome do software.
        O checkbox começa desmarcado.

        lista.addItem(item)
        Adiciona o item à QListWidget correspondente.
        Se estivermos na list_browsers, o software vai aparecer dentro dessa lista.
        source chat gpt 4.0
        """

    def checkbox_lista(self):
        softwares_para_instalar = []                #Lista para armazenar os softwares marcados

        for lista in [self.ui.list_browsers, self.ui.list_essen, self.ui.list_jogos, self.ui.list_utilita]:
            for i in range (lista.count()):                         # Percorrer cada item dentro da lista
                item = lista.item(i)
                if item.checkState() == Qt.CheckState.Checked:      # Se o checkbox estiver marcado
                    softwares_para_instalar.append(item.text())     # Adicionar o nome do software à lista

        return softwares_para_instalar                              # Devolve a lista de selecionados
    
    def executarInst(self):
        softwares_para_instalar = self.checkbox_lista()

        total_softwares = len(softwares_para_instalar)
        softwares_instalados = 0
        self.ui.progressBar.setValue(0)

        if not softwares_para_instalar:                                 #Se user nao selecionar nenhum software
            self.ui.log.append("Nao tem nenhum software selecionado")   #Imprime console log 
            self.ui.log.ensureCursorVisible()
            return 0
        

        for software in softwares_para_instalar:                        #Para cada software na lista

            if software in self.mapeamento_softwares:                   #Se o nome esta na lista de codigos de software
                comando = self.mapeamento_softwares[software]           #O comando toma o valor desse codigo
            else:                                                       #Se o nome do software ja for o comando
                comando = software                                      #O comando toma o valor do nome
        
            self.ui.log.append(f"A instalar {software}...")
            QApplication.processEvents()
            self.ui.log.ensureCursorVisible()

            resultado = subprocess.Popen(["powershell", "-Command", f"winget install --silent --accept-source-agreements --accept-package-agreements {comando}" ],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding="utf-8")
            
            for linha in resultado.stdout:

                linha = linha.strip()

                if linha in ["-", "\\", "|", "/"]:
                    continue                            #Ignora estes caracteres

                self.ui.log.append(linha)
                self.ui.log.ensureCursorVisible()       #Puxa o scroll para baixo
                QApplication.processEvents()            #Atualiza o log



            if resultado.returncode == 0:
                self.ui.log.append(f"{software} foi instalado com sucesso!")
                self.ui.log.ensureCursorVisible()
            elif resultado.returncode == 1:
                self.ui.log.append(f"\n{software} não foi instalado!")
                self.ui.log.ensureCursorVisible()
            
            self.ui.log.ensureCursorVisible()

            softwares_instalados += 1
            progresso = int((softwares_instalados/total_softwares)*100)
            self.ui.progressBar.setValue(progresso)
            QApplication.processEvents()
#############################################################
    def abrir_sobre(self):
        if not self.Sobre:                                                  #Se a janela Sobre nao estiver aberta
            self.Sobre = Sobre()                                            #Cria a janela Sobre
        
        self.Sobre.ui.about_text.setText("PROGRAMA CRIADO POR ALVARO ALEXANDRE\nPYQT6/PYTHON E WINGET/PSHELL\n2025\n\nVer. 1.0")
        self.Sobre.show()                                                   #Mostra a janela Sobre

        self.Sobre.ui.button_sobre_ok.clicked.connect(self.Sobre.close)     #Botao OK fecha a janela
    
    
        


if __name__ == "__main__":
    app = QApplication([])
    window = InstaladorUtil()
    window.show()
    app.exec()


    