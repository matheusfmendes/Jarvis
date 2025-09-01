# Jarvis Assistant

Um assistente de voz simples em Python integrado ao ChatGPT.

## 🚀 Funcionalidades
- Reconhecimento de voz (Google STT via SpeechRecognition)
- Resposta em voz (pyttsx3 TTS)
- Integração com ChatGPT

## 📦 Instalação

1. Clone este repositório ou extraia o `.zip`.
2. Crie um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Uso

1. Substitua `SUA_API_KEY_AQUI` pela sua chave da API da OpenAI em `main.py`.
2. Execute:
   ```bash
   python main.py
   ```
3. Fale com o Jarvis! Para encerrar, diga **"sair"**.

---

## 🔮 Melhorias Futuras
- TTS mais natural (ElevenLabs, Edge TTS)
- STT offline (Vosk)
- Detecção de palavra-chave (Porcupine)
- Interface gráfica (Flask + Web)
- Streaming (responder enquanto pensa)
