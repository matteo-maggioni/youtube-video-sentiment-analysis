import os

import pandas as pd

from src.comments import request, list_comments
from src.sentiment import calculate_sentiment

if __name__ == '__main__':

    # Set your API TOKEN
    api_key = os.getenv('API_KEY')
    video_id = os.getenv('VIDEO_ID')
    comments = []
    nextPageToken = None

    # recupero commenti
    while True:
        response = request(video_id, api_key, nextPageToken)
        comments.append(list_comments(response['items']))
        if not response.get('nextPageToken'):
            break

        nextPageToken = response['nextPageToken']

    flatten_comments = [element for sublist in comments for element in sublist]

    # sentiment
    comments_sentiment = calculate_sentiment(flatten_comments)

    # calcolo sentiment generale
    df_comments = pd.DataFrame(comments_sentiment, columns=['Comment', 'Sentiment'])
    video_sentiment = df_comments['Sentiment'].mode()[0]

    print(f"Il video ha un sentiment {video_sentiment}")
