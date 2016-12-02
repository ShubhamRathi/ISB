for i in [24]:
    wait("1480588716895.png")
    type("cd D:\\ISB\\Pairs\\" + str(i) + "\\Acq\\" + Key.ENTER)
    type("A=loaddl(A.txt)" + Key.ENTER)
    wait(3)
    type(Key.ENTER)
    type("save A \"A.csv\"" + Key.ENTER)
    wait(3)
    

