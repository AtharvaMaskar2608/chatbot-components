from utils import *
import pandas as pd
import json
# /home/choice/Desktop/chatbot-components/audio_calls/2/2b2719b9-9a98-4c04-80f1-2a97c917ad84.mp3
import os 


def main(audio_file_url: str, agentName: str):
    print(audio_file_url)
    audio_file_url = f"/home/choice/Desktop/chatbot-components/audio_calls/2/{audio_file_url}.mp3"


    transcripts = transcribe_audio(audio_file_url)

    # translated_transcripts = translate_to_english(transcripts=translate_to_english)

    audio_transcripts = ""

    for transcript in transcripts:
        audio_transcripts += f"Speaker {transcript.speaker}: {transcript.text}\n"

    audio_transcripts = preprocess_speaker_transcript(audio_transcripts, agentName)

    summary = generate_sumary(transcript=audio_transcripts, agentName=agentName)
    print(f"Summary: {summary}")

    print(audio_transcripts)
    didGreet = check_greeting(transcript=audio_transcripts, summary=summary)
    print(f"Greeting: {didGreet}")
    

    empathy_score = check_empathy(transcript=audio_transcripts, summary=summary)
    print("Empathy Score: ", empathy_score)

    closure_score = check_closure(transcript=audio_transcripts, summary=summary)
    print(f"Closure: {closure_score}")

    query = get_query_type(transcript=audio_transcripts)
    print(f"Query Type: {query}")


    data = {
        "Call URL": audio_file_url,
        "Transcript": [audio_transcripts],
        "Caller Name": agentName,
        "Query Type": query,  
        "Greetings": [didGreet], 
        "Empathy": [empathy_score], 
        "Closure": [closure_score], 
        "Summary": [summary]    
    }

    return data

if __name__ == "__main__":

    df = pd.DataFrame(columns=['Call URL', 'Transcript', 'Caller Name', 'Query Type', "Greetings", "Empathy", "Closure", "Summary"])

    data = []
    with open("calls.json", 'r') as callsFile:
        data = json.load(callsFile)

    # data = []

    # folder_path = "/home/choice/Desktop/chatbot-components/audio_calls/0"

    # for root, dirs, files in os.walk(folder_path):
    #     for file in files:
    #         data.append(file[:-4])

    for call in data:
        calls_url = call['calls']
        agentName = call['caller_name']
        row = main(audio_file_url=calls_url, agentName=agentName)

        df = pd.concat([df, pd.DataFrame(row)], ignore_index=True)

    df.to_csv('calls.csv', index=False)