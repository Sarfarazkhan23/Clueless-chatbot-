from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from groq import Groq
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from dotenv import load_dotenv
from transformers import pipeline
import torch, os, base64, uuid, tempfile, requests, random

# Setup
app = Flask(__name__)
CORS(app)
load_dotenv()

# API keys
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
eleven_labs = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")

# Load Whisper model
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=device)

# Fun, clueless response via LLaMA3
def get_funny_response(prompt):
    res
