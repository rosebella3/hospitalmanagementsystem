from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Room(models.Model):
    room_no = models.IntegerField()
    floor = models.CharField(max_length=30)

    def __str__(self):
        return 'room:{} floor:{}'.format(self.room_no, self.floor)

class Patient(models.Model):
    social_security = models.CharField(max_length=10000000, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    d_o_b = models.DateField()
    choices = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=choices)
    contact_no = models.IntegerField()
    reg_date = models.DateField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_out_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('patient_detail', kwargs={'pk':self.social_security})


class Bills(models.Model):
    date = models.DateField()
    room_charges = models.IntegerField()
    doctor_fee = models.IntegerField()
    lab_fee = models.IntegerField()
    miscellaneous = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('bill_detail', kwargs={'pk':self.id})



class LabReport(models.Model):
    test_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=500)
    choices = (('C', 'Complete'), ('P', 'Pending'))
    status = models.CharField(max_length=1, choices=choices)

    def __str__(self):
        return '{} {}'.format(self.test_name, self.patient)

    def get_absolute_url(self):
        return reverse('test_detail', kwargs={'pk':self.id})
