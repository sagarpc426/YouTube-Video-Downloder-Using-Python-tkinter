from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

folderName = ""

class Download:
	def __init__(self,root):
		self.root = root
		self.root.title("Download YouTube Video")
		self.root.geometry("800x300+300+200")
		self.root.resizable(False, False)
		frameDetails = Frame(self.root, bg="white")
		frameDetails.place(x=10, y=10, width=780, height=280)
		youtubeUrl = Label(frameDetails, text= "Enter Url", font=("Goudy old style",15), fg="black", bg="white").place(x=30,y=30)
		self.text_url = Entry(frameDetails, font=("times new roman",13), bg="lightgray")
		self.text_url.place(x=200,y=30, width=500, height=30)
		self.location = Button(frameDetails, command=self.getLocation, text="Choose Location", font=("Goudy old style",15), fg="white", bg="#d77337").place(x=30,y=80,width=150, height=40)		
		self.locationError = Label(self.root, text="Choose destination folder to save video.. ",font=("Goudy old style",15), fg="red", bg="white", anchor="w").place(x=250,y=90,width=500, height=30)
		self.downBtn = Button(frameDetails, command=self.download_fun, text="Download", font=("Goudy old style",15), fg="white", bg="#d77337").place(x=330,y=180,width=120, height=40)

	def download_fun(self):
		if self.text_url.get()=="":
			messagebox.showerror("Error","Please Enter Url", parent=self.root)
		else:
			print(self.text_url.get())
			messagebox.showinfo("Downloading","Your video will download soon", parent=self.root)
			video = YouTube(self.text_url.get())
			video = video.streams.get_highest_resolution()
			video.download(folderName)

	def getLocation(self):
		global folderName
		folderName = filedialog.askdirectory()
		if len(folderName)>1 :
			self.locationError = Label(self.root, text= folderName, font=("Goudy old style",15), fg="green", bg="white", anchor="w").place(x=250,y=90,width=500, height=30)
		else :
			self.locationError = Label(self.root, text= "Please Choose Folder...!!!", font=("Goudy old style",15), fg="red", bg="white", anchor="w").place(x=250,y=90,width=500, height=30)

root = Tk()
obj = Download(root)
root.mainloop()