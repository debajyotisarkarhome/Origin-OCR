import cv2
import pytesseract
from tkinter import *
from tkinter.filedialog import *
from autocorrect import Speller
import os
fil=""
ra = Tk()
ra.title('Origin OCR')
ra.configure(background="#03031b")
ta=StringVar(ra)
ta.set("Select File or Folder Then Click Start")
ra.configure(height="999",width="999")
Label(ra,text="Welcome to Origin-OCR      ",font=('arial',21),bg="#03031b",fg="white").grid(row=0,column=1)
Label(ra,text="Language : ",font=('arial',15),fg="white",bg="#03031b").grid(row=1,column=0)
variable = StringVar(ra)
variable.set("eng")
drp=OptionMenu(ra, variable, "eng","ben",)
drp.config(width=6, font=('Helvetica', 12))
drp.grid(row=1,column=1)
if variable=="English":
    variable.set(eng)
elif variable=="Bengali":
    variable.set(ben)
def sel_file():
    global fil
    filo=askopenfilename()
    cp_fil=filo
    l=[]
    l.append(cp_fil)
    fil=l
def sel_dir():
    global fil
    filo=askdirectory()
    ll=os.listdir(filo.replace("/","\\"))
    fil=[]
    for i in range(0,len(ll)):
        ach=ll[i]
        #print(ach[-3:])
        if ach[-3:]=="jpg" or ach[-3:]=="JPG" or ach[-3:]=="png":
            fil.append(filo.replace("/","\\")+"\\"+ll[i])
    
    
        
        
               
    
    
    
def start():
        mk=variable.get()
        print(fil)
        for i in range(0,len(fil)):
            spell=Speller()
            f=cv2.imread(fil[i])
            print(fil[i])
            #cv2.imshow("mm",f)
            gray=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
            adap=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,29,11)
            #cv2.imshow("test",adap)
            if mk=="eng":
                tex=spell(pytesseract.image_to_string(adap,lang=mk))
            elif mk=="ben":
                tex=pytesseract.image_to_string(adap,lang=mk)
            pth=fil[i]
            print(pth)
            path_new=pth.replace(".jpg",".txt")
            path_new=path_new.replace(".JPG",".txt")
            #path_new=pth.replace("png","txt")
            de=open(path_new,"wb")
            de.write(tex.encode("utf8"))
            de.close()
            
    
Button(ra,text="Select File",command=sel_file).grid(row=4,column=0,padx=5,pady="20")
Label(ra,text="OR",bg="#03031b").grid(row=4,column=1)
Button(ra,text="Select Folder",command=sel_dir).grid(row=4,column=2,pady="20",padx=20)
Label(ra,textvariable=ta,bg="#03031b",fg="white",font=("Arial",12)).grid(row=5,column=1)
Button(ra,text="Start",padx=20,command=start).grid(row=6,column=1,pady="20")






ra.mainloop()

