
from Bed import Bed
class ClassBBed(Bed):
    def __init__(self,ward_no,bed_no):
        super().__init__(ward_no,bed_no,'B',240,269,308)
        self.__air_con=False

    @property
    def air_con(self):
        return self.__air_con
    
    @air_con.setter
    def air_con(self,air_con):
        self.__air_con = air_con

    def calculate_charges(self,citizen_status):
        if citizen_status=='SC':
            amount=self.sc_cost
        elif citizen_status=='PR':
            amount=self.pr_cost
        elif citizen_status=='Foreigner':
            amount=self.foreigner_cost
        if self.__air_con:
            amount+=50
        return amount

    def __repr__(self):
        return self.__class__.__name__ + "('{:d}','{:d}')".format(self.ward_no,self.bed_no)
