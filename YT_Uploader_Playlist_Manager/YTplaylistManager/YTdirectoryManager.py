'''
Created on May 8, 2014

@author: Eddie
'''
import os

def setup_playlist(playlist_name):
    if ( os.path.isdir( os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name) ):
        return
    else:
        os.mkdir( os.path.isdir( os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name) )
        
