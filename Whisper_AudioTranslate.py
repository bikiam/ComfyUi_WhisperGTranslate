# whisper_translate_node.py

import os
import uuid
import whisper
from googletrans import Translator
import torchaudio
import tempfile
import folder_paths
import numpy as np
import soundfile as sf  # pip install soundfile

class WhisperAudioTranslateNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO", ),
                "source_language": ("STRING", {
                    "default": "en"
                }),
                "target_language": ("STRING", {
                    "default": ""
                }),
                "whisper_model_size": (["tiny", "base", "small", "medium", "large"], {
                    "default": "small"
                })
            }
        }

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("Transcription/Translation", )
    FUNCTION = "transcribe_and_translate"
    CATEGORY = "WhisperAudioTranslate"

    def __init__(self):
        self.translator = Translator()

    def transcribe_and_translate(self, audio, source_language, target_language, whisper_model_size):
       
        temp_dir = folder_paths.get_temp_directory()
        os.makedirs(temp_dir, exist_ok=True)
        audio_save_path = os.path.join(temp_dir, f"{uuid.uuid1()}.wav")
        torchaudio.save(audio_save_path, audio['waveform'].squeeze(
            0), audio["sample_rate"])
      
        print(f"[Whisper Node] Transcribing temporary .wav file: {audio_save_path}")
        print("[Whisper Node] Loading Whisper model...")
        model = whisper.load_model(whisper_model_size)
        result = model.transcribe(audio_save_path, language=source_language)

        text = result["text"]
        print(f"[WhisperAudioTranslateNode] Transcription: {text}")

        # Remove temp file
        os.remove(audio_save_path)

        # Translate if needed
        if target_language and target_language != source_language:
            translated = self.translator.translate(text, dest=target_language)
            return (translated.text,)
        else:
            return (text,)
