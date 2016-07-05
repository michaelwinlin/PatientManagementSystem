class MedicalRecord:
    def __init__(self,diagnosis,temperature,entry_added):
        self.__diagnosis=diagnosis
        self.__temperature=temperature
        self.__entry_added=entry_added


    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self,diagnosis):
        self.__diagnosis = diagnosis

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self,temperature):
        self.__temperature = temperature

    @property
    def entry_added(self):
        return self.__entry_added

    @entry_added.setter
    def entry_added(self,entry_added):
        self.__entry_added = entry_added
