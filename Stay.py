# Student Number : S10165254A , S10127952K
# Student Name   : Lin XiongQing and Lin Yu Hsien
# Module Group   : FI 04

class Stay():
    def __init__(self,admitted_date):
        self.__admitted_date=admitted_date
        self.__discharge_date=''
        self.__payment_status='Unpaid'
        self.__record_list=[]
        self.__bedstay_list=[]

    @property
    def admitted_date(self):
        return self.__admitted_date

    @admitted_date.setter
    def admitted_date(self,admitted_date):
        self.__admitted_date = admitted_date

    @property
    def discharge_date(self):
        return self.__discharge_date

    @discharge_date.setter
    def discharge_date(self,discharge_date):
        self.__discharge_date = discharge_date

    @property
    def payment_status(self):
        return self.__payment_status

    @payment_status.setter
    def payment_status(self,payment_status):
        self.__payment_status = payment_status

    @property
    def record_list(self):
        return self.__record_list

    @property
    def bedstay_list(self):
        return self.__bedstay_list

    def add_record(self,MedicalRecord):
        self.__record_list.append(MedicalRecord)

    def add_bedstay(self,BedStay):
        self.__bedstay_list.append(BedStay)

    def __repr__(self):
        return self.__class__.__name__ + "('{:s}','{:s}','{:s}')".format(self.__admitted_date,self.__discharge_date,self.__payment_status)



    
