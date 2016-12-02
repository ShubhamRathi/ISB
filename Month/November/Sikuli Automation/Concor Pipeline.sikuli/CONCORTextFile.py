a=[75]
for i in a:
    # 68, 74, 75
    App('Uci6').focus()
    type("f",KeyModifier.CTRL)
    wait(1)
    type("D:\\ISB\\V2\\"+str(i)+"\\CONCOR\\")
    click("1480620083223.png")
    click("1480617320011.png")
    wait(1)
    click("1480617365233.png")
    click("2.png")
    click("1.png")
    click("3.png")
    wait(1)
    click(Pattern("1480618017082.png").targetOffset(-63,-119))
    type("a",KeyModifier.CTRL)
    type("D:\\ISB\\V2\\"+str(i)+"\\Sum\\SUM.##h")
    click("1480618295382.png")
    notepad=App("notepad")
    while True:
       if notepad.isRunning():
           notepad.focus()
           click(Pattern("1480631027863.png").targetOffset(-88,-4))
           wait(1)
           
           click(Pattern("1480631100587.png").targetOffset(-41,-8))
           click(Pattern("1480631782828.png").targetOffset(-104,-15))
           
           type("a",KeyModifier.CTRL)
           type("D:\\ISB\\V2\\"+str(i)+"\\CONCOR\\Concor.txt")
           click(Pattern("1480631275305.png").targetOffset(63,-6))
           
           notepad.close()
           break;
    click(Pattern("1480632228962.png").targetOffset(134,31))
    

    
    
    