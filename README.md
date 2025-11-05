# 🚀 MAV - Mini Assistente Virtual

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

O **MAV** é um **Mini Assistente Virtual** em Python, controlado por voz e com interface gráfica, capaz de entender comandos em português, executá-los e responder ao usuário.  
Ideal para automatizar tarefas simples, consultas rápidas e anotações pessoais.

---

## 🛠 Funcionalidades Principais

O MAV pode realizar uma variedade de tarefas:

### 💡 Consultas
- Informar as horas (`"Que horas são?"`)
- Pesquisar na Wikipedia (`"Pesquise na Wikipedia sobre..."`)
- Verificar o clima de uma cidade (`"Qual o clima em..."`)
- Pesquisar no Google (`"Pesquisar..."`)

### 🖥 Ações no Sistema
- Abrir navegador e editor de texto
- Obter informações detalhadas do sistema (CPU, RAM, disco)
- Tirar screenshots
- Ajustar volume do sistema

### 📝 Produtividade
- Fazer anotações (`"Anote para mim..."`)
- Ler anotações salvas (`"Ler minhas anotações"`)

### 🧠 Memória
- Lembrar informações pessoais (nome, idade, cidade)
- Listar informações memorizadas
- Limpar memória

### 😄 Personalidade
- Contar piadas
- Ajustar parâmetros da própria voz (velocidade e volume)
- Responder saudações (Bom dia, Boa tarde, Boa noite)
- Apresentar os criadores


## 💻 Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias principais:

* **Python 3:** Linguagem base do projeto.
* **Tkinter:** Para a construção da interface gráfica (GUI).
* **SpeechRecognition:** Para o reconhecimento de voz (Speech-to-Text).
* **gTTS (Google Text-to-Speech):** Para a síntese de voz (Text-to-Speech).
* **Pydub:** Para manipulação e reprodução dos áudios gerados.
* **Wikipedia:** Para realizar buscas diretas na enciclopédia. 
* **Requests:** Para consultas de API (como a de clima). 
* **psutil, py-cpuinfo, pyautogui, keyboard:** Para controle e obtenção de informações do sistema operacional (RAM, CPU, disco, volume, screenshots). 

## 🛠️ Instalação e Configuração

Para executar o MAV em sua máquina local, siga estes passos:

### Pré-requisitos

* Python 3.x
* Um microfone funcional e configurado no seu sistema.
* **FFmpeg:** Essencial para a biblioteca `pydub` (usada em `voz.py`) conseguir processar os arquivos de áudio MP3.
    * **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
    * **Windows/macOS:** Baixe do [site oficial do FFmpeg](https://ffmpeg.org/download.html) e adicione ao PATH do seu sistema.

### Instalação
```bash
git clone <https://github.com/GittCris/Projeto-Processamento-de-Voz>
cd <Projeto_ProcVoz>
pip install -r requirements.txt
```

**3. Como Executar:**
Após instalar todas as dependências, basta executar o arquivo principal mav.py:

```bash
python mav.py
```

## 📂 Estrutura de Arquivos

| Arquivo            | Descrição                                        |
|--------------------|--------------------------------------------------|
| `mav.py`           | Arquivo principal, controla GUI e loop de escuta |
| `comandos.py`      | Lógica de execução dos comandos                  |
| `voz.py`           | Módulo TTS (gTTS + Pydub)                        |
| `escuta.py`        | Módulo STT (SpeechRecognition)                   |
| `memoria.py`       | Controla memória (`memoria.json`)                |
| `memoria.json`     | Armazena informações memorizadas                 |
| `notas.txt`        | Arquivo de anotações (criado automaticamente)    |
| `requirements.txt` | Lista de dependências                            |


## 👨‍💻 Autores

- Cristian de Andrade
- Mikaela Rikberg

Desenvolvido para a matéria "Processamento de Voz" com o professor Fernando Gil
