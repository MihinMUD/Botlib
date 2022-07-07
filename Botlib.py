from types import NoneType


class Bot:
    def __init__(self, name:str , desp:str, showMsg=True):
        self.commands = {}
        self.name = name
        self.desp = desp
        self.showMsg = showMsg

    def onMessage(self, func:callable):
        self.commands[func.__name__] = func

    def runBot(self):
        if self.showMsg == True:
            self.send(f"I am {self.name} - {self.desp}")
        while True:
            req = str(input("User: ")).lower().strip()
            args = req.split()
            if req.startswith("exit"):
                break
            elif  req != "":
                try:
                    command = self.commands.get(args.pop(0))
                    command(args)
                except TypeError:
                    print("Invalid Command!")
                except Exception as e:
                    print(e)

    def send(self, ctx):
        print(f"{self.name}: {ctx}")

        
