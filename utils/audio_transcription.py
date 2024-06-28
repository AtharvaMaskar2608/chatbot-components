from typing import List, Dict
import os

# Importing Assembly AI libraries 
import assemblyai as aai

from dotenv import load_dotenv

load_dotenv()


def transcribe_audio(audio_file_path: str) -> List[Dict[str, str]]:
    """
    Description:
        - This function uses the assembly AI API to take an audio file and transcribe it. 

    parameters:
        - audio_file_path (str): path of the audio file 
    
    returns:
        - transcripts (arr): Array of dictionary of transcripts
    """

    # Setting assembly ai api key 
    aai.settings.api_key = os.getenv('ASSEMBLY_AI_API_KEY')

    # Initializing transcriber
    transcriber = aai.Transcriber()

    # Config 
    config = aai.TranscriptionConfig(speaker_labels=True, language_code='hi', punctuate=True, speakers_expected=2)

    # Transcribing audio 
    transcript = transcriber.transcribe(audio_file_path, config)

    audio_transcript = []

    for utterence in transcript.utterances:
        audio_transcript.append({
            "speaker": utterence.speaker, 
            "text": utterence.text
        })

    return audio_transcript

