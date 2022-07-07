class Bot:
    def __init__(self, name:str , desp:str):
        self.commands = {}
        self.name = name
        self.desp = desp

    def onMessage(self, func:callable):
        self.commands[func.__name__] = func

    def runBot(self):
        self.send("I am MUD - "+self.desp)
        while True:
            req = str(input("User: ")).lower().strip()
            args = req.split()
            if req.startswith("exit"):
                break
            elif  req != "":
                command = self.commands.get(args.pop(0))
                command(args)

    def send(self, ctx):
        print(f"{self.name}: {ctx}")
