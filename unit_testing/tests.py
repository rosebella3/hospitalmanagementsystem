from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Room, Patient, Bills, LabReport

# Create your tests here.

class RoomModelTest(TestCase):
    def setUp(self):
        Room.objects.create(room_no=12, floor="2A")
    
    def test_text_content(self):
        room = Room.objects.get(id=1)
        expected_object_name = f'{room.room_no}'
        self.assertEqual(expected_object_name, '12')
    
class PatientModelTest(TestCase):
    room_ = Room.objects.get(id=1)
    doc = User.objects.get(id=1)
    def setUp(self):
        User.objects.create(username='test', password='test')
        Room.objects.create(room_no=12, floor="2A")
        Patient.objects.create(social_security='027420489BHF',
        first_name = "Amos",
        last_name = "Bett",
        d_o_b = '1995-03-03',
        gender= 'M',
        contact_no = "098765432",
        reg_date = "2019-03-03",
        doctor = self.doc,
        room = self.room_,
        )
    def test_content(self):
        patient = Patient.objects.get(social_security='027420489BHF')
        expected_object_name = f'{patient.social_security}'
        self.assertEqual(expected_object_name, '027420489BHF')

class BillModelTest(TestCase):
    room_ = Room.objects.get(id=1)
    doc = User.objects.get(id=1)
    def setUp(self):
        User.objects.create(username='test', password='test')
        Room.objects.create(room_no=12, floor="2A")
        Patient.objects.create(social_security='027420489BHF',
        first_name = "Amos",
        last_name = "Bett",
        d_o_b = '1995-03-03',
        gender= 'M',
        contact_no = "098765432",
        reg_date = "2019-03-03",
        doctor = self.doc,
        room = self.room_,
        )
        pat = Patient.objects.get(social_security='027420489BHF')
        Bills.objects.create(date="2017-04-02",
        room_charges = 2000,
        lab_fee = 40000,
        doctor_fee = 7000,
        miscellaneous = 1000,
        patient = pat,
        )

    def test_content(self):
        bill = Bills.objects.get()
        expected_object_name = f'{bill.date}'
        self.assertEqual(expected_object_name, "2017-04-02")

class LabReportModel(TestCase):
    room_ = Room.objects.get(id=1)
    doc = User.objects.get(id=1)
    def setUp(self):
        User.objects.create(username='test', password='test')
        Room.objects.create(room_no=12, floor="2A")
        Patient.objects.create(social_security='027420489BHF',
        first_name = "Amos",
        last_name = "Bett",
        d_o_b = '1995-03-03',
        gender= 'M',
        contact_no = "098765432",
        reg_date = "2019-03-03",
        doctor = self.doc,
        room = self.room_,
        )
        pat = Patient.objects.get(social_security='027420489BHF')
        LabReport.objects.create(
            test_name = 'covid-19',
            patient = pat,
            doctor = self.doc,
            date = '2019-04-01',
            description = 'corona virus test',
            status = 'C'
        )
    
    def test_context(self):
        report = LabReport.objects.get(id=1)
        expected_object_name = f'{report.test_name}'
        self.assertEqual(expected_object_name, 'covid-19')

class HomePageTest(TestCase):

    def test_view_url(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'hrm/dashboard.html')

class PatientTest(TestCase):

    def setUp(self):
        self.room = Room.objects.create(room_no=12, floor='12A')
        self.user = get_user_model().objects.create(
            username='test',
            password='test'
            )
        self.patient = Patient.objects.create(social_security='027420489BHF',
        first_name = "Amos",
        last_name = "Bett",
        d_o_b = '1995-03-03',
        gender= 'M',
        contact_no = "098765432",
        reg_date = "2019-03-03",
        doctor = self.user,
        room = self.room,
        )
        self.bill = Bills.objects.create(
            date = '2019-06-07',
            room_charges ='2000',
            doctor_fee = '3456789999',
            lab_fee = '20022',
            miscellaneous = '5000',
            patient = self.patient
        )
        self.test = LabReport.objects.create(
            test_name = 'covid-19',
            patient = self.patient,
            doctor = self.user,
            date = '2019-04-01',
            description = 'corona virus test',
            status = 'C'
        )
    
    def test_content(self):
        patient = Patient.objects.get(social_security='027420489BHF')
        expected_object_name = f'{patient.social_security}'
        self.assertEqual(expected_object_name, '027420489BHF')


    def test_patient_list_view(self):
        resp = self.client.get(reverse('all_patients'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'hrm/tables.html')
    
    def test_patient_detail_view(self):
        resp = self.client.get(reverse('patient_detail', kwargs={'pk':'027420489BHF'}))
        no_resp = self.client.get('patient/1000000000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertTemplateUsed(resp, 'hrm/patient.html')

    def test_patient_create_view(self):
        resp = self.client.post(reverse('addpatient'),{
            'social_security': '0986545256BUIW',
            'first_name': 'test12',
            'last_name' : 'test13',
            'd_o_b' : '2019-06-07',
            'gender' : 'M',
            'contact_no' : '3456789999',
            'reg_date' : '2019-05-22',
            'doctor' : self.user,
            'room' : self.room,
        })
        self.assertEqual(resp.status_code, 200)

    def test_patient_update_view(self):
        resp = self.client.post(reverse('update_patient', kwargs={'pk':'027420489BHF'}),{
            'first_name': 'test12',
            'last_name' : 'test13',
            'd_o_b' : '2019-06-07',
            'gender' : 'M',
            'contact_no' : '3456789999',
            'reg_date' : '2019-05-22',
            'doctor' : self.user,
            'room' : self.room,
        })
        self.assertEqual(resp.status_code, 200)

    def test_bills_list_view(self):
        resp = self.client.get(reverse('all_bills'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'hrm/listBills.html')
    
    def test_bills_detail_view(self):
        resp = self.client.get(reverse('bill_detail', kwargs={'pk':'1'}))
        no_resp = self.client.get('bill/1000000000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertTemplateUsed(resp, 'hrm/bill.html')

    def test_bill_create_view(self):
        resp = self.client.post(reverse('create_bill'),{
            'date' : '2019-06-07',
            'room_charges': '2000',
            'doctor_fee' : '3456789999',
            'lab_fee' : '20022',
            'miscellaneous' : '5000',
            'patient' : self.patient,
        })
        self.assertEqual(resp.status_code, 200)

    def test_bill_update_view(self):
        resp = self.client.post(reverse('edit_bill' ,kwargs={'pk':'1'}),{
            'date' : '2019-06-07',
            'room_charges': '2000',
            'doctor_fee' : '3456789999',
            'lab_fee' : '20022',
            'miscellaneous' : '5000',
            'patient' : self.patient,
        })
        self.assertEqual(resp.status_code, 200)

    def test_lab_report_list_view(self):
        resp = self.client.get(reverse('all_tests'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'hrm/listTests.html')
    
    def test_lab_report_detail_view(self):
        resp = self.client.get(reverse('test_detail', kwargs={'pk':'1'}))
        no_resp = self.client.get('test/1000000000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertTemplateUsed(resp, 'hrm/lab.html')

    def test_lab_report_create_view(self):
        resp = self.client.post(reverse('request_test'),{
            'test_name' : 'covid-19',
            'patient': self.patient,
            'doctor':self.user,
            'date':'2019-04-01',
            'description':'corona virus test',
            'status':'C'
        })
        self.assertEqual(resp.status_code, 200)

    def test_lab_report_update_view(self):
        resp = self.client.post(reverse('edit_test' ,kwargs={'pk':'1'}),{
            'test_name' : 'covid-19',
            'patient': self.patient,
            'doctor':self.user,
            'date':'2019-04-01',
            'description':'corona virus test',
            'status':'C'
        })
        self.assertEqual(resp.status_code, 200)

    
    





