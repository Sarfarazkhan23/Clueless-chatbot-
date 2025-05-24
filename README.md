# 🧠 Silly AI Chatbot

A Flask-based web app that listens to your audio or text, responds with funny, overly sweet, and clueless replies using **LLaMA3**, converts the response to audio with **ElevenLabs**, and fetches a matching GIF using **GIPHY**.

## 🎯 Features

* 🤪 Silly & Clueless AI Replies (powered by Groq's LLaMA3)
* 🎤 Speech-to-Text transcription (via Whisper)
* 🔊 Text-to-Speech voice generation (via ElevenLabs)
* 🎬 GIF reaction generator (via GIPHY API)
* 🧠 Designed for fun interactions in a browser-based interface


## 📦 Tech Stack

* **Python** (Flask)
* **Groq API** (LLaMA3 for text generation)
* **ElevenLabs API** (TTS)
* **Whisper** (from Hugging Face Transformers)
* **GIPHY API** (for reaction GIFs)
* **Flask-CORS**, **dotenv**, **Torch**, **requests**, etc.

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/silly-chatbot.git
cd silly-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, install manually:

```bash
pip install flask flask-cors groq elevenlabs python-dotenv transformers torch requests
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key
GIPHY_API_KEY=your_giphy_api_key
```

---

## 🧪 Usage

### Run the server

```bash
python chatbottt.py
```

Then open your browser at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

### API Endpoints

#### `/silly` (POST)

Send a text prompt and get a funny response, a GIF URL, and an audio clip.

```json
{
  "text": "Why do cats hate water?"
}
```

Returns:

```json
{
  "response": "Oh my gosh, maybe they think it's spicy?? I'm not a cat expert but I'd try a raincoat next time. 🐱💦",
  "gif": "https://media.giphy.com/media/...",
  "audio": "<base64-encoded-mp3>"
}
```

#### `/transcribe` (POST)

Send an audio file (WAV format) and get its transcription.

---

## 🧠 Whisper Model

Using `openai/whisper-base` — supports English voice input and is loaded on GPU if available.

---

## 🔐 Security Note

Do **not** expose your API keys in production. Use proper secret management tools.

---

## 🤝 Credits

* [Groq](https://groq.com/)
* [ElevenLabs](https://www.elevenlabs.io/)
* [GIPHY](https://developers.giphy.com/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [OpenAI Whisper](https://github.com/openai/whisper)

---

## 🪄 License

MIT License — do whatever you want, just don't blame me if it becomes sentient.

---

Let me know if you'd like a `requirements.txt` file or want to deploy it online (e.g., on Render, Railway, or Replit).
