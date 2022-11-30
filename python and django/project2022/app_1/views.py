from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import KorisnikForm, PredmetiForm, UpisniListForm, KorisnikbezlozinkeForm, NoviUpisniListForm
from .models import Predmeti, Korisnik, UpisniList




def get_subjects(request):
    predmeti =  Predmeti.objects.all()
    return render(request, 'all_subjects.html', {"data":predmeti})


def add_subject(request):
    if request.method == 'GET':
        predmetiForm = PredmetiForm()
        return render(request, 'insert_subject.html', {'form':predmetiForm})
    elif request.method == 'POST':
        predmetiForm = PredmetiForm(request.POST, request.FILES)
        if predmetiForm.is_valid():
            predmetiForm.save()
            return redirect('predmeti')
        else:
            return HttpResponse('ERROR')



def edit_subject(request, predmet_id):           
    subject_by_id = Predmeti.objects.get(id=predmet_id)
    
    if request.method == 'GET':
        data_to_update = PredmetiForm(instance=subject_by_id)
        return render(request, 'edit_subject.html', {'form': data_to_update})
    elif request.method == 'POST':
        data_to_update = PredmetiForm(request.POST, instance=subject_by_id)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect('predmeti')
    else:
        return HttpResponse("Something went wrong!")


def get_students(request):
    studenti =  Korisnik.objects.filter(role='student')
    return render(request, 'all_students.html', {"data":studenti})


def add_student(request):
    if request.method == 'GET':
        korisnikForm = KorisnikForm()
        return render(request, 'insert_student.html', {'form':korisnikForm})
    elif request.method == 'POST':
        korisnikForm = KorisnikForm(request.POST, request.FILES)
        if korisnikForm.is_valid():
            korisnikForm.save()
            return redirect('studenti')
        else:
            return HttpResponse('ERROR')


def edit_student(request, student_id):           
    student_by_id = Korisnik.objects.get(id=student_id)
    
    if request.method == 'GET':
        data_to_update = KorisnikbezlozinkeForm(instance=student_by_id)
        return render(request, 'edit_student.html', {'form': data_to_update})
    elif request.method == 'POST':
        #print(request.POST)
        data_to_update = KorisnikbezlozinkeForm(request.POST, instance=student_by_id)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect('studenti')
    else:
        return HttpResponse("Something went wrong!")



def get_prof(request):
    prof =  Korisnik.objects.filter(role='profesor')
    return render(request, 'all_prof.html', {"data":prof})


def add_prof(request):
    if request.method == 'GET':
        korisnikForm = KorisnikForm()
        return render(request, 'insert_prof.html', {'form':korisnikForm})
    elif request.method == 'POST':
        korisnikForm = KorisnikForm(request.POST, request.FILES)
        if korisnikForm.is_valid():
            korisnikForm.save()
            return redirect('prof')
        else:
            return HttpResponse('ERROR')


def edit_prof(request, prof_id):           
    prof_by_id = Korisnik.objects.get(id=prof_id)
    
    if request.method == 'GET':
        data_to_update = KorisnikbezlozinkeForm(instance=prof_by_id)
        return render(request, 'edit_prof.html', {'form': data_to_update})
    elif request.method == 'POST':
        #print(request.POST)
        data_to_update = KorisnikbezlozinkeForm(request.POST, instance=prof_by_id)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect('prof')
    else:
        return HttpResponse("Something went wrong!")


def popis(request, pred_id):
    upisi = UpisniList.objects.filter(predmet_id=pred_id)
    return render(request, 'popis.html', {"data":upisi})


def upisni_list(request):
    id_user = request.user.id
    data = UpisniList.objects.filter(student_id=id_user)
    return render(request, 'upisni_list.html', {"data":data})


def upisni_list_po_studentu(request, stud_id):
    data=UpisniList.objects.filter(student_id=stud_id)
    return render(request, 'upisni_list_po_studentu.html', {"data":data})


def login_role(request):
    
    if request.user.is_superuser==True:
      return render (request,'izbornik_admin.html')
    elif request.user.role=='profesor':
        return render (request,'izbornik_prof.html')
    elif request.user.role=='student':

        
        prva_godina=UpisniList.objects.filter(student_id=request.user.id).filter(status='pass').values_list('predmet_id', flat=True) 
        print(prva_godina)
        predmeti=Predmeti.objects.filter(sem_red=1).filter(id__in=prva_godina).values_list('id', flat=True) 
        pred=Predmeti.objects.filter(sem_red=2).filter(id__in=predmeti).values_list('id', flat=True)
        neupisano=Predmeti.objects.filter(sem_red=1).exclude(id__in=predmeti).values_list('id', flat=True)

       
        print(pred)
        print(predmeti)
        print(neupisano)


        polozeno = UpisniList.objects.filter(student_id=request.user.id).filter(status='pass')
        upisano = UpisniList.objects.filter(student_id=request.user.id).filter(status='enrolled')
        neupisani_id= UpisniList.objects.filter(student_id=request.user.id).values_list('predmet_id')
        other=Predmeti.objects.exclude(id__in=neupisani_id)
        if request.user.status == 'izv':
            return render(request, 'sem_izv.html', {"pass":polozeno, "enrolled":upisano, "other":other, 'nepolozeno': neupisano}) #poslat tu upisni list
        elif request.user.status == "red":
            return render(request, 'sem_red.html', {"pass":polozeno, "enrolled":upisano, "other":other, 'nepolozeno': neupisano}) #poslat tu upisni list
    else:
        return redirect('login')


def lista_predmeta_po_studentu(request, stud_id):
    user = Korisnik.objects.filter(id=stud_id).first()
    polozeno = UpisniList.objects.filter(student_id=stud_id).filter(status='pass')
    upisano = UpisniList.objects.filter(student_id=stud_id).filter(status='enrolled')
    neupisani_id= UpisniList.objects.filter(student_id=stud_id).values_list('predmet_id')
    other=Predmeti.objects.exclude(id__in=neupisani_id)

    if user.status == 'izv':
        return render(request, 'admin_izv.html', {"pass":polozeno, "enrolled":upisano, "other":other, "stud_id":stud_id}) #poslat tu upisni list
    elif user.status == "red":
        return render(request, 'admin_red.html', {"pass":polozeno, "enrolled":upisano, "other":other, "stud_id":stud_id}) #poslat tu upisni list



def predmeti_po_prof(request):
    id_prof=request.user.id
    data=Predmeti.objects.filter(nositelj_kolegija=id_prof)
    return render(request, 'predmeti_po_prof.html', {"data":data})

def studenti_po_predmetu(request, id_pred):
    data=UpisniList.objects.filter(predmet_id=id_pred)
    return render(request, 'studenti_po_predmetu.html', {"data":data})


def polozeni_pred_po_studentu(request, pred_id):
    data=UpisniList.objects.filter(predmet_id=pred_id).filter(status='pass')
    return render(request, 'polozeni_pred_po_studentu.html', {"data":data})



def add_upisni_list(request):
    if request.method == 'GET':
        upisnilistForm = UpisniListForm()
        return render(request, 'insert_upisni_list.html', {'form':upisnilistForm})
    elif request.method == 'POST':
        upisnilistForm = UpisniListForm(request.POST, request.FILES)
        if upisnilistForm.is_valid():
            upisnilistForm.save()
            return redirect('izbornik') #
        return HttpResponse('ERROR')


def edit_upisni_list(request, pred_id, stud_id):           
    #ul_by_id = UpisniList.objects.filter(predmet_id=pred_id).filter(student_id=stud_id).first()
   
    ime_predmeta=Predmeti.objects.get(id=pred_id)
    ime_stud=Korisnik.objects.get(id=stud_id)
    upisni = UpisniList.objects.filter(predmet_id=pred_id).filter(student_id=stud_id).first()

    print(upisni)


    if request.method == 'GET':
        data_to_update = NoviUpisniListForm(instance=upisni)
        return render(request, 'edit_upisni_list.html', {'form': data_to_update, 'predmet': ime_predmeta, 'student': ime_stud})
    elif request.method == 'POST':
        data_to_update = NoviUpisniListForm(request.POST, instance=upisni)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect("studenti") 

    else:
        return HttpResponse("Something went wrong!")


def upisi_predmet(request, pred_id):
    user = request.user.id
    if request.method == 'GET':
        data = {'student_id':Korisnik.objects.get(pk=user), 'predmet_id':Predmeti.objects.get(id=pred_id), 'status': 'enrolled'} 
        f = UpisniListForm(data)
        if f.is_valid():
            f.save()
            return HttpResponse('predmet je upisan')
        else:
            return HttpResponse('predmet nije upisan')

def upisi_predmet_admin(request, pred_id, stud_id):
    if request.method == 'GET':
        data = {'student_id':Korisnik.objects.get(pk=stud_id), 'predmet_id':Predmeti.objects.get(id=pred_id), 'status': 'enrolled'} 
        f = UpisniListForm(data)
        if f.is_valid():
            f.save()
            return HttpResponse('predmet je upisan')
        else:
            return HttpResponse('predmet nije upisan')

def upisi_kao_pass(request, pred_id, stud_id):
    if request.method == 'GET':
        data = {'student_id':Korisnik.objects.get(pk=stud_id), 'predmet_id':Predmeti.objects.get(id=pred_id), 'status': 'pass'} 
        f = UpisniListForm(data)
        if f.is_valid():
            f.save()
        return HttpResponse('Predmet upisan kao polozen!')
    else:
        return HttpResponse('predmet nije upisan kao polozen')


def prof_pass(request, pred_id, stud_id):
    if request.method == 'GET':
        data = UpisniList.objects.filter(predmet_id=pred_id).filter(student_id=stud_id).update(status='pass')
        return HttpResponse('Predmet upisan kao polozen!')
    else:
        return HttpResponse('predmet nije upisan kao polozen')

def deletion_confirmation(request, pred_id, stud_id):
    if request.method == 'GET':
        return render(request, 'izbrisi_predmet.html', {"pred_id":pred_id, "stud_id":stud_id})
    return HttpResponse('greška')


def delete(request, pred_id, stud_id):
    pred_by_id = UpisniList.objects.filter(predmet_id=pred_id).filter(student_id=stud_id)
    if 'yes' in request.POST:
        pred_by_id.delete()
        return HttpResponse('Successfully deleted!')
    return redirect('izbornik')
    





def zad1(request, stud_id):
    prva_godina=UpisniList.objects.filter(student_id=stud_id).values_list('predmet_id', flat=True) #upisani pred 
    print(prva_godina)
    predmeti=Predmeti.objects.filter(sem_red=1).filter(id__in=prva_godina).values_list('id', flat=True) #upisani na prvom sem
    neupisano=Predmeti.objects.filter(sem_red=1).exclude(id__in=predmeti).values_list('id', flat=True)
    print(predmeti)
    print(neupisano)
    if neupisano!=None:
        return render(request, 'obrana.html', {'form': neupisano})

    #pg=UpisniList


    
def zad2(request):
    ul=UpisniList.objects.all().exclude(student_id=None).values_list('student_id', flat=True)
    print(ul)
    pred_red=Predmeti.objects.filter(sem_red=3).values_list('id', flat=True)
    pred_izv=Predmeti.objects.filter(sem_izv=4).values_list('id', flat=True)
    ul_red=UpisniList.objects.filter(predmet_id__in=pred_red).values_list('student_id', flat=True)
    ucenici=Korisnik.objects.filter(id__in=ul_red).filter(status='red').values_list('username', flat=True)
    print(ul_red)
    print(ucenici)

    ul_izv=UpisniList.objects.filter(predmet_id__in=pred_izv).values_list('student_id', flat=True)
    izvanredni=Korisnik.objects.filter(id__in=ul_izv).filter(status='izv').values_list('username', flat=True)

    return render(request, 'zad2.html', {'red': ucenici, 'izv': izvanredni})

#popis svih studenata na zadnjoj god studija izv na 4 god red na 3 god