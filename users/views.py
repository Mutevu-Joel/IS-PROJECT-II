from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from Vaccine.Models import vaccine_id,vaccine_type
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
from .filters import ChildFilter, ParentFilter
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, VaccineForm, ChildForm, ClinicForm
from .models import Child, Immunization, Vaccine,Parent


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been added')
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    items = Vaccine.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff1 = User.objects.all()
    staff_count = staff1.count()
    child = Parent.objects.all()
    child_count = child.count()
    context = {
        'items': items,
        'staff': staff,

        'vaccine': vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,

    }
    return render(request, 'profile/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,

    }
    return render(request, 'profile/profile_update.html', context)
def vaccine_edit(request, pk):
    from .models import Vaccine
    item = Vaccine.objects.get(id=pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            vaccine_type = form.cleaned_data.get('child_registration_no')
            messages.success(request, f'{vaccine_type} has been deleted')
            return redirect('vaccine')
    else:
        form = VaccineForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'users/vaccine_edit.html', context)


def childedit(request, pk):
    from .models import Parent
    item = Parent.objects.get(parent_id=pk)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('childRegistration')
    else:
        form = ChildForm(instance=item)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'users/childedit.html', context)


def parentedit(request, pk):
    from .models import Child
    item = Child.objects.get(child_registration_no=pk)
    if request.method == 'POST':
        form = ClinicForm(request.POST, instance=item)
        if form.is_valid():
            item.save()
            return redirect('reports')
    else:
        form = ClinicForm(instance=item)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'users/childedit2.html', context)


@login_required
def vaccine1(request):
    from .models import Vaccine
    data = Immunization.objects.all()
    items = Vaccine.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Parent.objects.all()
    child_count = child.count()
    # items = vaccine.objects.raw('SELECT * FROM authsysproject_vaccine')
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            vaccine_type = form.cleaned_data.get('vaccine_id')
            messages.success(request, f'{vaccine_type} has been added')
            return redirect('vaccine')
    else:
        form = VaccineForm()
    context = {
        'items': items,
        'form': form,
        'data': data,
        'vaccine': vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,

    }

    return render(request, 'users/vaccine.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'users/home.html')


def adminchildview(request):
    items = Parent.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Parent.objects.all()
    child_count = child.count()

    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(parent_id__icontains=q) | Q(mobile_no__icontains=q))
        data = Child.objects.filter(multiple_q)
    else:
        data = Parent.objects.all()

    context = {
        'items': items,
        'data': data,
        'vaccine': vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,
    }
    return render(request, 'users/adminchildview.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    return render(request, 'users/login.html')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request(request):
    messages.success(request, "You have successfully logged out.")
    return redirect("login")


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def base(request):
    from .models import Vaccine
    from .models import Child
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Parent.objects.all()
    child_count = child.count()

    context = {
        'vaccine': vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,

    }
    return render(request, 'users/base.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staff(request):
    workers = User.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Parent.objects.all()
    child_count = child.count()
    context = {
        'workers': workers,
        'vaccine': vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,

    }
    return render(request, 'users/staff.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def immunization1(request, pk):
    return render(request, 'users/immunization.html')


def staff_details(request, pk):
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    parent = Parent.objects.all()
    child_count = parent.count()
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
        'vaccine': vaccine,

        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,
    }
    return render(request, 'users/staff_details.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def childRegistration(request):
    from .models import Child
    from .models import Vaccine
    items = Parent.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Parent.objects.all()
    child_count = child.count()
    vaccines = Vaccine.objects.filter(vaccine_quantity__gte=1)

    # items = vaccine.objects.raw('SELECT * FROM authsysproject_vaccine')
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            parent = form.cleaned_data.get('parent_id')
            messages.success(request, f'{parent} has been added')
        return redirect('childRegistration')
    else:
        form = ChildForm()
    context = {
        'items': items,
        'form': form,
        'vaccine': vaccine,
        'vaccines': vaccines,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,
        # 'orders': orders,

    }

    return render(request, 'users/childRegistration.html', context)


@login_required
def adminprofile(request):
    return render(request, 'users/adminprofile.html')


def childview(request):
    from .models import Parent
    from .models import Vaccine
    items = Parent.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Parent.objects.all()
    child_count = child.count()
    item = Parent.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(parent_id__icontains=q) | Q(mobile_no__icontains=q))
        item = Parent.objects.filter(multiple_q)
    else:
        item = Parent.objects.all()
    context = {
        'item': item,

        'vaccine': vaccine,

        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,
    }
    return render(request, 'users/childview.html', context)


def decorator(request):
    return render(request, 'users/decorator.html')


def vaccine_delete(request, pk):
    from .models import Vaccine
    item = Vaccine.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('vaccine')
    context = {
        'item': item
    }

    return render(request, 'users/vaccine_delete.html', context)


def childdelete(request, pk):
    from .models import Parent
    item = Parent.objects.get(parent_id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('childRegistration')
    context = {
        'item': item
    }

    return render(request, 'users/childdelete.html', context)

def childdelete2(request, pk):
    from .models import Child
    item = Child.objects.get(child_registration_no=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('reports')
    context = {
        'item': item
    }

    return render(request, 'users/childdelete2.html', context)


def reports(request):
    from .models import Child
    child = Child.objects.all()
    parent = Parent.objects.all()
    myFilter = ChildFilter(request.GET, queryset=child)
    Filter = ParentFilter(request.GET, queryset=parent)
    # immunizations = myFilter.qs

    context = {
        'myFilter': myFilter,
        'child': child,
        'Filter': Filter,
        # 'immunizations':immunizations,
    }
    return render(request, 'users/reports.html', context)

def clinic(request):
    items = Child.objects.all()
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    parent = Parent.objects.all()
    child_count = parent.count()
    # items = vaccine.objects.raw('SELECT * FROM authsysproject_vaccine')
    if request.method == 'POST':
        form = ClinicForm(request.POST)
        if form.is_valid():
            order = form.save()
            parent = form.cleaned_data.get('child_registration_no')
            messages.success(request, f'{parent} has been added')
            product = Vaccine.objects.get(id=order.vaccine_id.pk)
            product.vaccine_quantity = product.vaccine_quantity - 1
            product.save()
            return redirect('childRegistration')

    else:
        form = ClinicForm()
    context = {
        'items': items,
        'form': form,
        'vaccine': vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,


    }

    return render(request, 'users/clinic.html', context)

def pdf_report_create(request):
    child = Child.objects.all()
    myFilter = ChildFilter(request.GET, queryset=child)

    template_path = 'users/reports.html'

    context = {'child': child, 'myFilter': myFilter}

    response = HttpResponse(content_type='myFilter')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




# Create your views here.
