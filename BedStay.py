
from Bed import Bed
class BedStay():
    def __init__(self,start_bedstay,bed):
        self.__start_bedstay=start_bedstay
        self.__end_bedstay=''
        self.__bed=bed

    @property
    def start_bedstay(self):
        return self.__start_bedstay

    @start_bedstay.setter
    def start_bedstay(self,start_bedstay):
        self.__start_bedstay = start_bedstay

    @property
    def end_bedstay(self):
        return self.__end_bedstay

    @end_bedstay.setter
    def end_bedstay(self,end_bedstay):
        self.__end_bedstay = end_bedstay

    @property
    def bed(self):
        return self.__bed

    @bed.setter
    def bed(self,bed):
        self.__bed = bed

    def __repr__(self):
        return self.__class__.__name__ + "('{:s}','{:s}','{}')".format(
            self.__start_bedstay,self.__end_bedstay,self.__bed)

