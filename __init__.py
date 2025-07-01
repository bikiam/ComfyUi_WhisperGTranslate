from .Whisper_AudioTranslate import WhisperAudioTranslateNode
# Node registration
NODE_CLASS_MAPPINGS = {
    "WhisperAudioTranslateNode": WhisperAudioTranslateNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WhisperAudioTranslateNode": "Whisper + AudioTranslate"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
