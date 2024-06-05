import os
from customtkinter import *
from pytube import YouTube, exceptions

class YouTubeVideoDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("500x500")

        self.create_gui()

    def create_gui(self):
        # Create a label and entry for the video URL
        url_label = CTkLabel(self.root, text="Video URL:")
        url_label.pack(pady=10)
        self.url_entry = CTkEntry(self.root, placeholder_text="Enter video URL")
        self.url_entry.pack(pady=5)

        # Create a label and entry for the save path
        path_label = CTkLabel(self.root, text="Save Path:")
        path_label.pack(pady=10)
        self.path_entry = CTkEntry(self.root, placeholder_text=os.getcwd())
        self.path_entry.pack(pady=5)

        # Create a label to display the download status
        self.status_label = CTkLabel(self.root, text="")
        self.status_label.pack(pady=10)

        # Create a download button
        download_button = CTkButton(self.root, text="Download", command=self.download_video)
        download_button.pack(pady=10)

    def download_video(self):
        try:
            # Get the video URL and save path from the entry fields
            video_url = self.url_entry.get()
            save_path = self.path_entry.get()

            # Update the status label
            self.status_label.configure(text="Downloading...")

            # Create a YouTube object with the video URL
            yt = YouTube(video_url)

            # Select the highest resolution available
            video = yt.streams.get_highest_resolution()

            # Download the video to the specified path
            video.download(save_path)

            # Update the status label
            self.status_label.configure(text="Download completed!")
        except exceptions.VideoUnavailable as e:
            self.status_label.configure(text=f"Error: Video unavailable ({e})")
        except IOError as e:
            self.status_label.configure(text=f"Error: IO error ({e})")
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}")

if __name__ == "__main__":
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    root = CTk()
    app = YouTubeVideoDownloader(root)
    root.mainloop()