class Bot:
    def __init__(self, name:str , desp:str , startMesg:bool = True , customMesg:str = f"Hi i m a") -> None:
        self.name = name
        self.desp =  desp
        self.customMesg = customMesg
        
    def onMessage(self, ctx:str):
            pass

    def runBot(self):
        while True:
            req = str(input("User: "))
            if req == "exit":
                break
            elif  req.lower() != "":
                self.onMessage(req)
    
    def command(self, func:callable):
        cmdName = func.__name__
        def onMessage(ctx):
            if ctx.lower() == cmdName.lower():
                func(ctx)
        self.onMessage = onMessage
    
    def send(self, ctx):
        print(f"{self.name}: {ctx}")

        
