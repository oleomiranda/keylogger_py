# Keylogger in Python for studying purposes

The program saves the words in a variable and send it to the email that you chose after the time you chose too <br>
The lib (pynput) bugs when you press two keys at the same tipe like 'CTRL + C' and it returns a ASCII code like \x031 so the code
writes to the file [code returned by pynput] + ASCII Control code


# Libs used 
- re (regex)
- pynput (kyboard)
- threading
- smtplib

