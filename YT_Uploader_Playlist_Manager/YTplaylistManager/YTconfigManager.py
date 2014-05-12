'''
Created on May 8, 2014

@author: Eddie
'''
import os
import ConfigParser

def make_playlist_config(path):
    config = ConfigParser.RawConfigParser()
    
    config.add_section('VideoData')
    config.set('VideoData', 'Title', 'Basic Title Goes Here')
    config.set('VideoData', 'Description', 'Video descriptions for all videos goes here')
    config.set('VideoData', 'Category', '22')
    config.set('VideoData', 'Keywords', 'Insert,Keywords,Here')
    config.set('VideoData', 'PrivacyStatus', 'private')
    
    with open(path + '\MetaDataFile.cfg', 'wb') as configfile:
        config.write(configfile)
        
def get_playlist_config_settings(playlist_name):
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name
    
    config = ConfigParser.ConfigParser()
    config.read(path+'\MetaDataFile.cfg')
    
    return [config.get('VideoData', 'Title'), config.get('VideoData', 'Description'), config.get('VideoData', 'Category'), config.get('VideoData', 'Keywords'), config.get('VideoData', 'PrivacyStatus')]
    
def write_config_for_playlist(playlist_name, meta_data):
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '\UploadsFolder\\' + playlist_name
    
    config = ConfigParser.RawConfigParser()
    
    config.add_section('VideoData')
    config.set('VideoData', 'Title', meta_data[0])
    config.set('VideoData', 'Description', meta_data[1])
    config.set('VideoData', 'Category', meta_data[2])
    config.set('VideoData', 'Keywords', meta_data[3])
    config.set('VideoData', 'PrivacyStatus', meta_data[4])
    
    with open(path + '\MetaDataFile.cfg', 'wb') as configfile:
        config.write(configfile)