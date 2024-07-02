from utils import *
import pandas as pd



def main(audio_file_url):

    transcripts = transcribe_audio(audio_file_url)

    # translated_transcripts = translate_to_english(transcripts=translate_to_english)

    audio_transcripts = ""

    for transcript in transcripts:
        audio_transcripts += f"Speaker {transcript.speaker}: {transcript.text}\n"

    agentName = "Ambika"
    audio_transcripts = preprocess_speaker_transcript(audio_transcripts, agentName)

    with open("transcripts.txt", 'w') as file:
        file.write(audio_transcripts)




    print(audio_transcripts)
    didGreet = check_greeting(transcript=audio_transcripts)
    print(f"Greeting: {didGreet}")
    

    empathy_score = check_empathy(transcript=audio_transcripts)
    print("Empathy Score: ", empathy_score)

    closure_score = check_closure(transcript=audio_transcripts)
    print(f"Closure: {closure_score}")

    summary = generate_sumary(transcript=audio_transcripts, agentName=agentName)
    print(f"Summary: {summary}")


    data = {
        "Transcripts": [audio_transcripts],
        "Greeting Score": [didGreet], 
        "Empathy Score": [empathy_score], 
        "Closure Score": [closure_score], 
        "Summary": [summary]    
    }

    df =pd.DataFrame(data=data)

    df.to_csv('output.csv', index=True)

if __name__ == "__main__":

    audio_file_url = f"/home/choice/Desktop/chatbot-components/audio_files/very-bad.mp3"

    main(audio_file_url=audio_file_url)
