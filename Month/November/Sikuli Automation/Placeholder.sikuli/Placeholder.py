button= "cursor.png"
        while(1):
            wait(Button, 30*60) # This will spinlock for 30 minutes for the button to appear
            if exists(Button):
                popup("Found")
                break;