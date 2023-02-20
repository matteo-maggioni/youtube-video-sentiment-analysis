import torch
from torch import nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def calculate_sentiment(comments):
    comments_sentiment = list()

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("neuraly/bert-base-italian-cased-sentiment")
    # Load the model
    model = AutoModelForSequenceClassification.from_pretrained("neuraly/bert-base-italian-cased-sentiment")

    for comment in comments:
        input_ids = tokenizer.encode(comment, add_special_tokens=True)

        # Create tensor
        tensor = torch.tensor(input_ids).long()
        # Fake batch dimension
        tensor = tensor.unsqueeze(0)

        # Call the model and get the logits
        logits, = model(tensor).logits

        # Remove the fake batch dimension
        logits = logits.squeeze(0)

        proba = nn.functional.softmax(logits, dim=0)

        # Unpack the tensor to obtain negative, neutral and positive probabilities
        negative, neutral, positive = [float(e) * 100 for e in proba]

        index_sentiment_max = [index for index, item in enumerate([negative, neutral, positive]) if item == max([negative, neutral, positive])][0]

        if index_sentiment_max == 0:
            sentiment = 'Negativo'
        elif index_sentiment_max == 1:
            sentiment = 'Neutro'
        else:
            sentiment = 'Positivo'

        comments_sentiment.append([comment, sentiment])

    return comments_sentiment
