import pyttsx3
import datetime
import speech_recognition as sr
import pause
import os
import random
import subprocess

# Inicializa o TTS globalmente para evitar reconfigurações repetitivas
engine = pyttsx3.init()
engine.setProperty("rate", 195)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id if voices else None)  # Ajusta para voz masculina

def falar(texto):
    """Converte texto em fala e exibe no console."""
    print(f"Assistente: {texto}")
    engine.say(texto)
    engine.runAndWait()

def obter_tempo():
    """Informa a hora atual."""
    hora_atual = datetime.datetime.now().strftime("%H:%M")
    falar(f"Agora são {hora_atual}")

def obter_data():
    """Informa a data atual de forma verbal."""
    agora = datetime.datetime.now()
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    falar(f"Hoje é dia {agora.day} de {meses[agora.month]} de {agora.year}.")

def saudacao():
    """Dá as boas-vindas com base no horário do dia."""
    hora = datetime.datetime.now().hour
    saudacao = "Bom dia" if hora < 12 else "Boa tarde" if hora < 18 else "Boa noite"
    falar(f"{saudacao}, senhor! Bem-vindo de volta!")

def ouvir_comando():
    """Escuta e reconhece comandos de voz."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language='pt-BR').lower()
            print(f"Você disse: {comando}")
            return comando
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError:
            falar("Erro na conexão. Tente novamente.")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None

def tocar_musica():
    """Toca uma música aleatória da pasta definida."""
    pasta_musicas = 'musicas/'
    if not os.path.isdir(pasta_musicas):
        falar("A pasta de músicas não foi encontrada.")
        return

    musicas = [musica for musica in os.listdir(pasta_musicas) if musica.endswith(('.mp3', '.wav', '.ogg'))]
    if not musicas:
        falar("Não há músicas disponíveis.")
        return

    musica = random.choice(musicas)
    caminho_completo = os.path.join(pasta_musicas, musica)
    
    try:
        subprocess.Popen(['start', caminho_completo], shell=True)
       
