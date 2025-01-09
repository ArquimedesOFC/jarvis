JARVIS 0.1

Descrição

JARVIS 0.1 é um projeto de estudo que explora diversas bibliotecas de fala em Python. Este projeto tem como objetivo demonstrar a utilização de ferramentas para reconhecimento de fala, manipulação de áudio e síntese de fala, oferecendo uma visão geral de suas funcionalidades e desempenho.

Bibliotecas Utilizadas

SpeechRecognition: Para reconhecimento de fala e transcrição de áudio em texto.

PyTTSx3: Para síntese de fala, convertendo texto em áudio.

Instalação

Certifique-se de ter o Python 3.x instalado. Em seguida, instale as dependências usando o comando abaixo:

pip install SpeechRecognition PyDub pyttsx3

Como Usar

Reconhecimento de Fala

Utilize a biblioteca SpeechRecognition para converter áudio em texto:

import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('audio_file.wav') as source:
    audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    print("Texto reconhecido:", text)

Síntese de Fala

Converta texto em fala com PyTTSx3:

import pyttsx3

engine = pyttsx3.init()
engine.say("Olá, este é um teste de síntese de fala.")
engine.runAndWait()

Conclusão

Este projeto oferece uma introdução prática às bibliotecas de fala em Python, demonstrando suas capacidades e usos práticos. JARVIS 0.1 é o resultado de estudos inicante de bibliotecas de fala

Contribuições

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas melhorias.
