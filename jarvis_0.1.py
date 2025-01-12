import pyttsx3
import datetime
import speech_recognition as sr
import pause
import os
import random
import subprocess

# Inicializa o TTS
texto_fala = pyttsx3.init()
texto_fala.setProperty("rate", 195)  # Ajusta a velocidade da fala
voices = texto_fala.getProperty('voices')
texto_fala.setProperty('voice', voices[0].id)  # 0 = Masculina, 1 = Feminina

def falar(audio):
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    hora_atual = datetime.datetime.now().strftime("%I:%M")
    falar(f"Agora são, {hora_atual}")
    print(f"Hora: {hora_atual}")

def data():
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    agora = datetime.datetime.now()
    dia = agora.day
    mes = meses[agora.month - 1]
    ano = agora.year
    falar(f"Hoje é dia {dia} de {mes}, de {ano}!")
    print(f"Data: {dia} de {mes} de {ano}")

def bem_vindo():
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        saudacao = "Bom dia senhor! Bem vindo de volta!"
    elif 12 <= hora < 18:
        saudacao = "Boa tarde senhor! Bem vindo de volta!"
    else:
        saudacao = "Boa noite senhor! Bem vindo de volta!"
    falar(saudacao)

def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando sua fala...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Processando...")
            comando = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro na conexão: {e}")
            falar("Houve um problema na conexão. Por favor, tente novamente.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            falar("Desculpe, algo deu errado. Tente novamente.")
            return None

def tocar_musica():
    pasta_musicas = 'musicas/'  
    try:
        musicas = os.listdir(pasta_musicas)
        if musicas:
            musica = random.choice(musicas)
            caminho_completo = os.path.join(pasta_musicas, musica)
            subprocess.Popen(['start', caminho_completo], shell=True)
            falar(f"Tocando {musica}")
        else:
            falar("Não encontrei músicas na pasta.")
    except Exception as e:
        print(f"Erro ao tocar música: {e}")
        falar("Houve um problema ao tentar tocar a música.")

if __name__ == "__main__":
    bem_vindo()
    while True:
        print("Escutando...")
        comando = microfone()

        if comando is None:
            continue

        if 'jarvis' in comando:
            falar("Estou lhe ouvindo!")
            continue

        if 'como' in comando:
            falar("Estou bem! Obrigado por perguntar.")
            falar("O que posso fazer para ajudá-lo?")
        elif 'horas' in comando:
            tempo()
        elif 'data' in comando:
            data()
        elif 'volte' in comando:
            falar("Por quanto tempo devo esperar?")
            while True:
                resposta = microfone()
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
            falar("Desculpe, não entendi o comando. Pode repetir?")
