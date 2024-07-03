from openai import OpenAI

client = OpenAI()

query_types = [
        {
            "query": "Account Query", 
            "description": "query regarding accounts"
        }, 
        {
            "query": "Technical", 
            "description": "Any technical issues the user is going through."
        }, 
        {
            "query": "Login Guidance", 
            "description": "Customer needs help logging in"   
        }, 
        {
            "query": "Account closure", 
            "description": "Queries regarding closing the account."   
        }, 
        {
            "query": "Franchise", 
            "description": "Queries regarding franchise."   
        }, 
        {
            "query": "Brokerage", 
            "description": "Queries regarding platform brokerage."   
        },        
        {
            "query": "Onboarding", 
            "description": "Queries regarding onboarding on the platform."   
        }, 
        {
            "query": "Fund settlement", 
            "description": "Queries regarding settlement of the funds."   
        }, 
        {
            "query": "Refer and earn", 
            "description": "Queries regarding the refer and earn scheme ."   
        }
]


def get_query_type(transcript: str) -> str:
    """
    Description:
        - This function takes the transcript and returns which query type it belongs to. 
    parameters: 
        - transcript (str): Transcript of the call
    returns:
        - query type        
    """
    
    system_prompt = f"""You are a professional hindi sales call analyzer. You will be given a hindi transcript, you have to classify the transcript into one of the following queries. Check the query name and it's description and return only the name of the query that describes the call. Do not return any justification or other text. {query_types}"""

    user_prompt = f"{transcript}. Classifiy the given transcript into a query type"

    completion = client.chat.completions.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return completion.choices[0].message.content
