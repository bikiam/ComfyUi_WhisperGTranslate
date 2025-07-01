# google_translate_node.py

from googletrans import Translator

class GoogleTranslateNode:
  
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "আমি ভালো আছি"
                }),
                "target_language": ("STRING", {
                    "default": "en"
                })
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Translated Text",)
    FUNCTION = "translate_text"
    CATEGORY = "WhisperAudioTranslate"

    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, target_language):
        if not text:
            return ("",)
        result = self.translator.translate(text, dest=target_language)
        return (result.text,)
