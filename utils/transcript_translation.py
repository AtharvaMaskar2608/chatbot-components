import requests
from typing import List, Dict
from dotenv import load_dotenv
import os
from googletrans import Translator


load_dotenv()

def translate_to_english(transcripts: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Description:
        - This function accepts the generated transcripts in hindi and returns english transcripts
    
    parameters:
        - transcript (list) - List of dirs of formatted transcript
        {
            speaker: speakerName, 
            text: text
        }

    returns: 
        - translated transcripts (list):
        {
            speaker: speakerNamer, 
            text: translated_text
        }
    """

    translator = Translator()
    translated_transcripts = []

    for transcript in transcripts:
        translation = translator.translate(transcript.text, src='hi', dest='eng')
        translated_transcripts.append({
            "speaker": transcript.speaker, 
            "translated_text": translation
        })

    return translated_transcripts