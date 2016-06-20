#!/usr/bin/python

import argparse
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
#sudo pip install --upgrade google-api-python-client
DEVELOPER_KEY = "<key>"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(video_ids):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  
  #video_ids = "jv8MsZyHZ4U,2abnx5lyezU"

  # Call the videos.list method to retrieve location details for each video.
  video_response = youtube.videos().list(
    id=video_ids,
    part='snippet, statistics'
  ).execute()

  videos = []

  # Add each result to the list, and then display the list of matching videos.
  for video_result in video_response.get("items", []):
    videos.append("%s, %s, (%s)" % (video_result["id"],
			      video_result["snippet"]["title"],
			      video_result["statistics"]["viewCount"]))

  print "Videos:\n", "\n".join(videos), "\n"


if __name__ == "__main__":

  #argparser.add_argument("--q", help="Search term", default="capbeast")
  #argparser.add_argument("--max-results", help="Max results", default=25)
  #args = argparser.parse_args()

  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("video_ids", help="display view count of video ids", type=str)
    args = parser.parse_args()
  
    #youtube_search(args)
    youtube_search(sys.argv[1])
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

