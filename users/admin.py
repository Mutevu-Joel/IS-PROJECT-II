from django.contrib import admin

from .models import Child, Parent
from .models import Profile
from .models import Vaccine


class VaccineAdmin(admin.ModelAdmin):
    list_display = ('vaccine_id', 'mode_of_admission', 'batch_no', 'vaccine_quantity')
    list_filter = ['batch_no', 'mode_of_admission']


# class ImmunizationAdmin(admin.ModelAdmin): list_display = ('vaccine_id','vaccine_type','immunization_description',
# 'date') class ChildAdmin(admin.ModelAdmin): list_display = ('child_registration_no', 'Surname', 'Other_name',
# 'weight','sex','height','DOB','parent_ID','phone_no','ward','Underlying_condition','vaccine_id','vaccine_type',
# 'immunization_description','immunized_at')


admin.site.site_header = 'KSCH'
# Register your models here.
admin.site.register(Vaccine, VaccineAdmin)

admin.site.register(Profile)
admin.site.register(Parent)
# admin.site.register(Immunization,ImmunizationAdmin)

admin.site.register(Child)
