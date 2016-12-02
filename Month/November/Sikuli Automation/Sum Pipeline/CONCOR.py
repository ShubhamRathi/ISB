n='y'
def vanish(event):
    popup("Detected")
    
for i in [101]:    
    if(n=='y'):
        App('Uci6').focus()
        click("1480613303580.png")
        type("cd D:\\ISB\\V2\\" + str(i) + "\\Sum\\" + Key.ENTER)
        #wait(2)
        hover(Location(700,500))
        type("Sum=loadcsv(sum.csv)" + Key.ENTER)
        wait(3)
        if waitVanish(Pattern("cursor.png").similar(0.50),3600):
            popup("Found")
        #n=input('Continue?')
    else:
        break