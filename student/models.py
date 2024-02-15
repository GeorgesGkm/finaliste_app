from django.db import models
import uuid

# Create your models here.
class StudentModel(models.Model):
    
    P_CHOICES =[
        ("1", "L2 II"),  
        ("2", "L2 CSI"),
        ("3", "LPTA 4 II"),
    ] 
    
    D_CHOICES =[
        ("1", "INFORMATIQUE INDUSTRIELLE "),  
        ("2", "iNFORMATIQUE DE GESTION"),
    ] 
    
    S_CHOICES =[
        ("1", "M"),  
        ("2", "F"),
    ] 
    
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nom = models.CharField(max_length=255)
    postnom = models.CharField(max_length=255)
    sexe = models.CharField(choices = S_CHOICES, max_length=10)
    promotion = models.CharField(choices = P_CHOICES, max_length=10)
    departement = models.CharField(choices = D_CHOICES, max_length=10)
    langage = models.CharField(max_length=255)
    directeur = models.CharField(max_length=255)
    codirecteur = models.CharField(max_length=255)
    sujet = models.TextField()
    problematique = models.TextField()
    date_depot = models.DateField(auto_now=True)

