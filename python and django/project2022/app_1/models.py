from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Korisnik(AbstractUser):
    ROLES = (('profesor', 'profesor'), ('student', 'student'))
    STATUS = (('none', 'None'), ('izv', 'izvanredni student'), ('red', 'redovni student'))
    role = models.CharField(max_length=50, choices=ROLES)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
       return '%s' % (self.username)#, self.email, self.status)


class Predmeti(models.Model):
    IZBORNI = (('da', 'da'), ('ne', 'ne'))
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.CharField(max_length=50, choices=IZBORNI)
    nositelj_kolegija = models.ForeignKey(Korisnik, on_delete=models.CASCADE, blank=True, null=True, related_name = 'nositelj_kolegija')

    def __str__(self):
       return '%s %s %s %s %s %s %s %s' % (self.name, self.kod, self.program, self.ects, self.sem_red, self.sem_izv, self.izborni, self.nositelj_kolegija)



class UpisniList(models.Model):
    student_id = models.ForeignKey(Korisnik, on_delete=models.CASCADE, blank=True, null=True, related_name='student')
    predmet_id = models.ForeignKey(Predmeti, on_delete=models.CASCADE, blank=True, null=True, related_name='predmeti')
    STATUS = (('pass', 'pass'), ('enrolled', 'enrolled'))
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return '%s %s %s' % ( self.student_id, self.predmet_id, self.status ) #self.Korisnik.username,







