from django.db import models

class Candidat(models.Model):
    nom = models.CharField()
    email = models.EmailField(unique=True)
    competences = models.TextField()
    cv = models.FileField(upload_to='cv/', blank=True)

    def __str__(self):
        return self.nom

class Recruteur(models.Model):
    nom = models.CharField()
    entreprise = models.CharField()
    role = models.CharField()

    def __str__(self):
        return f"{self.nom} ({self.entreprise})"
