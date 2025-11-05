from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def falar(texto, volume_db=0, velocidade=1.0, log_func=print):

    """
    Fala o texto.
    volume_db: aumento/redução em decibéis (+/-)
    velocidade: 1.0 = normal, >1 = mais rápido, <1 = mais lento
    """
    
    if not texto:
        return

    log_func(f"MAV: {texto}")
    try:
        nome_arquivo = "audio_temp.mp3"
        tts = gTTS(text=texto, lang="pt-br", slow=False)
        tts.save(nome_arquivo)

        som = AudioSegment.from_mp3(nome_arquivo)
        # Ajusta velocidade
        som = som._spawn(som.raw_data, overrides={
            "frame_rate": int(som.frame_rate * velocidade)
        }).set_frame_rate(som.frame_rate)

        # Ajusta volume
        som = som + volume_db

        play(som)
        os.remove(nome_arquivo)

    except Exception as e:
        log_func(f"Erro na síntese ou reprodução de voz: Não consigo captar seu áudio.")