from tkinter import *
from PIL import ImageTk,Image
import os
import fbdown
root=Tk()
root.geometry("550x300")
root.maxsize(height=300,width=550)
root.minsize(height=300,width=550)
root.title("FB Downloader")

# =================MainWindows Image========================
main_window=ImageTk.PhotoImage(Image.open("Fbdownloader.png"))
panel=Label(root,image=main_window)
panel.place(x=-2,y=0)
# ======================EntryUrl============================
# =======================EntryUrl End=========================
# =================UrlLabel====================================
url_lbl=Label(root,text="URL HERE:")
url_lbl.place(x=50,y=172)
# =================UrlLabel End====================================
# =================Functions==================================
def VideoDownload():
    get_link=fbdown.getdownlink(download_url.get("1.0","end-1c"))
    download_it=get_link
    file_path=str(os.chdir("C:\\Users\\TalhaZunair\\Downloads\\Video"))
    fbdown.download(download_it,file_path)

download_url = Text(root, height=1.4, width=30)
download_url.place(x=130, y=172)
# =================Functions End==============================
# =====================DownloadButton==============================
download_button_image=ImageTk.PhotoImage(Image.open("DownloadButton.png"))
download_button=Button(image=download_button_image,command=VideoDownload)
download_button.place(x=385,y=158)


root.mainloop()