import speech_recognition as sr

from Tkinter import *
r = sr.Recognizer()



class MotusGUI:
    def __init__(self, master):
        self.master = master
        master.title("Motus")

        self.label = Label(master, text="Welcome to Motus!")
        self.label.pack()

        self.greet_button = Button(master, text="Click Me & Say Something!", command=self.action)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def action(self):
        var = StringVar()
        
        
        with sr.Microphone() as source:
            audio = r.listen(source)
        
        try:
   
            m = "Alright! The Motus app thinks you said " + r.recognize_google(audio)
        except sr.UnknownValueError:
            m = "Motus could not understand what you said!!"
        except sr.RequestError as e:
            m = "Motus was unsuccessful to request service; {0}".format(e)

        label = Message( root, textvariable=var, relief=RAISED)
        var.set(m)
        label.pack()

root = Tk()
my_gui = MotusGUI(root)
root.mainloop()