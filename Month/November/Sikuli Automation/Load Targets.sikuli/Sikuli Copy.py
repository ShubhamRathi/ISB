for i in [1,11,125,150]:
    type("cd D:\\ISB\\Pairs\\" + str(i) + "\\Target\\" + Key.ENTER)
    #wait(2)
    type("T=loaddl(T.txt)" + Key.ENTER)
    type(Key.ENTER)
    type("Tr=transp(T)" +Key.ENTER)
    type("save Tr \"Tr.csv\"" + Key.ENTER)
    wait(2)
    

