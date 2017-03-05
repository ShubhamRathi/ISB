import os
# files = os.listdir('D:\\Sandeep\\Cisco')
files = range(1998, 2011)
for f in files:
    f = str(f)
    App('Uci6').focus()
    type("f",KeyModifier.CTRL)
    wait(1)
    click(Pattern("3.png").targetOffset(11,-2))
    wait(1)
    type("a",KeyModifier.CTRL)
    type("D:\\Sandeep\\Cisco\\" + str(f) + Key.ENTER)
    click(Pattern("1488754505777.png").targetOffset(-8,-3))
    click("1488754822665.png")
    click("4.png")
    click(Pattern("1488754897120.png").similar(0.68).targetOffset(0,-3))
    type("a",KeyModifier.CTRL)
    type("D:\\Sandeep\\Cisco\\" + str(f) + "\\FILE.##h"+ Key.ENTER)
    notepad=App("notepad")
    while True:
       if notepad.isRunning():
           notepad.focus()
           notepad.close()
           break;
    
    
    
    