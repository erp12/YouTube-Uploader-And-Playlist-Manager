'''
Created on May 8, 2014

@author: Eddie
'''
import YT_Uploader_Playlist_Manager.YTapiManager.httplib2 as httplib2
import os
import sys
import shutil

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

def yt_auth(is_new_login):
    CLIENT_SECRETS_FILE = "client_secrets.json"

    # This variable defines a message to display if the CLIENT_SECRETS_FILE is
    # missing.
    MISSING_CLIENT_SECRETS_MESSAGE = """
    WARNING: Please configure OAuth 2.0

    To make this sample run you will need to populate the client_secrets.json file
    found at:

    %s

    with information from the {{ Cloud Console }}
    {{ https://cloud.google.com/console }}

    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       CLIENT_SECRETS_FILE))
    # This OAuth 2.0 access scope allows for read-only access to the authenticated
    # user's account, but not other types of account access.
    YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE,
                                   scope=YOUTUBE_READONLY_SCOPE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid or is_new_login:
        flags = argparser.parse_args()
        credentials = run_flow(flow, storage, flags)

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    http=credentials.authorize(httplib2.Http()))
    
    shutil.copy(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+'\YTapiManager\client_secrets.json', os.path.abspath(os.path.join(os.getcwd(), os.pardir))+'\YTUGUI')
    
    return youtube

def create_new_playlists(youtube):
    # This code creates a new, private playlist in the authorized user's channel.
    playlists_insert_response = youtube.playlists().insert(
      part="snippet,status",
      body=dict(
        snippet=dict(
          title="Eddie's Test Playlist",
          description="A private playlist created with the YouTube API v3"
        ),
        status=dict(
          privacyStatus="public"
        )
      )
    ).execute()
    
def list_my_playlists(youtube):
    list_of_playlists = []
    
    channels_response = youtube.channels().list(mine=True, part='contentDetails').execute()
    
    for channel in channels_response['items']:
        playlists_list_request = youtube.playlists().list(part='snippet', mine=True)
        
        while playlists_list_request:
            playlist_list_response = playlists_list_request.execute()
            for playlist in playlist_list_response['items']:
                #print playlist['snippet']['title']
                list_of_playlists.append(playlist['snippet']['title'])
        
            playlists_list_request = youtube.playlistItems().list_next(playlists_list_request,
                                                                       playlist_list_response)
    return list_of_playlists


'''    
def NOlist_my_playlists(youtube):
    channels_response = youtube.channels().list(mine=True,
                                                part="contentDetails").execute()
    for channel in channels_response["items"]:
        # From the API response, extract the playlist ID that identifies the list
        # of videos uploaded to the authenticated user's channel.
        uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]

        print "Videos in list %s" % uploads_list_id

        # Retrieve the list of videos uploaded to the authenticated user's channel.
        playlistitems_list_request = youtube.playlistItems().list(playlistId=uploads_list_id,
                                                                  part="snippet",
                                                                  maxResults=50)
    
    while playlistitems_list_request:
        playlistitems_list_response = playlistitems_list_request.execute()

        # Print information about each video.
        for playlist_item in playlistitems_list_response["items"]:
            title = playlist_item["snippet"]["title"]
            video_id = playlist_item["snippet"]["resourceId"]["videoId"]
            print "%s (%s)" % (title, video_id)

        playlistitems_list_request = youtube.playlistItems().list_next(playlistitems_list_request,
                                                                       playlistitems_list_response)
'''


#yt = yt_auth(True)
#list_my_playlists(yt)
#create_new_playlists(yt)