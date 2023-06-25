import os
import re
import googleapiclient.discovery

def extract_time_comments(comments):
    time_comments = []
    pattern = r'\d{2}:\d{2}'  # Regular expression pattern to match time codes in the format "MM:SS"

    for comment in comments:
        match = re.search(pattern, comment)
        if match:
            time_comments.append(comment)

    return time_comments

def main():
    # Set up the YouTube Data API v3
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "YOUR_API_KEY"

    # Prompt the user to enter a YouTube video link
    video_link = input("Enter the YouTube video link: ")

    # Extract the video ID from the link
    video_id = re.search(r"v=([^#\&\?]+)", video_link)
    if video_id:
        video_id = video_id.group(1)
    else:
        print("Invalid YouTube video link.")
        return

    # Create a YouTube API client
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    try:
        # Retrieve video comments using the YouTube API
        video_comments = []
        next_page_token = None

        while True:
            response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=next_page_token,
                maxResults=100
            ).execute()

            for item in response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
                video_comments.append(comment)

            if "nextPageToken" in response:
                next_page_token = response["nextPageToken"]
            else:
                break

        time_comments = extract_time_comments(video_comments)
        if time_comments:
            for comment in time_comments:
                print(comment)
        else:
            print("No comments with time codes found.")

    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e)

    except Exception as ex:
        print("An exception occurred:", ex)

if __name__ == "__main__":
    main()
