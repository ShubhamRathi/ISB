import os
companies = ['TI']
for c in companies:
    path = 'D:\\Sandeep\\'+ c
    files = os.listdir(path)
    if c == 'TI':
        files = range(2006, 2011)        
    for f in files:
        f = str(f)
        App('Uci6').focus()
        type("f",KeyModifier.CTRL)
        wait(1)
        click(Pattern("1488787044063.png").targetOffset(-103,-15))    
        wait(1)
        type("a",KeyModifier.CTRL)
        type(path+ "\\" + str(f) + Key.ENTER)
        click(Pattern("1488754505777.png").targetOffset(-8,-3))
        click("1488805796309.png")
        click("1.png")
        click("1_1.png")
        wait(1)
        click(Pattern("1_2.png").targetOffset(-15,-86))
        loc = path +'\\'+ str(f) +"\\FILE-maxsym.##h"
        wait(1)
        type("a",KeyModifier.CTRL)
        type(loc)
        wait(1)
        click("1489059722535.png")
        notepad=App("notepad")
        while True:
           if notepad.isRunning():
               notepad.focus()
               click(Pattern("5.png").targetOffset(-90,-1))
               click(Pattern("Screenshot_5.png").targetOffset(-57,0))
               click(Pattern("Screenshot_6.png").targetOffset(-107,-5))
               wait(1)
               type("a",KeyModifier.CTRL)
               fn = path+'\\' + f +"\Closeness.txt"
               type(fn)
               click("Screenshot_7.png")
               notepad.close()
               break;