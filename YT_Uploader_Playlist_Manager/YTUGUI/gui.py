'''
Created on May 8, 2014

@author: Eddie
'''
import Tkinter as tk

from YT_Uploader_Playlist_Manager.YTapiManager import YTapi_interface
from YT_Uploader_Playlist_Manager.YTplaylistManager import YTdirectoryManager
 
class Application(tk.Frame):    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        #Label: YouTube Info
        self.yt_label = tk.Label(self, text='YouTube Information\n|=========================|')
        self.yt_label.grid(row=0, column=0, columnspan = 2)
        #Label: Selected Playlist
        self.playlist_label = tk.Label(self, text='Selected Playlist\n|=========================|')
        self.playlist_label.grid(row=0, column=2)
        #Label: Config File
        self.config_label = tk.Label(self, text='Config File\n|=========================|')
        self.config_label.grid(row=0, column=4, columnspan = 2)
        #Panel: YouTube Info
        #    Label: Currently Signed in account
        #    Button: Sign In
        #    List: Playlists in channel
        self.current_account_label = tk.Label(self, text='Currently Logged In YouTube Account:')
        self.current_account_label.grid(row=1, column=0)
        self.current_account_display = tk.Label(self, text='No Account Logged In')
        self.current_account_display.grid(row=2, column=0)
        
        self.signIn_button = tk.Button(self, text='Sign In To Different YouTube Account')
        self.signIn_button.grid(row=3, column=0, columnspan = 2)
        
        self.playlist_list = tk.Listbox(self)
        for p in self.getPlaylistsList():
            self.playlist_list.insert(tk.END, p)
        self.playlist_list.grid(row=4, rowspan = 2, column=0, columnspan = 2)
        #Panel: Selected
        #    List: Videos in playlist
        self.video_list=tk.Listbox(self)
        for v in self.getVideosToBeUploadedInPlaylist():
            self.video_list.insert(tk.END, v)
        self.video_list.grid(row=0, rowspan = 6, column=2)
        #Panel: Conig File
        #    Labels for each meta data element
        #    Entries for each meta data element
        self.title_label = tk.Label(self, text = 'Title:')
        self.title_label.grid(row=1, column = 4)
        self.description_label = tk.Label(self, text = 'Description:')
        self.description_label.grid(row=2, column = 4)
        self.keyword_label = tk.Label(self, text = 'Keyword:')
        self.keyword_label.grid(row=3, column = 4)
        self.category_label = tk.Label(self, text = 'Category:')
        self.category_label.grid(row=4, column = 4)
        self.privacy_label = tk.Label(self, text = 'Privacy:')
        self.privacy_label.grid(row=5, column = 4)
        
        self.title_entry = tk.Entry(self, text = 'Title:')
        self.title_entry.grid(row=1, column = 5)
        self.description_entry = tk.Entry(self, text = 'Description:')
        self.description_entry.grid(row=2, column = 5)
        self.keyword_entry = tk.Entry(self, text = 'Keyword:')
        self.keyword_entry.grid(row=3, column = 5)
        self.category_entry = tk.Entry(self, text = 'Category:')
        self.category_entry.grid(row=4, column = 5)
        self.privacy_entry = tk.Entry(self, text = 'Privacy:')
        self.privacy_entry.grid(row=5, column = 5)
        
        #Button: Create new playlist
        self.new_playlist_button = tk.Button(self, text = 'Create New Playlist')
        self.new_playlist_button.grid(row = 6, column = 2)
        #Button: Save Config
        self.save_config_button = tk.Button(self, text = 'Save Config Info')
        self.save_config_button.grid(row = 6, column = 5)
        
    def getPlaylistsList(self):
        yt = YTapi_interface.yt_auth(False)
        return YTapi_interface.list_my_playlists(yt)
    
    def getVideosToBeUploadedInPlaylist(self):
        selected_playlist = self.playlist_list.curselection()
        YTdirectoryManager.setup_playlist(selected_playlist)
    
app = Application()
app.master.title('YouTube Uploader and Playlist Manager')
app.mainloop()