class Bot:
    def __init__(self, name:str , desp:str , startMesg:bool = True , customMesg:str = f"Hi i m a") -> None:
        self.name = name
        self.desp =  desp
        self.customMesg = customMesg
        
    def onMessage(slef , ctx:str):
            pass

    def runBot(self):
        while True:
            req = str(input("User: "))
            if  req != "":
                self.onMessage(req)