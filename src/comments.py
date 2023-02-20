import googleapiclient.discovery


def request(video_id, api_key, next_page_token):
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)
    yt_request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        pageToken=next_page_token,
        maxResults=1
    )
    response = yt_request.execute()
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
