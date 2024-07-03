from transformers import pipeline

# Initialize the sentiment analysis pipeline
pipe = pipeline("text-classification", model="LondonStory/txlm-roberta-hindi-sentiment")

# Example text for sentiment analysis
text = "यह एक बहुत अच्छी फ़िल्म है।"

# Perform sentiment analysis
result = pipe(text)

# Interpret the sentiment analysis result
label = result[0]['label']  # e.g., 'positive', 'negative', 'neutral'
score = result[0]['score']  # confidence score

print(f"Sentiment: {label}, Score: {score}")
