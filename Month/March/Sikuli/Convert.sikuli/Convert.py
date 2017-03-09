import os
files = os.listdir('D:\\Sandeep\\Cisco')
for f in files:
    type("cd D:\\Sandeep\\Cisco\\" + str(f) + Key.ENTER)
    fn = "Cisco_Network_" + f +".txt"
    type("File =loaddl("+fn+")" + Key.ENTER)
    wait(1)
    type(Key.ENTER)
