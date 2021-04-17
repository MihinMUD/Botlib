# Botlib
A bot lib for python


#How to use it
Download the bot.py file and move it to your project dir

```py
from Botlib import Bot
from random import randint
bot = Bot("Mud" , "Cool Bot")

def onMessage(ctx:str):
    if ctx == "hi":
        print("hello")
    
    elif ctx.startswith("roll"):
        args = ctx.split(" ")
        ans = randint(0,int(args[1]))
        print(f"you rolled {ans}")
    else:
        print("Invalid command")


bot.onMessage = onMessage
bot.runBot()
```

a example code on how to use it
