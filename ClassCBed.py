
from Bed import Bed
class ClassCBed(Bed):
    def __init__(self,ward_no,bed_no):
        super().__init__(ward_no,bed_no,'C',39,87,222)
        self.__portable_tv=False

    @property
    def portable_tv(self):
        return self.__portable_tv
    
    @portable_tv.setter
    def portable_tv(self,portable_tv):
        self.__portable_tv = portable_tv

    def calculate_charges(self,citizen_status):
        if citizen_status=='SC':
            amount=self.sc_cost
        elif citizen_status=='PR':
            amount=self.pr_cost
        elif citizen_status=='Foreigner':
            amount=self.foreigner_cost
        if self.__portable_tv:
            amount+=30
        return amount
    
    def __repr__(self):
        return self.__class__.__name__ + "('{:d}','{:d}')".format(self.ward_no,self.bed_no)
