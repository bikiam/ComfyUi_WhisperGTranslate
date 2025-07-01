from .Whisper_AudioTranslate import WhisperAudioTranslateNode
from .Google_translate import GoogleTranslateNode
# Node registration
NODE_CLASS_MAPPINGS = {
    "WhisperAudioTranslateNode": WhisperAudioTranslateNode
    "GoogleTranslateNode": GoogleTranslateNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WhisperAudioTranslateNode": "Whisper + AudioTranslate"
    "GoogleTranslateNode": "Google Translate Node"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
