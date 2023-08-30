from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('new_page/', views.new_page, name='new_page'),
    path('form_page/', views.form_page, name='form_page'),
    path('success/', views.success, name='success'),
    path('home/', views.home, name='home'),
    path('get_Courses/<int:department_id>/', views.get_Courses, name='get_Courses'),

]
