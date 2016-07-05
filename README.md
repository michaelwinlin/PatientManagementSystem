# PatientManagementSystem

from Patient import Patient
from Child import Child
from Adult import Adult
from Senior import Senior
from Bed import Bed
from Stay import Stay
from BedStay import BedStay
from MedicalRecord import MedicalRecord
from ClassABed import ClassABed
from ClassBBed import ClassBBed
from ClassCBed import ClassCBed


def menu ():
    print('\nMENU\n=====')
    print('1. Register patient')
    print('2. View all patients')
    print('3. View all beds')
    print('4. View all available beds')
    print('5. Register a hospital stay')
    print('6. Retrieve patient details')
    print('7. Enter medical record entry')
    print('8. View medical records')
    print('9. Monitor a patient')
    print('10. Transfer patient to another bed')
    print('11. Discharge patient')
    print('12. View and make payment')
    print('0. Exit')
    #print('\n')

    
def registration(plist):
    print('\nOption 1.Register Patient')
    Name=input('Enter name: ')
    ID=input('Enter identification Number: ').upper()
    Age=int(input('Enter age: '))
    Gender=input('Enter Gender [M/F]: ').upper()
    CZStatus=input('Enter Citizenship Status [SC/PR/Foreigner]: ')
    if CZStatus == 'SC' and 0<=Age:
        if 0<=Age<=12:
            CDA=int(input('Enter CDA Balance: '))
            p=Child(ID,Name,Age,Gender,CZStatus,CDA)
        elif 13<=Age<=64:
            Medisave=int(input('Enter Medisave Balance: '))
            p=Adult(ID,Name,Age,Gender,CZStatus,Medisave)
        elif 65<=Age:
            p=Senior(ID,Name,Age,Gender,CZStatus)
        plist.append(p)
        print('\n',Name,'is registered successfully.')
    elif CZStatus == 'PR' and 0<=Age:
        if 0<=Age<=12:
            p=Child(ID,Name,Age,Gender,CZStatus,0)
        elif 13<=Age<=64:
            Medisave=int(input('Enter Medisave Balance: '))
            p=Adult(ID,Name,Age,Gender,CZStatus,Medisave)
        elif 65<=Age:
            p=Senior(ID,Name,Age,Gender,CZStatus)
        plist.append(p)
        print('\n',Name,'is registered successfully.')
    elif CZStatus == 'Foreigner' and 0<=Age:
        if 0<=Age<=12:
            p=Child(ID,Name,Age,Gender,CZStatus,0)
        elif 13<=Age<=64:
            p=Adult(ID,Name,Age,Gender,CZStatus,0)
        elif 65<=Age:
            p=Senior(ID,Name,Age,Gender,CZStatus)
        plist.append(p)
        print('\n',Name,'is registered successfully.')
    else:
        print('\n',Name,'is not registered successfully.')

def list_all_patients(plist):
    print('\nOption 2.View All Patients')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))

def list_all_beds(blist):
    print('\nOption 3.View All Beds')
    print('{:4s}\t{:7s}\t{:6s}\t{:2s}\t{:2s}\t{:10s}\t{:10s}'.format(
        'Type','Ward No','Bed No','SC','PR','Foreigner','Available'))
    for each in blist:
        print('{:s}\t{:d}\t{:d}\t{:d}\t{:d}\t{:d}\t\t{}'.format(
                each.bed_type,each.ward_no,each.bed_no,each.sc_cost,each.pr_cost,
                each.foreigner_cost,each.available))
            
def list_all_available_beds(blist):
    print('\nOption 4.View All Available Beds')
    print('{:4s}\t{:7s}\t{:6s}\t{:2s}\t{:2s}\t{:10s}\t{:10s}'.format(
        'Type','Ward No','Bed No','SC','PR','Foreigner','Available'))
    for each in blist:
        if each.available==True:
            print('{:s}\t{:d}\t{:d}\t{:d}\t{:d}\t{:d}\t\t{}'.format(
                each.bed_type,each.ward_no,each.bed_no,each.sc_cost,each.pr_cost,
                each.foreigner_cost,each.available))

def register_hospital_stay(plist,blist):
    print('\nOption 5.Register a hospital stay')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        if each.status == 'Registered':
            print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    fail=True
    for each in plist:
        if each.id==ID:
            fail=False
            p=each
            break
    if fail == False:
        print('\n{:2s}\t{:4s}\t{:7s}\t{:6s}\t{:2s}\t{:2s}\t{:10s}\t{:10s}'.format(
            'No','Type','Ward No','Bed No','SC','PR','Foreigner','Available'))
        for i,each in enumerate(blist):
            if each.available==True:
                print('{:d}\t{:s}\t{:d}\t{:d}\t{:d}\t{:d}\t{:d}\t\t{}'.format(
                    i+1,each.bed_type,each.ward_no,each.bed_no,each.sc_cost,
                    each.pr_cost,each.foreigner_cost,each.available))
        No=int(input('Select bed to stay: '))
        while No > len(blist) or No < 1:
            No=int(input('Invalid bed, Select bed to stay again: '))
        b=bed_list[No-1]
        AdmissionDate=input('Enter date of admission(DD/MM/YYYY): ')
        stay=Stay(AdmissionDate)
        bedstay=BedStay(AdmissionDate,b)
        stay.add_bedstay(bedstay)
        p.add_stay(stay)
        b.available=False
        if isinstance(b,ClassABed):
            accompanying_person=input('Any accompanying guest?(Addtional $100 per day)[Y/N]: ').upper()
            if accompanying_person == 'Y':
                b.accompanying_person=True
        if isinstance(b,ClassBBed):
            air_con=input('Is air-conditionaed variant required?(Additional $50 per day)[Y/N]').upper()
            if air_con == 'Y':
                b.air_con=True
        if isinstance(b,ClassCBed):
            portable_tv=input('Any portable TV required?(Addtional $30 per day)[Y/N]:' ).upper()
            if portable_tv == 'Y':
                b.portable_tv=True
        p.status='Admitted'
        print('\nStay registration successful!')
    else:
        print('\nStay registration not successful!')

def retrieve_patient_details(plist):
    Fail=True
    print('\nOption 6.Retrieve Patient Details')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            Fail=False
            print('\nName of patient:',each.name)
            print('ID number:',each.id)
            print('Citizenship status:',each.citizen_status)
            print('Gender:',each.gender)
            print('Status:',each.status)
            if each.status=='Registered':
                print('\nAdmission date:')
                print('Discharge date:')
                print('Payment status:')
                print('=====')
                print('Ward number:')
                print('Bed number:')
                print('Ward class:')
                print('Start of bed stay:')
                print('End of bed stay:')
            else:
                print('\nAdmission date:',each.stay_list[-1].admitted_date)
                print('Discharge date:',each.stay_list[-1].discharge_date)
                print('Payment status:',each.stay_list[-1].payment_status)
                print('=====')
                print('Ward number:', each.stay_list[-1].bedstay_list[-1].bed.ward_no)
                print('Bed number:', each.stay_list[-1].bedstay_list[-1].bed.bed_no)
                print('Ward class:', each.stay_list[-1].bedstay_list[-1].bed.bed_type)
                print('Start of bed stay:', each.stay_list[-1].bedstay_list[-1].start_bedstay)
                print('End of bed stay:', each.stay_list[-1].bedstay_list[-1].end_bedstay)
    if Fail:
        print('Invalid Patient ID number')


def enter_medical_record(plist):
    fail=True
    from sense_hat import SenseHat
    sense = SenseHat()
    import datetime
    print('\nOption 7.Enter Medical Record Entry')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        if each.status == 'Admitted':
            print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            fail=False
            p=each
            break
    if fail == False:
        temp = sense.get_temperature()
        print('Patient temperature: {:.1f} deg.cel'.format(temp))
        diagnosis=input('Please enter patient observation: ')
        time=str(datetime.datetime.now())
        mrecord=MedicalRecord(diagnosis,temp,time)
        p.stay_list[-1].add_record(mrecord)
        print('\nMedical record entry for {:s} successful!'.format(p.name))
    else:
        print('\nMedical record entry not successful!')


def view_medical_records(plist):
    Fail=True
    print('\nOption 8.View medical records')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            Fail=False
            print('\nName of patient:',each.name)
            print('ID number:',each.id)
            print('Citizenship status:',each.citizen_status)
            print('Gender:',each.gender)
            print('Status:',each.status)
            if each.status=='Admitted':
                print('\nAdmission date:',each.stay_list[-1].admitted_date)
                print('Discharge date:',each.stay_list[-1].discharge_date)
                for i,every in enumerate(each.stay_list):
                    print('\n======Stay # {:d}======='.format(i+1))
                    print('Admission date:',every.admitted_date)
                    for j,anyone in enumerate(every.record_list):
                        print('\n=====Record# {:d}====='.format(j+1))
                        print('Date/Time:',anyone.entry_added)
                        print('Temperature: {:.1f} deg.cel'.format(anyone.temperature))
                        print('Diagnosis:',anyone.diagnosis)
            else:
                print('\nAdmission date:')
                print('Discharge date:')
    if Fail:
        print('Invalid Patient ID number')
        
def monitor_patient(plist):
    fail=True
    import time
    from sense_hat import SenseHat
    sense = SenseHat()
    from Stick import SenseStick
    stick=SenseStick()
    sense.clear()
    d = {
    stick.KEY_UP: 'up',
    stick.KEY_DOWN: 'down',
    stick.KEY_LEFT: 'left',
    stick.KEY_RIGHT: 'right',
    stick.KEY_ENTER: 'push',
    }
    print('\nOption 9.Monitor a Patient')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        if each.status == 'Admitted':
            print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            fail=False
            p=each
            break
    Again = 'Y'
    while Again =='Y' and fail == False:
        print('Current temperature: {:.1f} degree cel.'.format(sense.get_temperature()))
        print("====================================")
        print("Please set threshold with joystick")
        print("====================================")
        temp=30.4
        print('Current threshold: {:.2f} degree cel.'.format(temp))
        for event in stick:
            if event.state ==stick.STATE_PRESS:
                if d[event.key] == 'up':
                    temp+=0.1
                    print('Current threshold: {:.2f} degree cel.'.format(temp))
                elif d[event.key] == 'down':
                    temp-=0.1
                    print('Current threshold: {:.2f} degree cel.'.format(temp))
                elif d[event.key] == 'push':
                    sense.clear()
                    break
        print('New threshold set')
        print('Start monitoring....')
        print('Current Temperature')
        count=0
        no=0
        for i in range(8):
            for j in range(8):
                ctemp=sense.get_temperature()
                print('#{}: {:.2f} deg.cel.'.format(no+1,ctemp))
                if ctemp > temp:
                      sense.set_pixel(i,j,255,0,0)
                      count+=1
                else:
                      sense.set_pixel(i,j,0,255,0)
                time.sleep(0.5)
                no+=1
        print('Number of times threshold({:.2f} deg. cel.) crossed: {}'.format(temp,count))
        Again=input('Do you want to monitor again [Y/N]?').upper()
    if fail:
        print('Invalid Patient ID number')
    elif Again == 'N':
        print('\nMonitoring ended.')
    else:
        print('Invalid input')
        print('\nMonitoring ended.')
    sense.clear()
        
        
        
def transfer_patient(plist,blist):
    fail=True
    print('\nOption 10.Transfer Patient to Another Bed')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        if each.status == 'Admitted':
            print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            fail=False
            p=each
            break
    if fail == False:
        print('\n{:2s}\t{:4s}\t{:7s}\t{:6s}\t{:2s}\t{:2s}\t{:10s}\t{:10s}'.format(
            'No','Type','Ward No','Bed No','SC','PR','Foreigner','Available'))
        for i,each in enumerate(blist):
            if each.available==True:
                print('{:d}\t{:s}\t{:d}\t{:d}\t{:d}\t{:d}\t{:d}\t\t{}'.format(
                    i+1,each.bed_type,each.ward_no,each.bed_no,each.sc_cost,
                    each.pr_cost,each.foreigner_cost,each.available))
        No=int(input('Select bed to stay: '))
        while No > len(blist) or No < 1:
            No=int(input('Invalid bed, Select bed to stay again: '))
        b=bed_list[No-1]
        import datetime
        format = "%d/%m/%Y"
        TransferDate=input('Date of transfer(DD/MM/YYYY): ')
        start=datetime.datetime.strptime(p.stay_list[-1].bedstay_list[-1].start_bedstay,format)
        end=datetime.datetime.strptime(TransferDate,format)
        while (end-start).days <0:
            TransferDate=input('Invalid transfer date.\nDate of transfer(DD/MM/YYYY): ')
            end=datetime.datetime.strptime(TransferDate,format)
        p.stay_list[-1].bedstay_list[-1].end_bedstay=TransferDate
        wardno=p.stay_list[-1].bedstay_list[-1].bed.ward_no
        bedno=p.stay_list[-1].bedstay_list[-1].bed.bed_no
        newbedstay=BedStay(TransferDate,bed_list[No-1])
        p.stay_list[-1].add_bedstay(newbedstay)
        b.available=False
        for each in blist:
            if each.ward_no==wardno and each.bed_no==bedno:
                each.available = True
                break
        if isinstance(b,ClassABed):
            accompanying_person=input('Any accompanying guest?(Addtional $100 per day)[Y/N]: ').upper()
            if accompanying_person == 'Y':
                b.accompanying_person=True
        if isinstance(b,ClassBBed):
            air_con=input('Is air-conditionaed variant required?(Additional $50 per day)[Y/N]').upper()
            if air_con == 'Y':
                b.air_con=True
        if isinstance(b,ClassCBed):
            portable_tv=input('Any portable TV required?(Addtional $30 per day)[Y/N]:' ).upper()
            if portable_tv == 'Y':
                b.portable_tv=True
        print('\n{} will be transferred to Ward {} Bed {} on {}.'.format(
            p.name,b.ward_no,b.bed_no,TransferDate))
    else:
        print('\nTransfer of patient not successful!')


def discharge_patient(plist):
    Fail=True
    print('\nOption 11.Discharge patient')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        if each.status == 'Admitted':
            print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            Fail=False
            import datetime
            format = "%d/%m/%Y"
            DischargeDate=input('Date of discharge(DD/MM/YYYY): ')
            start=datetime.datetime.strptime(each.stay_list[-1].bedstay_list[-1].start_bedstay,format)
            end=datetime.datetime.strptime(DischargeDate,format)
            while (end-start).days <0:
                DischargeDate=input('Invalid discharge date.\nDate of discharge(DD/MM/YYYY): ')
                end=datetime.datetime.strptime(DischargeDate,format)
            each.stay_list[-1].discharge_date=DischargeDate
            each.stay_list[-1].bedstay_list[-1].end_bedstay=DischargeDate
            each.status='Discharged'
            each.stay_list[-1].bedstay_list[-1].bed.available=True
            print('\n',each.name,'is successfully discharged.')
    if Fail:
        print('Invalid Patient ID number')


def view_and_make_payment(plist):
    Fail=True
    print('\nOption 12.View and make payment')
    print('{:10s}\t{:6s}\t\t{:3s}\t{:6s}\t{:12s}\t{:6s}'.format('Name','ID No.','Age','Gender','Citizenship','Status'))
    for each in plist:
        if each.status == 'Discharged':
            print('{:10s}\t{:6s}\t{:d}\t{:6s}\t{:12s}\t{:6s}'.format(each.name,each.id,each.age,each.gender,each.citizen_status,each.status))
    ID=input('Enter Patient ID number: ').upper()
    for each in plist:
        if each.id==ID:
            Fail=False
            each.calculate_charges()
    if Fail:
        print('Invalid Patient ID number')

            
        
patient_list=[]
patient_list.append(Child('S1234567A','Adrian',10,'M','SC',50))
patient_list.append(Child('G1234567A','David',12,'M','PR',0))
patient_list.append(Child('F1234567A','Gabriel',8,'M','Foreigner','0'))

patient_list.append(Adult('S2345678A','Benjamin',35,'M','SC',100))
patient_list.append(Adult('G2345678A','Edda',38,'F','PR',100))
patient_list.append(Adult('F2345678A','Hannah',33,'F','Foreigner',0))

patient_list.append(Senior('S3456789A','Christina',70,'F','SC'))
patient_list.append(Senior('G3456789A','Febe',72,'F','PR'))
patient_list.append(Senior('F3456789A','Ian',66,'M','Foreigner'))


bed_list=[]
bed_list.append(ClassABed(51,1))
bed_list.append(ClassABed(51,2))
bed_list.append(ClassABed(52,1))
bed_list.append(ClassABed(52,2))

bed_list.append(ClassBBed(41,1))
bed_list.append(ClassBBed(41,2))
bed_list.append(ClassBBed(41,3))

bed_list.append(ClassCBed(31,1))
bed_list.append(ClassCBed(31,2))
bed_list.append(ClassCBed(31,3))

menu()
option=int(input('\nEnter your option: '))
while option!=0:
    if option==1:
        registration(patient_list)
    elif option==2:
        list_all_patients(patient_list)
    elif option==3:
        list_all_beds(bed_list)
    elif option==4:
        list_all_available_beds(bed_list)
    elif option==5:
        register_hospital_stay(patient_list,bed_list)
    elif option==6:
        retrieve_patient_details(patient_list)
    elif option==7:
        enter_medical_record(patient_list)
    elif option==8:
        view_medical_records(patient_list)
    elif option==9:
        monitor_patient(patient_list)
    elif option==10:
        transfer_patient(patient_list,bed_list)
    elif option==11:
        discharge_patient(patient_list)
    elif option==12:
        view_and_make_payment(patient_list)
    menu()
    option=int(input('\nEnter your option: '))
'''
import sys
try:
    menu()
    option=int(input('\nEnter your option: '))
    while option!=0:
        if option==1:
            registration(patient_list)
        elif option==2:
            list_all_patients(patient_list)
        elif option==3:
            list_all_beds(bed_list)
        elif option==4:
            list_all_available_beds(bed_list)
        elif option==5:
            register_hospital_stay(patient_list,bed_list)
        elif option==6:
            retrieve_patient_details(patient_list)
        elif option==7:
            enter_medical_record(patient_list)
        elif option==8:
            view_medical_records(patient_list)
        elif option==10:
            transfer_patient(patient_list,bed_list)
        elif option==11:
            discharge_patient(patient_list)
        elif option==12:
            view_and_make_payment(patient_list)
        menu()
        option=int(input('\nEnter your option: '))
except:
    print('Unxepected error:',sys.exc_info()[0])
finally:
    print('Program End')
'''


