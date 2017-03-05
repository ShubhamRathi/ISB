import os
files = os.listdir('D:\\Sandeep\\Intel')
for f in files:
    type("cd D:\\Sandeep\\Intel\\" + str(f) + Key.ENTER)
    fn = "Intel_Network_" + f +".txt"
    type("File =loaddl("+fn+")" + Key.ENTER)
    wait(1)
    type(Key.ENTER)
