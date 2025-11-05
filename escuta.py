import speech_recognition as sr
from voz import falar

def ouvir(recognizer: sr.Recognizer, log_func=print) -> str:
    """
    Escuta a voz do usuário e retorna o texto reconhecido.
    """
    with sr.Microphone() as source:
        #print("Ouvindo...")
        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language='pt-BR').strip()
            if comando:
                return comando.lower()
            else:
                log_func("Silêncio detectado.")
                return None
            
        except sr.WaitTimeoutError:
            log_func("Nenhum som detectado dentro do tempo limite.")
            return None
            
        except sr.UnknownValueError:
            #print("Áudio não reconhecido ou ruído.")
            return None

        except sr.RequestError:
            falar("Erro na conexão. Verifique sua internet.")
            return None
