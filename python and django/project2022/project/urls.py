"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app_1 import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('allsubjects/', views.get_subjects, name='predmeti'),
    path('addsubject/', views.add_subject),
    path('editsubject/<int:predmet_id>', views.edit_subject),

    path('allstudents/', views.get_students, name='studenti'),
    path('editstudent/<int:student_id>', views.edit_student),
    path('addstudent/', views.add_student),

    path('allprof/', views.get_prof, name='prof'),
    path('editprof/<int:prof_id>', views.edit_prof),
    path('addprof/', views.add_prof),


    path('popis/<int:pred_id>', views.popis),
    path('upisnilist/', views.upisni_list),

    path('izbornik/', views.login_role, name='izbornik'),

    path('predmetipoprof/', views.predmeti_po_prof),
    path('studentipopredmetu/<int:id_pred>', views.studenti_po_predmetu),

    path('upisipredmet/<int:pred_id>', views.upisi_predmet),
    path('upisipredmetadmin/<int:pred_id>/<int:stud_id>', views.upisi_predmet_admin),

    path('upisnilistpostudentu/<int:stud_id>', views.upisni_list_po_studentu),

    path('upisikaopass/<int:pred_id>/<int:stud_id>', views.upisi_kao_pass),
    path('prof_pass/<int:pred_id>/<int:stud_id>', views.upisi_kao_pass),

    
    path('polozenipred/<int:pred_id>', views.polozeni_pred_po_studentu),


    path('addupisnilist/', views.add_upisni_list),
    path('editupisnilist/<int:pred_id>/<int:stud_id>', views.edit_upisni_list),

    path('confirm/<int:pred_id>/<int:stud_id>', views.deletion_confirmation, name='confirm'),
    path('delete/<int:pred_id>/<int:stud_id>', views.delete, name='delete'),
    

    path('listapredmetapostudentu/<int:stud_id>', views.lista_predmeta_po_studentu, name='listapredmetapostudentu'),

    path('zad1/<int:stud_id>', views.zad1),
    path('zad2/', views.zad2),


]
