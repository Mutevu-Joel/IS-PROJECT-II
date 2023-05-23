from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('adminchildview/', views.adminchildview, name='adminchildview'),
    path('childview/', views.childview, name='childview'),
    path('decorator/', views.decorator, name='decorator'),
    path('vaccine_delete/<int:pk>/', views.vaccine_delete, name='vaccine_delete'),
    path('childdelete/<int:pk>/', views.childdelete, name='childdelete'),
    path('childdelete2/<int:pk>/', views.childdelete2, name='childdelete2'),
    path('vaccine_edit/<int:pk>/', views.vaccine_edit, name='vaccine_edit'),
    path('childedit/<int:pk>/', views.childedit, name='childedit'),
    path('parentedit/<int:pk>/', views.parentedit, name='parentedit'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('home/', views.home, name='home'),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
    path('immunization1/<int:pk>/', views.immunization1, name='immunization'),
    path('base/', views.base, name='base'),
    path('staff/', views.staff, name='staff'),
    path('staff_details/<int:pk>/', views.staff_details, name='staff_details'),
    path('vaccine1/', views.vaccine1, name='vaccine'),
    path('clinic/', views.clinic, name='clinic'),
    path('reports/', views.reports, name="reports"),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('childRegistration/', views.childRegistration, name='childRegistration'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
