from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik, Predmeti, UpisniList


# Register your models here.
#admin.site.register(Korisnik)

@admin.register(Korisnik)
class KorisnikAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )
        

#admin.site.register(Korisnik, KorisnikAdmin)




class PredmetiAdmin(admin.ModelAdmin):
    fields = ['name', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni', 'nositelj_kolegija']

           


admin.site.register(Predmeti, PredmetiAdmin)

 
class UpisniListAdmin(admin.ModelAdmin):
    fields = ['student_id', 'predmet_id', 'status']

admin.site.register(UpisniList, UpisniListAdmin)






