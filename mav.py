import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from escuta import ouvir
from voz import falar
from comandos import *
import speech_recognition as sr

# -----------------------------
# Funções de integração MAV
# -----------------------------

def executar_comando(comando):
    comando = comando.lower()

    if any(p in comando for p in ['horas','hora','horario','horário']):
        comando_horas(log_func=log)

    elif any(p in comando for p in ['wikipedia','wikipédia']):
        termo = comando.replace("wikipedia", "").replace("wikipédia", "").strip()
        if termo:
            comando_wikipedia(termo, log_func=log)
        else:
            falar("Por favor, diga o que você quer buscar na Wikipedia.", log_func=log)

    elif "clima" in comando:
        frase = comando.replace("qual é o clima em","").replace("qual o clima em","").replace("como está o clima em","").replace("clima em","")
        cidade = comando.replace("clima", "").replace('no',"").replace('na','').replace('em','').strip()
        comando_clima(cidade, log_func=log)

    elif any(p in comando for p in ["abrir navegador","abrir o navegador","abra o navegador"]):
        comando_abrir_navegador(log_func=log)

    elif "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip()
        comando_pesquisar(termo, log_func=log)

    elif any(p in comando for p in ["abrir bloco de notas","abra o bloco de notas","abrir notepad","abra o notepad"]):
        abrir_editor(log_func=log)

    elif "piada" in comando:
        comando_piada(log_func=log)

    elif any(p in comando for p in ["o que você lembra","o que você se lembra", "o que você tem na memória"]):
        comando_o_que_lembra(log_func=log)

    elif "limpar memória" in comando:
        comando_limpar_memoria(log_func=log)

    elif any(p in comando for p in ["lembra que", "lembra de", "lembrar"]):
        comando_lembra_que(comando, log_func=log)

    elif any(p in comando for p in ["anota para mim", 'anotar','anota',]):
        texto_anotar = comando.replace("anota para mim","").replace("anotar","").replace("anota","").strip()
        comando_anotar(texto_anotar, log_func=log)

    elif any(p in comando for p in ['ler anotações','ler minhas anotações','ler minhas notas', 'leia a', 'agora leia']):
        comando_ler_anotacoes(log_func=log)

    elif any(p in comando for p in ["aumentar volume","aumenta o volume"]):
        aumentar_volume(10, log_func=log)

    elif any(p in comando for p in ["diminuir volume","diminuir volume"]):
        diminuir_volume(10, log_func=log)

    elif any(p in comando for p in ["fale mais rapido","aumenta a velocidade","voz mais rapido","fale mais rápido"]):
        comando_voz(1, log_func=log)

    elif any(p in comando for p in ["voz mais devagar","fale mais devagar","diminuir a velocidade"]):
        comando_voz(2, log_func=log)

    elif any(p in comando for p in ["fale mais alto"]):
        comando_voz(3, log_func=log)

    elif any(p in comando for p in ["fale mais baixo"]):
        comando_voz(4, log_func=log)

    elif any(p in comando for p in ["informações do sistema","info do sistema","informacao do sistema","informação do sistema", "sobre o sistema","detalhes do sistema"
                                    "informações sistema", "pc","info sistema","informacao sistema","informação sistema", "sobre sistema","detalhes sistema","computador"]):
        comando_info_sistema(log_func=log)

    elif any(p in comando for p in ["captura de tela","capturar tela","screenshot", "print da tela", 'print screen',"print", "printar"]):
        comando_captura_tela(log_func=log)

    elif any(p in comando for p in ["o que acha de processamento de voz"]):
        procvoz(log_func=log)

    elif any(p in comando for p in ["quem é seu criador","quem te criou", 'criador']):
        criador(log_func=log)

    elif any(p in comando for p in ["seu nome","qual seu nome","como você se chama", 'qual é o seu nome']):
        nome_assistente(log_func=log)

    elif any(p in comando for p in ["bom dia","boa tarde","boa noite"]):
        saudacao(log_func=log)
    
    elif any(p in comando for p in ["limpar", 'limpa']):
        limpar_log()

    elif any(p in comando for p in ["sair","tchau"]):
        tchau(log_func=log)
        root.quit()

    else:
        nao_entendo(log_func=log)

# -----------------------------
# Funções da interface
# -----------------------------

def log(texto):
    txt_log.configure(state='normal')
    txt_log.insert(tk.END, f"{texto}\n")
    txt_log.see(tk.END)
    txt_log.configure(state='disabled')

def enviar_texto():
    comando = entry_comando.get()
    entry_comando.delete(0, tk.END)
    if comando:
        log(f"Comando digitado: {comando}")
        executar_comando(comando)

def ouvir_continuo():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        log("Calibrando o microfone para o ruído ambiente, por favor aguarde...")
        r.adjust_for_ambient_noise(source)
        log("Microfone calibrado.")

    falar("Estou pronto para ouvir você.", log_func=log)

    while True:
        comando = ouvir(r, log_func=log)
        if not comando:
            continue
        log(f"Você disse: {comando}")
        executar_comando(comando)

def limpar_log():
    txt_log.configure(state='normal')
    txt_log.delete(1.0, tk.END)
    txt_log.configure(state='disabled')

# -----------------------------
# Interface Gráfica
# -----------------------------
root = tk.Tk()
root.title("MAV - Mini Assistente Virtual")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

# Entrada de comando
entry_comando = tk.Entry(root, font=("Helvetica", 14))
entry_comando.pack(pady=10, padx=10, fill='x')

btn_enviar = tk.Button(root, text="Enviar Comando", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=enviar_texto)
btn_enviar.pack(pady=5)

# Botões rápidos
frame_botoes = tk.Frame(root, bg="#1e1e1e")
frame_botoes.pack(pady=10)

botoes_info = [
    ("Horas", comando_horas),
    ("Info Sistema", comando_info_sistema),
    ("Captura Tela", comando_captura_tela),
    ("Limpar Logs", limpar_log),

]

for txt, cmd in botoes_info:
    btn = tk.Button(frame_botoes, text=txt, font=("Helvetica", 12), bg="#9C27B0", fg="white", width=12, command=cmd)
    btn.pack(side='left', padx=5)

# Log de ações
txt_log = scrolledtext.ScrolledText(root, state='disabled', bg="#2e2e2e", fg="white", font=("Helvetica", 12))
txt_log.pack(pady=10, padx=10, fill='both', expand=True)

# Inicia loop de escuta contínuo em thread
Thread(target=ouvir_continuo, daemon=True).start()

# Inicia interface
root.mainloop()
