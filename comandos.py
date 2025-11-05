import datetime
import wikipedia
import requests
import webbrowser
import os
import platform
import subprocess
import re
from voz import falar
from memoria import *
from random import choice
import time
import psutil
import pyautogui
from cpuinfo import get_cpu_info

piadas = [
    "Por que o livro de matemática se suicidou? Porque tinha muitos problemas.",
    "Qual é o animal mais antigo? A zebra, porque está em preto e branco.",
    "Por que o computador foi ao médico? Porque pegou um vírus!",
    "Como o oceano se despede da praia? Ele dá um 'tchau-mar'.",
    "Por que o lápis se sentiu mal? Porque estava sem ponta.",
    "Qual é o cúmulo da velocidade? Fechar a porta e pegar o dedo.",
    "O que a vaca disse para o boi? 'Te vejo no pasto!'",
    "Por que o tomate não entrou na briga? Porque ele não queria se meter em molho.",
    "Qual é a fruta mais divertida? A banana, porque ela ri de si mesma.",
    "Por que a bicicleta não consegue ficar de pé sozinha? Porque ela é dois-ciclos."
]


# Configurações de voz globais
voz_config = {
    "volume_db": 0,      # volume relativo, em decibéis
    "velocidade": 1.0    # 1.0 = normal, >1 = mais rápido, <1 = mais lento
}

# -----------------------------
# PIADAS
# -----------------------------
def comando_piada(log_func=None):
    texto = choice(piadas)
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

# -----------------------------
# HORAS
# -----------------------------
def comando_horas(log_func=None):
    hora = datetime.datetime.now().strftime("%H:%M")
    texto = f"Agora são {hora}."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

# -----------------------------
# WIKIPEDIA
# -----------------------------
def comando_wikipedia(termo: str, log_func=None):
    try:
        wikipedia.set_lang("pt")
        resumo = wikipedia.summary(termo, sentences=2)
        if log_func:
            log_func(f"MAV: Buscando Wikipedia: {termo}")
            log_func(f"MAV: {resumo}")
        falar(resumo, **voz_config)
    except wikipedia.exceptions.DisambiguationError:
        texto = "O termo é ambíguo. Tente ser mais específico."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
    except wikipedia.exceptions.PageError:
        texto = "Não encontrei essa informação na Wikipedia."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
    except Exception:
        texto = "Ocorreu um erro ao buscar na Wikipedia."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)

# -----------------------------
# EDITOR DE TEXTO
# -----------------------------
def abrir_editor(log_func=None):
    sistema = platform.system()
    if log_func:
        log_func("MAV: Abrindo editor de texto...")
    if sistema == "Windows":
        try:
            os.startfile("notepad.exe")
        except:
            texto = "Erro ao abrir o Notepad."
            if log_func:
                log_func(f"MAV: {texto}")
            falar(texto, **voz_config)
    elif sistema == "Linux":
        for editor in ["gedit", "kate", "xed", "pluma", "leafpad", "mousepad", "nano"]:
            try:
                subprocess.Popen([editor])
                return
            except FileNotFoundError:
                continue
        texto = "Nenhum editor gráfico encontrado. Tentando o nano no terminal..."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
        os.system("nano")
    elif sistema == "Darwin":  # macOS
        try:
            subprocess.Popen(["open", "-a", "TextEdit"])
        except:
            texto = "Erro ao abrir o TextEdit."
            if log_func:
                log_func(f"MAV: {texto}")
            falar(texto, **voz_config)
    else:
        texto = "Sistema operacional desconhecido."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)

# -----------------------------
# CLIMA
# -----------------------------
def comando_clima(cidade: str, log_func=None):
    try:
        res = requests.get(f"https://wttr.in/{cidade}?format=3")
        texto = f"O clima em {res.text}"
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
    except Exception:
        texto = "Não consegui consultar o clima agora."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)

# -----------------------------
# NAVEGADOR
# -----------------------------
def comando_abrir_navegador(log_func=None):
    texto = "Abrindo navegador..."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)
    webbrowser.open("https://www.google.com")

def comando_pesquisar(termo: str, log_func=None):
    if termo:
        texto = f"Pesquisando por {termo} no Google..."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
        webbrowser.open(f"https://www.google.com/search?q={termo}")
    else:
        texto = "Por favor, diga o que deseja pesquisar."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)

# -----------------------------
# ANOTAÇÕES
# -----------------------------
def comando_anotar(comando: str, log_func=None):
    with open("notas.txt", "a", encoding="utf-8") as f:
        f.write(comando + "\n")
    texto = f"Anotado: {comando}"
    if log_func:
        log_func(f"MAV: {texto}")
    falar("Anotado!", **voz_config)

def comando_ler_anotacoes(log_func=None):
    try:
        with open("notas.txt", "r", encoding="utf-8") as f:
            notas = f.readlines()
        if notas:
            if log_func:
                log_func("MAV: Lendo suas anotações")
            falar("Suas anotações são:", **voz_config)
            for nota in notas:
                if log_func:
                    log_func(f"MAV: {nota.strip()}")
                falar(nota.strip(), **voz_config)
        else:
            texto = "Você não tem anotações."
            if log_func:
                log_func(f"MAV: {texto}")
            falar(texto, **voz_config)
    except FileNotFoundError:
        texto = "Você não tem anotações."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)


# -----------------------------
# MEMÓRIA INTELIGENTE
# -----------------------------
def comando_lembra_que(frase: str, log_func=None):
    if not frase:
        texto = "Desculpe, não entendi o que devo lembrar."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto)
        return

    info = extrair_info(frase)  # captura nome, idade, cidade e profissão de uma vez

    # --- Nome ---
    if 'nome' in info:
        gravar_info("nome", info['nome'])
        texto = f"Entendi, então seu nome é {info['nome']}, certo?"
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto)

    # --- Idade ---
    if 'idade' in info:
        gravar_info("idade", info['idade'])
        texto = f"Ok, você tem {info['idade']} anos."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto)

    # --- Cidade ---
    if 'cidade' in info:
        gravar_info("cidade", info['cidade'])
        texto = f"Entendi, você mora em {info['cidade']}."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto)

    if 'profissao' in info:
        gravar_info("profissao", info['profissao'])
        texto = f"Beleza, você trabalha como {info['profissao']}."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto)

    # --- Profissão ou outros casos ---
    if not info:
        gravar_info("outro", frase)
        texto = "Ok, vou lembrar disso."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto)


def comando_o_que_lembra(log_func=None):
    respostas = formatar_lembrancas()
    if respostas:
        for frase in respostas:
            if log_func:
                log_func(f"MAV: {frase}")
            falar(frase, **voz_config)
    else:
        texto = "Ainda não tenho nenhuma lembrança registrada."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)

def comando_limpar_memoria(log_func=None):
    limpar_lembrancas()
    texto = "Todas as lembranças foram apagadas."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

# -----------------------------
# VOLUME MULTIPLATAFORMA
# -----------------------------
def aumentar_volume(valor=10, log_func=None):
    sistema = platform.system()
    if sistema == "Windows":
        try:
            import keyboard
            for _ in range(valor // 2):
                keyboard.send('volume up')
                time.sleep(0.05)
        except Exception as e:
            print("Erro no Windows:", e)
    elif sistema == "Linux":
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ +{valor}%")
    elif sistema == "Darwin":
        os.system(f"osascript -e 'set volume output volume ((output volume of (get volume settings)) + {valor})'")
    texto = "Volume aumentado."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def diminuir_volume(valor=10, log_func=None):
    sistema = platform.system()
    if sistema == "Windows":
        try:
            import keyboard
            for _ in range(valor // 2):
                keyboard.send('volume down')
                time.sleep(0.05)
        except Exception as e:
            print("Erro no Windows:", e)
    elif sistema == "Linux":
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ -{valor}%")
    elif sistema == "Darwin":
        os.system(f"osascript -e 'set volume output volume ((output volume of (get volume settings)) - {valor})'")
    texto = "Volume diminuído."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

# -----------------------------
# CONFIGURAÇÃO DE VOZ
# -----------------------------
def comando_voz(comando: str, log_func=None):
    match comando:
        case 1:
            voz_config["velocidade"] = min(voz_config["velocidade"] + 0.2, 3.0)
            texto = "Ok, vou falar mais rápido!"
        case 2:
            voz_config["velocidade"] = max(voz_config["velocidade"] - 0.2, 0.5)
            texto = "Ok, vou falar mais devagar..."
        case 3:
            voz_config["volume_db"] = min(voz_config["volume_db"] + 3, 20)
            texto = "Ok, vou falar mais alto!"
        case 4:
            voz_config["volume_db"] = max(voz_config["volume_db"] - 3, -20)
            texto = "Ok, vou falar mais baixo..."
        case _:
            texto = "Comando de voz desconhecido."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

# -----------------------------
# INFORMAÇÕES DO SISTEMA
# -----------------------------
def comando_info_sistema(log_func=None):
    try:
        sistema = platform.system()
        processador = get_cpu_info()
        memoria_total = round(psutil.virtual_memory().total / (1024 ** 3), 2)
        memoria_usada = round(psutil.virtual_memory().used / (1024 ** 3), 2)
        if "Windows" in sistema:
            disco_total = round(psutil.disk_usage('C:\\').total / (1024 ** 3), 2)
            disco_usado = round(psutil.disk_usage('C:\\').used / (1024 ** 3), 2)
        else:
            disco_total = round(psutil.disk_usage('/').total / (1024 ** 3), 2)
            disco_usado = round(psutil.disk_usage('/').used / (1024 ** 3), 2)
        info = (f"Sistema: {sistema}. "
                f"Processador: {processador['brand_raw']}. "
                f"Memória RAM: {memoria_usada} de {memoria_total} GigaBytes usada. "
                f"Disco: {disco_usado} de {disco_total} GigaBytes usado.")
        if log_func:
            log_func(f"MAV: {info}")
        falar(info, **voz_config)
    except Exception as e:
        texto = "Não consegui obter as informações do sistema."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
        print(e)

# -----------------------------
# CAPTURA DE TELA
# -----------------------------
def comando_captura_tela(log_func=None):
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        arquivo = f"screenshot_{now}.png"
        caminho = os.path.join(os.getcwd(), arquivo)
        screenshot = pyautogui.screenshot()
        screenshot.save(caminho)
        texto = f"Screenshot salva como {arquivo}."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
    except Exception as e:
        texto = "Não consegui capturar a tela."
        if log_func:
            log_func(f"MAV: {texto}")
        falar(texto, **voz_config)
        print(e)

# -----------------------------
# COMANDOS GERAIS
# -----------------------------
def ola(log_func=None):
    texto = "Olá! Como posso ajudar você hoje?"
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def bom_dia(log_func=None):
    texto = "Bom dia! Espero que você tenha um ótimo dia!"
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def boa_tarde(log_func=None):
    texto = "Boa tarde! Como está sendo o seu dia até agora?"
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def boa_noite(log_func=None):
    texto = "Boa noite! Espero que você tenha um descanso tranquilo."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def saudacao(log_func=None):
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        bom_dia(log_func=log_func)
    elif 12 <= hora_atual < 18:
        boa_tarde(log_func=log_func)
    else:
        boa_noite(log_func=log_func)

def criador(log_func=None):
    texto = "Fui criada por Cristian de Andrade e Mikaela Rikberg como parte de um projeto da matéria processamento de voz."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def nome_assistente(log_func=None):
    texto = "Meu nome é MAV, sua mini assistente virtual."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def procvoz(log_func=None):
    texto = "Me disseram que a matéria processamento de voz com o professor fernando gil é o melhor"
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def tchau(log_func=None):
    texto = "Tchau! Até logo!"
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)

def nao_entendo(log_func=None):
    texto = "Não entendi o comando."
    if log_func:
        log_func(f"MAV: {texto}")
    falar(texto, **voz_config)


