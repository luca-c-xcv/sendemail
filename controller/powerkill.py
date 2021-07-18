from controller.power import power

class powerkill( power ):
    __brief__ = None


    def __init__(self):
        super().__init__()
        self.__setBrief__()

    def __setIntro__(self):
        self.__intro__ = "We need"


    def __setBrief__(self):
        self.__brief__ = "to kill the server"


    def getIntro(self):
        return str(self.__intro__)


    def getBrief(self):
        return str( self.__brief__ )







