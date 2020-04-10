from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from .models import Patient, Bills, LabReport

# Create your views here.

class dash(TemplateView):
    template_name = 'hrm/dashboard.html'

class PatientCreate(CreateView):
    model = Patient
    template_name = 'hrm/addPatient.html'
    fields = ['social_security', 'first_name', 'last_name', 'd_o_b', 'gender', 'contact_no', 'reg_date', 'doctor', 'room', 'check_out_date']

class PatientDetail(DetailView):
    model = Patient
    context_object_name = "patient"
    template_name = "hrm/patient.html"

class RequestTest(CreateView):
    model = LabReport
    template_name = 'hrm/requestTest.html'
    fields = [
        'patient',
        'test_name',
        'description',
        'doctor',
        'date',
        'status',

    ]

class TestDetail(DetailView):
    model = LabReport
    template_name = 'hrm/lab.html'
    context_object_name = 'test'

class UpdateTest(UpdateView):
    model = LabReport
    template_name = 'hrm/updateTest.html'
    fields = [
        'patient',
        'test_name',
        'description',
        'doctor',
        'date',
        'status',

    ]

class CreateUser(CreateView):
    form_class = UserRegistrationForm
    model = User
    template_name = 'hrm/createuser.html'

class UserDetail(DetailView):
    model = User
    template_name = 'hrm/user.html'
    context_object_name = 'user'

class UpdateUser(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'hrm/updateuser.html'
    success_url = reverse_lazy('all_users')


class CreateBill(CreateView):
    model = Bills
    template_name = 'hrm/createBill.html'
    fields = [
        'date',
        'room_charges',
        'doctor_fee',
        'lab_fee',
        'miscellaneous',
        'patient',

    ]

class BillDetail(DetailView):
    model = Bills
    template_name = 'hrm/bill.html'
    context_object_name = 'bill'

class EditBill(UpdateView):
    model = Bills
    template_name = 'hrm/editBill.html'
    fields = [
        'date',
        'room_charges',
        'doctor_fee',
        'lab_fee',
        'miscellaneous',
        'patient',

    ]

class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'hrm/updatePatient.html'
    fields = ['social_security', 'first_name', 'last_name', 'd_o_b', 'gender', 'contact_no', 'reg_date', 'doctor', 'room']

class PatientListView(ListView):
    model = Patient
    template_name = 'hrm/tables.html'
    context_object_name = 'Patients'

class UsersListView(ListView):
    model = User
    template_name = 'hrm/allusers.html'
    context_object_name = 'users'

class BillListView(ListView):
    model = Bills
    template_name = 'hrm/listBills.html'
    context_object_name = 'bills'

class TestListView(ListView):
    model = LabReport
    template_name = 'hrm/listTests.html'
    context_object_name = 'tests'
