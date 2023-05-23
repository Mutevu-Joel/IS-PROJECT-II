from django.contrib.auth.models import User
from django.db import models

# Create your models here.
VACCINE_TYPE = (
    ('BCG', 'BCG'),
    ('OPV ', 'OPV '),
    ('Rotavirus ', 'Rotavirus'),
    ('Pneumo_Conj', 'Pneumo_Conj '),

    ('DTWPHibHepB', 'DTWPHibHepB'),

    ('IPV', 'IPV'),
    ('YF', 'YF'),
    ('Measles', 'Measles '),

    ('HPV', 'HPV'),

)

MODE_OF_ADMISSION = (
    ('oral', 'oral'),
    ('injection', 'injection'),
)

SEX = (
    ('male', 'male'),
    ('female', 'female'),
)

UNDERLYING_CONDITION = (
    ('None', 'None'),
    ('HIV', 'HIV'),
    ('Down Syndrome', 'Down Syndrome'),
    ('Orofacial cleft', 'Orofacial cleft'),
    ('Hemophilia', 'Hemophilia'),
    ('Congenital dislocated hip', 'Congenital dislocated hip'),
    ('Tay-Sachs disease', 'Tay-Sachs disease'),
)

WARD = (
    ('Thange', 'Thange'),
    ('Kikumbulyu South', 'Kikumbulyu South'),
    ('Kikumbulyu North', 'Kikumbulyu North'),
    ('Masongaleni', 'Masongaleni'),
    ('Nguumo', 'Nguumo'),
    ('Mtito Andei', 'Mtito Andei'),
    ('Ivingoni/Nzambani', 'Ivingoni/Nzambani'),
    ('Emali/Mulala', 'Emali/Mulala'),
    ('Makindu', 'Makindu'),
    ('Nguu/Masumba', 'Nguu/Masumba'),

)
DOSE_NO = (
    ('dose I', 'dose I'),
    ('dose II', 'dose II'),
    ('dose III', 'dose III'),

)

CLINIC_NO = (
    ('clinic I', 'clinic I'),
    ('clinic II', 'clinic II'),
    ('clinic III', 'clinic III'),
    ('clinic IV', 'clinic IV'),
    ('clinic V', 'clinic V'),
    ('clinic VI', 'clinic VI'),
    ('clinic VII', 'clinic VII'),
    ('clinic VIII', 'clinic VIII'),
    ('clinic IX', 'clinic IX'),

)


class Parent(models.Model):
    parent_id = models.PositiveIntegerField(primary_key=True, )
    mobile_no = models.PositiveIntegerField(null=True, )
    surname = models.CharField(max_length=12)
    other_name = models.CharField(max_length=12)
    sex = models.CharField(max_length=10, null=True, choices=SEX)
    dob = models.DateTimeField(auto_now_add=False, null=True)
    village = models.CharField(max_length=12)
    ward = models.CharField(max_length=50, null=True, choices=WARD)
    pre_condition = models.CharField(max_length=50, null=True, choices=UNDERLYING_CONDITION)

    def __int__(self):
        return self.parent_id

    class Meta:
        verbose_name_plural = 'Parent'


class Vaccine(models.Model):
    vaccine_id = models.CharField(max_length=50, null=False, default='some_value')
    mode_of_admission = models.CharField(max_length=50, choices=MODE_OF_ADMISSION, null=True)
    batch_no = models.CharField(max_length=50)
    vaccine_quantity = models.PositiveIntegerField()
    expiry_date = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return f'{self.vaccine_id}'


class Child(models.Model):
    child_registration_no = models.CharField(max_length=50, null=False,primary_key=True,default='some_value')
    clinic_no = models.CharField(max_length=50, choices=CLINIC_NO, null=True)
    weight = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE, null=True)
    dose_no = models.CharField(max_length=50, choices=DOSE_NO, null=True)
    comment = models.CharField(max_length=30, null=True)
    immunized_at = models.DateTimeField(auto_now_add=False, null=True)
    return_date = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name_plural = 'Child'

    def save(self):
        account_sid = 'ACef7420809ae8cf102c5c858c1d56c3e1'
        auth_token = 'ab7c7d625c0c94755d63a6df29077604'
        from twilio.rest import Client
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Congratulations!! {self.parent_id.surname} {self.parent_id.other_name} for receiving {self.vaccine_id} {self.dose_no} Batch No. {self.vaccine_id.batch_no} on {self.immunized_at} at the Kibwezi Sub-county Hospital.The next clinic day will be on {self.return_date}.Incase of any queries contact us by dialing 0798466318",
            from_='+12538678758',
            to='+254798466318'
        )
        #return message.sid
        super().save()



    def _str_(self):
        return f'{self.child_registration_no},{self.vaccine_id},{self.parent_id}'


class Staff(models.Model):
    staff_ID = models.PositiveIntegerField()
    Surname = models.CharField(max_length=12)
    Other_name = models.CharField(max_length=12)
    email = models.CharField(max_length=12, null=True)
    DOB = models.DateTimeField()
    Mobile_No = models.PositiveIntegerField()
    Job_description = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)


class Profile(models.Model, ):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    image = models.ImageField(default='default.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.staff.username}-Profile'


class Immunization(models.Model):
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE, null=True)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPE, null=True)
    immunization_description = models.CharField(max_length=12, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vaccine_id}'
