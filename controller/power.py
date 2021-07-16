class power:
    __title__ = None
    __intro__ = None

    def __init__(self):
        self.__setTitle__()
        self.__setIntro__()

    def __setTitle__(self):
        self.__title__ = "PowerHub"

    def __setIntro__(self):
        self.__intro__ = "We have detect"

    def getTitle(self):
        return str(self.__title__)

    def getIntro(self):
        return str(self.__intro__)
