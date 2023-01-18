import os

import googleapiclient.discovery


def request(video_id, api_key, nextPageToken):
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        pageToken=nextPageToken,
        maxResults=1
    )
    response = request.execute()
    return response


def list_comments(items, replies=True):
    comments = []
    for comment in items:
        comments.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])
        if replies:
            if comment['snippet']['totalReplyCount'] > 0:
                for reply in comment['replies']['comments']:
                    comments.append(reply['snippet']['textDisplay'])

    return comments


if __name__ == '__main__':

    # Set your API TOKEN
    api_key = os.getenv('API_KEY')
    video_id = os.getenv('VIDEO_ID')
    comments = []
    nextPageToken = None

    while True:
        response = request(video_id, api_key, nextPageToken)
        comments.append(list_comments(response['items']))
        if not response.get('nextPageToken'):
            break

        nextPageToken = response['nextPageToken']

    flatten_comments = [element for sublist in comments for element in sublist]
    print(flatten_comments)
