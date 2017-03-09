import os
path = 'D:\\Sandeep\\Cisco\\'
files = os.listdir(path)
for f in files:
    f = str(f)
    App('Uci6').focus()
    type("f",KeyModifier.CTRL)
    wait(1)
    click(Pattern("1488787044063.png").targetOffset(-103,-15))    
    wait(1)
    type("a",KeyModifier.CTRL)
    type("D:\\Sandeep\\Cisco\\" + str(f) + Key.ENTER)
    click(Pattern("1488754505777.png").targetOffset(-8,-3))
    click("1488805796309.png")
    click("Screenshot_1.png")
    click("Screenshot_2.png")
    loc = path + str(f) +"\\FILE-maxsym.##h"
    wait(1)
    click(Pattern("Screenshot_8.png").similar(0.50).targetOffset(90,-24))
    type("a",KeyModifier.CTRL)
    type(loc)
    click(Pattern("Screenshot_3.png").targetOffset(-154,-32))
    type(Key.DOWN)
    click("Screenshot_4.png")
    notepad=App("notepad")
    while True:
       if notepad.isRunning():
           notepad.focus()
           click(Pattern("5.png").targetOffset(-90,-1))
           click(Pattern("Screenshot_5.png").targetOffset(-57,0))
           click(Pattern("Screenshot_6.png").targetOffset(-107,-5))
           wait(1)
           type("a",KeyModifier.CTRL)
           fn = path + f +"\DegreeCentrality.txt"
           type(fn)
           click("Screenshot_7.png")
           notepad.close()
           break;
           
           
           
           
    
    
    
    
    