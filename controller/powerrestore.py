import calendar
import datetime
import os

from controller.power import power

class powerrestore( power ):
    __brief__ = None
    __descr__ = None
    __perc__ = None

    def __init__(self):
        super().__init__()
        self.__setBrief__()
        self.__setDescr__()

    def __setBrief__(self):
        self.__brief__ = "a power grid restoration"

    def __setDescr__(self):
        wday = str( calendar.day_name[ datetime.date.today().weekday() ] )
        day = str( datetime.date.today().day )
        month = str ( calendar.month_name[ datetime.date.today().month ] )
        year = str( datetime.date.today().year )
        hour = str( datetime.datetime.now().hour )
        min = str( datetime.datetime.now().minute )
        out = os.popen( "apcaccess | grep BCHARGE | cut -d : -f 2 | cut -d ' ' -f 2").read()
        # out = "100%" #TODO


        self.__descr__ = '%s, %s %s %s at %s:%s'%(wday, day, month, year, hour, min)

        self.__perc__ = '%s'%(out)




    def getBrief(self):
        return str( self.__brief__ )

    def getTimeDescr(self):
        return str( self.__descr__ )

    def getPercDescr(self):
        return str( self.__perc__ )






