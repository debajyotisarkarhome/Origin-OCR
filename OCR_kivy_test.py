from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
import kivy
pug=0
shownum=0
class Gri(GridLayout):
    def __init__(self,**kwargs):
        global pug
        global shownum
        super(Gri,self).__init__(**kwargs)
        self.cols=1
        self.inter=GridLayout()
        self.inter.cols=2
        self.sel_file=Button(text="Select File",font_size=30,size_hint=(0.5,0.5))
        self.sel_folder=Button(text="Select Folder",font_size=30,size_hint=(0.5,0.5))
        self.inter.add_widget(self.sel_file)
        self.inter.add_widget(self.sel_folder)
        







        
        #self.showspace=GridLayout()
        #self.showspace.cols=shownum
        #self.interaction.add_widget(Label(text="Select The File or Folder You Wanna Scan",font_size=30))
        ########## layout_main ##########
        self.add_widget(Image(source="head.jpg"))

        pb=ProgressBar(max=100)
        self.add_widget(pb)
        pb.value=pug

        self.add_widget(Label(text="Select The [b]File[/b] or [b]Folder[/b] You Wanna Scan",font_size=30,markup=True))

        self.add_widget(self.inter)

        self.strt=Button(text="Start",font_size=40,padding=(100,100),size_hint=(0.0001,0.4))
        self.add_widget(self.strt)
        ################layout main end#############

class OriginOCR(App):
    def build(self):
        return Gri()



if __name__ == "__main__":
    OriginOCR().run()
