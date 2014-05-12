'''
Created on May 8, 2014

@author: Eddie
'''
import Tkinter as tk

from YT_Uploader_Playlist_Manager.YTapiManager import YTapi_interface
from YT_Uploader_Playlist_Manager.YTplaylistManager import YTdirectoryManager
from YT_Uploader_Playlist_Manager.YTplaylistManager import YTconfigManager

def onNewPlaylistSelect(evt):
    print('Hi')
    w = evt.widget
    index = int(w.curselection()[0])
    selected_playlist = w.get(index)
    print selected_playlist
        
 
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
        
        self.signIn_button = tk.Button(self, text='Sign In To Different YouTube Account', command=self.signInButtonCallback)
        self.signIn_button.grid(row=3, column=0, columnspan = 2)
        
        self.playlist_list = tk.Listbox(self)
        for p in self.getPlaylistsList():
            self.playlist_list.insert(tk.END, p)
        self.playlist_list.grid(row=4, rowspan = 2, column=0, columnspan = 2)
        self.playlist_list.select_set(0, 0)
        self.playlist_list.bind('<<ListBoxSelect>>', onNewPlaylistSelect)
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
        self.keyword_label = tk.Label(self, text = 'Keywords:')
        self.keyword_label.grid(row=3, column = 4)
        self.category_label = tk.Label(self, text = 'Category:')
        self.category_label.grid(row=4, column = 4)
        self.privacy_label = tk.Label(self, text = 'Privacy:')
        self.privacy_label.grid(row=5, column = 4)
        
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=1, column = 5)
        self.description_text = tk.Text(self, height = 5, width = 20)
        self.description_text.grid(row=2, column = 5)
        self.keyword_entry = tk.Entry(self)
        self.keyword_entry.grid(row=3, column = 5)
        
        #self.category_list = tk.Listbox(self, height = 3)
        #self.category_list.insert(tk.END, '22')
        #self.category_list.grid(row=4, column = 5)
        self.category_entry = tk.Label(self, text='22 (More coming in future version)')
        self.category_entry.grid(row=4, column=5)
        
        self.privacy_entry = tk.Entry(self)
        self.privacy_entry.grid(row=5, column = 5)
        
        self.setConfigView()
        
        #Button: Create new playlist
        self.Upload_videos_button = tk.Button(self, text = 'Upload Selected Video')
        self.Upload_videos_button.grid(row = 6, column = 2)
        #Button: Save Config
        self.save_config_button = tk.Button(self, text = 'Save Config Info', command=self.saveConfigButtonCallback)
        self.save_config_button.grid(row = 6, column = 5)
        
        self.init_all_playlists()
        
    def init_all_playlists(self):
        for p in self.playlist_list.get(0, tk.END):
            YTdirectoryManager.setup_playlist(p)
        
    def getPlaylistsList(self):
        yt = YTapi_interface.yt_auth(False)
        return YTapi_interface.list_my_playlists(yt)
    
    def getVideosToBeUploadedInPlaylist(self):
        list_selection = self.playlist_list.curselection()
        if len(list_selection) > 0:
            selected_playlist = self.playlist_list.get(list_selection[0])
            return YTdirectoryManager.get_videos_in_playlist(selected_playlist)
        else:
            return []
    
    def setConfigView(self):
        list_selection = self.playlist_list.curselection()
        if len(list_selection) > 0:
            selected_playlist = self.playlist_list.get(list_selection[0])
            meta_data = YTconfigManager.get_playlist_config_settings(selected_playlist)
        
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, meta_data[0])
        
            self.description_text.delete(-0.1, tk.END)
            self.description_text.insert(-0.1, meta_data[1])
        
            self.keyword_entry.delete(0, tk.END)
            self.keyword_entry.insert(0, meta_data[3])
        
            #self.category_list.select_set(0, 0)
        
            self.privacy_entry.delete(0, tk.END)
            self.privacy_entry.insert(0, meta_data[4])
                
    def saveConfigButtonCallback(self):
        print 'setting config'
        list_selection = self.playlist_list.curselection()
        if len(list_selection) > 0:
            selected_playlist = self.playlist_list.get(list_selection[0])
        else:
            print 'No Playlist'
            return
        
        meta_data = []
        meta_data.append(self.title_entry.get())
        meta_data.append(self.description_text.get(-0.1, tk.END))
        meta_data.append(self.category_entry['text'])
        meta_data.append(self.keyword_entry.get())
        meta_data.append(self.privacy_entry.get())
        
        YTconfigManager.write_config_for_playlist(selected_playlist, meta_data)
        
    def updateViewAfterNewPlaylistSelected(self, selected_playlist):
        self.video_list.delete(0, tk.END)
        for v in self.getVideosToBeUploadedInPlaylist(selected_playlist):
            self.video_list.insert(tk.END, v)
            
        self.setConfigView()
        
    def signInButtonCallback(self):
        auth_response = YTapi_interface.yt_auth(True)
        if auth_response == 'Auth-Failed':
            self.current_account_display['text'] = 'Authorization Failed\nYou are not signed in.'
        else:
            self.current_account_display['text'] = 'You are signed in!'
        
        self.playlist_list.delete(0, tk.END)
        for p in self.getPlaylistsList():
            self.playlist_list.insert(tk.END, p)
            
        self.video_list.delete(0, tk.END)
        for v in self.getVideosToBeUploadedInPlaylist():
            self.video_list.insert(tk.END, v)
        
        self.init_all_playlists()
        
        
    
app = Application()
app.master.title('YouTube Uploader and Playlist Manager')
app.mainloop()