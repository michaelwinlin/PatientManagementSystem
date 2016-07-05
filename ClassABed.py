
from Bed import Bed
class ClassABed(Bed):
    def __init__(self,ward_no,bed_no):
        super().__init__(ward_no,bed_no,'A',430,430,430)
        self.__accompanying_person=False

    @property
    def accompanying_person(self):
        return self.__accompanying_person

    @accompanying_person.setter
    def accompanying_person(self,accompanying_person):
        self.__accompanying_person = accompanying_person

    def calculate_charges(self,citizen_status):
        if citizen_status=='SC':
            amount=self.sc_cost
        elif citizen_status=='PR':
            amount=self.pr_cost
        elif citizen_status=='Foreigner':
            amount=self.foreigner_cost
        if self.__accompanying_person:
            amount+=100
        return amount

    def __repr__(self):
        return self.__class__.__name__ + "('{:d}','{:d}')".format(
            self.ward_no,self.bed_no)
