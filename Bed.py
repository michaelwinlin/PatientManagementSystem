# Student Number : S10165254A , S10127952K
# Student Name   : Lin XiongQing and Lin Yu Hsien
# Module Group   : FI 04

from abc import ABCMeta,abstractmethod
class Bed(metaclass=ABCMeta):
    def __init__(self,ward_no,bed_no,bed_type,sc_cost,pr_cost,foreigner_cost):
        self.__ward_no=ward_no
        self.__bed_no=bed_no
        self.__bed_type=bed_type
        self.__sc_cost=sc_cost
        self.__pr_cost=pr_cost
        self.__foreigner_cost=foreigner_cost
        self.__available=True

    @property
    def ward_no(self):
        return self.__ward_no

    @ward_no.setter
    def ward_no(self,ward_no):
        self.__ward_no = ward_no

    @property
    def bed_no(self):
        return self.__bed_no

    @bed_no.setter
    def bed_no(self,bed_no):
        self.__bed_no = bed_no

    @property
    def bed_type(self):
        return self.__bed_type

    @bed_type.setter
    def bed_type(self,bed_type):
        self.__bed_type = bed_type

    @property
    def sc_cost(self):
        return self.__sc_cost

    @sc_cost.setter
    def sc_cost(self,sc_cost):
        self.__sc_cost = sc_cost

    @property
    def pr_cost(self):
        return self.__pr_cost

    @pr_cost.setter
    def pr_cost(self,pr_cost):
        self.__pr_cost = pr_cost

    @property
    def foreigner_cost(self):
        return self.__foreigner_cost

    @foreigner_cost.setter
    def foreigner_cost(self,foreigner_cost):
        self.__foreigner_cost = foreigner_cost

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self,available):
        self.__available = available

    @abstractmethod
    def calculate_charges(self,citizen_status):
        pass

    def __repr__(self):
        return self.__class__.__name__ + "('{:d}','{:d}','{:s}',{:.2f},{:.2f},{:.2f},{})".format(
            self.__ward_no,self.__bed_no,self.__bed_type,self.__sc_cost,self.__,pr_cost,self.__foreigner_cost,self.__available)

    


