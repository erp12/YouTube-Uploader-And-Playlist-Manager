'''
Created on May 8, 2014

@author: Eddie
'''
import os

import YTconfigManager

def setup_playlist(playlist_name):
    if ( os.path.isdir( os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name) ):
        return
    else:
        os.mkdir( os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name)
        YTconfigManager.make_playlist_config(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name)
        
def get_videos_in_playlist(playlist_name):
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name
    onlyfiles = [ f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
    list_of_videos = []
    for f in onlyfiles:
        if f != 'MetaDataFile.cfg':
            list_of_videos.append(f)
    return list_of_videos