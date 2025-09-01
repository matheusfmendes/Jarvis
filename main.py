import speech_recognition as sr
import pyttsx3
import openai

# Configurar chave da API do ChatGPT
openai.api_key = "SUA_API_KEY_AQUI"

# Inicializar TTS
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {command}")
        return command
    except sr.UnknownValueError:
        return "Não entendi o que você disse."
    except sr.RequestError:
        return "Erro no reconhecimento de fala."

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    speak("Olá, eu sou o Jarvis. Como posso ajudar?")
    while True:
        command = listen().lower()
        if "sair" in command:
            speak("Até logo!")
            break
        response = chat_with_gpt(command)
        print("Jarvis:", response)
        speak(response)
