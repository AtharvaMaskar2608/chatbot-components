from openai import OpenAI

client = OpenAI()

def check_greeting(transcript: str) -> bool:
    """
    Description: This function checks if the agent has greeted the client

    parameter:
        - transcript (str): Transcript in the text format
    
    returns:
        - didGreet (bool): Returns true if the agent has greeted, returns false if the agent hasn't greeted. 
    """


    system_prompt = f"You are a hindi sales call analyzer. Your job is to ensure that the agent that picks up the call is following his tasks well. You will be given a transcript, you have to tell if the agent has greeted the client. Eg: Hello sir, good morning/evening/afternoon sir. If he does return 1 else he doesnt return 0. Only return 0 ir 1 without any other sentences"

    user_prompt = f"{transcript} did user greet? Just return 1 if he does, 0 if he doesn't"


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return int(completion.choices[0].message.content)


def check_empathy(transcript: str) -> int:
    """
    Description:
        - This function checks if the agent was empathetic towards the client. 
    parameter:
        - transcript (str): call transcript
    returns:
        - emapthy_score (int): Empathy score on a scale of 0 - 2. 0 - Not empathetic, 1 - Neutral, 2 - Empathetic
    """

    system_prompt = "You are a professional HINDI sales call analyzer. Your job is to ensure that the agent that calls is empathetic towards the client. You will be given a hindi transcript and have to mark the agent on a scale of 0 - 2. If the agent uses bad words or demeans the client or is being mean even once then straight up give 0. 0 - Agent was not empathetic at all, 1 - Agent was neutral, 2 - Agent was empathetic. Only reply in 0, 1 or 2"

    user_prompt = f"{transcript}, check how empathetic the agent was towards the client on a scale of 0 to 2"


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return int(completion.choices[0].message.content)

def check_closure(transcript: str) -> int:
    """
    Description: This function checks if the agent gave a proper closure to the client during the call. 

    parameters: 
        - tranascript (str): Call transcript

    returns: 
        - closure_score (int): Returns 0 if the agent did not give a proper closure, and returns 1 if he gave a closure.         
    """

    system_prompt = """You are a professional HINDI sales call analyzer. Your job is to make sure that the agent wished the client well before ending the call. 
    Eg:  Can I assist you with anything else? Thank you sir have a nice day? Is there anything you need help with? etc. 
    You will be given a hindi transcript and have to return 1 if the agent did the closure well and return 0 if the agent did not say anything in the closure. Only reply in 1 and 0 nothing else."""

    user_prompt = f"{transcript}. for the given transcript return 0 if the agent didnot do a closure before the end of the call. Return 1 if he did,"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return int(completion.choices[0].message.content)