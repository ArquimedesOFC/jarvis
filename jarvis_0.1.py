import pyttsx3
import datetime
import speech_recognition as sr
import pause
import os
import random
import subprocess

# Inicializa o TTS
def iniciar_tts():
    engine = pyttsx3.init()
    engine.setProperty("rate", 195)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id if voices else None)  # Ajusta para voz masculina
    return engine

tts = iniciar_tts()

def falar(texto):
    tts.say(texto)
    tts.runAndWait()

def obter_tempo():
    hora_atual = datetime.datetime.now().strftime("%H:%M")
    falar(f"Agora são {hora_atual}")
    print(f"Hora: {hora_atual}")

def obter_data():
    agora = datetime.datetime.now()
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    falar(f"Hoje é dia {agora.day} de {meses[agora.month]}, de {agora.year}.")
    print(f"Data: {agora.day} de {meses[agora.month]} de {agora.year}")

def saudacao():
    hora = datetime.datetime.now().hour
    saudacao = "Bom dia" if hora < 12 else "Boa tarde" if hora < 18 else "Boa noite"
    falar(f"{saudacao}, senhor! Bem-vindo de volta!")

def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando sua fala...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language='pt-BR').lower()
            print(f"Você disse: {comando}")
            return comando
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Erro na conexão. Tente novamente.")
            falar("Erro na conexão. Tente novamente.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            falar("Ocorreu um erro. Tente novamente.")
    return None

def tocar_musica():
    pasta_musicas = 'musicas/'
    if not os.path.isdir(pasta_musicas):
        falar("A pasta de músicas não foi encontrada.")
        return

    musicas = os.listdir(pasta_musicas)
    if not musicas:
        falar("Não há músicas disponíveis.")
        return

    musica = random.choice(musicas)
    caminho_completo = os.path.join(pasta_musicas, musica)
    try:
        subprocess.Popen(['start', caminho_completo], shell=True)
        falar(f"Tocando {musica}")
    except Exception as e:
        print(f"Erro ao tocar música: {e}")
        falar("Houve um problema ao tentar tocar a música.")

if __name__ == "__main__":
    saudacao()
    while True:
        comando = ouvir_comando()
        if not comando:
            continue

        if 'jarvis' in comando:
            falar("Estou lhe ouvindo!")

        elif 'como você está' in comando:
            falar("Estou bem! Obrigado por perguntar. Como posso ajudar?")

        elif 'horas' in comando:
            obter_tempo()

        elif 'data' in comando:
            obter_data()

        elif 'volte' in comando:
            falar("Por quanto tempo devo esperar?")
            while True:
                resposta = ouvir_comando()
                if resposta and resposta.isdigit():
                    segundos = int(resposta)
                    falar(f"Ok, voltarei em {segundos} segundos.")
                    pause.seconds(segundos)
                    falar("Estou de volta, senhor!")
                    break
                else:
                    falar("Por favor, diga um número válido.")

        elif 'tocar música' in comando:
            tocar_musica()

        elif 'obrigado' in comando:
            falar("Tudo bem! Se precisar, estou aqui!")
            break

        else:
            falar("Não entendi o comando. Pode repetir?")
