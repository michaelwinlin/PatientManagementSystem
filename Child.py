# Student Number : S10165254A , S10127952K
# Student Name   : Lin XiongQing and Lin Yu Hsien
# Module Group   : FI 04

from Patient import Patient
from Bed import Bed
from ClassABed import ClassABed
from ClassBBed import ClassBBed
from ClassCBed import ClassCBed
class Child(Patient):
    def __init__(self,id,name,age,gender,citizen_status,cda_balance):
        super().__init__(id,name,age,gender,citizen_status)
        self.__cda_balance=cda_balance

    @property
    def cda_balance(self):
        return self.__cda_balance

    @cda_balance.setter
    def cda_balance(self,cda_balance):
        self.__cda_balance = cda_balance

    def calculate_charges(self):
        total=0
        import datetime
        format = "%d/%m/%Y"
        for i,each in enumerate(self.stay_list):
            if each.payment_status=='Unpaid':
                print('=====Stay # {}====='.format(i+1))
                print('Admission date:',each.admitted_date)
                print('Discharge date:',each.discharge_date)
                print('Payment status:',each.payment_status)
                for n,every in enumerate(each.bedstay_list):
                    print('=====Bed # {}====='.format(n+1))
                    print('Ward number:',every.bed.ward_no)
                    print('Bed number:',every.bed.bed_no)
                    print('Ward class:',every.bed.bed_type)
                    print('Start of bed stay:',every.start_bedstay)
                    print('End of bed stay:',every.end_bedstay)
                    if isinstance(every.bed,ClassABed):
                        print('Accompany person:',every.bed.accompanying_person)
                    if isinstance(every.bed,ClassBBed):
                        print('Air-conditioned variant:',every.bed.air_con)
                    if isinstance(every.bed,ClassCBed):
                        print('Portable TV:',every.bed.portable_tv)
                    start=datetime.datetime.strptime(every.start_bedstay,format)
                    end=datetime.datetime.strptime(every.end_bedstay,format)
                    days=(end-start).days
                    print('Number of days stayed:',days)
                    sub=days*every.bed.calculate_charges(self.citizen_status)
                    print('Total charges:$',sub)
                    total+=sub
        if self.__cda_balance < total:
            subtotal=total-self.__cda_balance
            deduct=self.__cda_balance
        else:
            subtotal=0
            deduct=total
        print('=========')
        print('Total charges pending:$',total)
        print('CDA balance:$',self.__cda_balance)
        print('To deduct from CDA:$',deduct)
        print('Sub-total:',subtotal)
        payment=input('\nWould you like to make payment now?[Y/N]: ').upper()
        if payment=='Y':
            print('\nCommencing payment...')
            self.stay_list[-1].payment_status='Paid'
            self.status='Registered'
            print('\n$ {:d} has been deducted from CDA balance'.format(deduct))
            self.__cda_balance= self.__cda_balance-deduct
            print('New CDA balance:$',self.__cda_balance)
            print('Sub-toal:${:d} has been paid by cash'.format(subtotal))
            print('\nPayment successful!')
        else:
            print('\nPayment cancelled.')
            

    def __repr__(self):
        return self.__class__.__name__ + "('{:s}','{:s}','{:d}','{:s}','{:s}','{:s}',{:d})".format(
            self.id,self.name,self.age,self.gender,self.citizen_status,self.__cda_balance)



    
