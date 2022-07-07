# Botlib
A bot lib for python


# How to use it
Download the Botlib.py file and move it to your project dir

```py
from Botlib import Bot
from random import randint

mybot = Bot("Bot", "nice bot")

@mybot.onMessage
def hi(ctx):
    mybot.send("hi")

@mybot.onMessage
def randnum(ctx):
    try:
        mybot.send(randint(1, int(ctx[0])))
    except:
        mybot.send("Empty or wrong Input!")

mybot.runBot()
```

a example code on how to use it
