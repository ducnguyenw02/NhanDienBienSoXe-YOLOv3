import tkinter as tk
import os
from tkinter import *
import tkinter.filedialog as fd
from tkinter import filedialog
import cv2
from detection import *
import numpy as np
import glob
from PIL import ImageTk,Image
import random

# Form main
root = tk.Tk()
root.geometry('320x29')
root.title("NHẬN DẠNG BIỂN SỐ XE")
root.iconbitmap('search.ico')
# open file
def openFile():
	filepath = filedialog.askopenfilename(initialdir = "D:\\Môn Học\\HK4-DS(3)-Thu thập và tiền xử lý dữ liệu\\Đồ án\\yolo_custom_detection\\Val",
										  title="CHỌN ẢNH", 
										  filetypes=(("jpg files","*.jpg"),("png files","*.png")))
	img = cv2.imread(filepath)
	dtc_img = detection(filepath)
	# img = cv2.resize(img,(600,400))
	if img is None:
		print("Wrong path")
	else:
		img = cv2.resize(img,(600,600))
		cv2.imshow("Image", img)
		dtc_img = cv2.resize(dtc_img,(600,600))
		cv2.imshow("Detection", dtc_img)
		cv2.waitKey(0)

# button
button = Button(text="Open",command=openFile)
button.pack()
# Loop
root.mainloop()


