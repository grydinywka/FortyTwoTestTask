from django.db import models
#name, surname, date of birth, bio, contacts
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    biography = models.TextField()
    phone_numb = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
