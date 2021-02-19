import fbdown
import os

def VideoDownload():
    get_link=fbdown.getdownlink("https://www.facebook.com/watch/?v=946679739019054&extid=vOpCffapZoXjYEeO")
    download_it=get_link
    file_path=str(os.chdir("C:\\Users\\TalhaZunair\\Downloads\\Video"))
    fbdown.download(download_it,file_path)

print(VideoDownload())