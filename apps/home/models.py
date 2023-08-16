# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.
class Users(models.Model):
    entreprise1 = "ccbm"
    entreprise2 = "orbit"
    ROLE_CHOICES = (
        (entreprise1, 'ccbm'),
        (entreprise2, 'orbit'),
    )

    idu = models.BigAutoField(primary_key=True)
    nompreu = models.CharField(max_length=100, null=True, verbose_name="Votre  Nom")
    emailu = models.EmailField(null=True, verbose_name=" Votre Email", unique=True)
    teleu = models.CharField(max_length=15, null=True, verbose_name="Votre Télephone")
    mdpu = models.CharField(max_length=128, null=True, verbose_name="Votre  Mot de Passe")
    # entreu = models.CharField(max_length=128,null=True)
    entreprise = models.CharField(max_length=30, choices=ROLE_CHOICES)
    postu = models.CharField(max_length=128, null=True, verbose_name="Poste")
    sectu = models.CharField(max_length=128, null=True, verbose_name="Secteur")
    adresseu = models.CharField(max_length=15, null=True, verbose_name="Votre Adresse")
    dateinsu = models.DateTimeField("date creation", null=True, default=datetime.now)
    # image = models.CharField(max_length=128, null=True)
    image = models.FileField(upload_to="photos",  verbose_name="Profil")

    class Meta:
        db_table = "orbituser"

    # Create your models here.
    def __str__(self):
        return str(self.dateinsu)




class Entreprise(models.Model):
    ident = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mdpent = models.CharField(max_length=255)
    class Meta:
        db_table = "orbitentreprise"

    def __str__(self):
        return self.nom




class DmdCredit(models.Model):
    iddmd = models.AutoField(primary_key=True)
    idclt = models.IntegerField(default=1)
    nomclt = models.CharField(max_length=255,null=True)
    noment = models.CharField(max_length=255 , null=True)
    status = models.IntegerField(default=0)
    idpro = models.IntegerField()
    datedebut = models.DateTimeField("date creation", null=True, default=datetime.now)
    dateexpir= models.DateTimeField("date creation", null=True)
    debit = models.DecimalField(max_digits=100, decimal_places=5,null=True)
    etatpayer = models.IntegerField(default=0)
    montant= models.DecimalField(max_digits=100, decimal_places=5,null=True)
    description = models.TextField(null=True,default="Hisen Frigo")
    class Meta:
        db_table = 'orbitdmdcredit'
class dmdecheance(models.Model):
    iddmdech = models.AutoField(primary_key=True)
    dmdcre = models.ForeignKey(DmdCredit, related_name='echeance', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    etatpayer = models.IntegerField(default=0)
    idclt = models.IntegerField(default=1)
    class Meta:
        db_table = 'orbitdmdecheance'
class Product(models.Model):
    idpro = models.AutoField(primary_key=True)
    mimage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    class Meta:
        db_table = 'ordbitproduct'
class Commande(models.Model):
    idcom = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now)
    etat=models.IntegerField(default=0)
    total=models.DecimalField(max_digits=100, decimal_places=5,null=True)
    vandor=models.CharField(default="v9096", max_length=200)
    idclt = models.IntegerField(null=False)
    idpro = models.IntegerField(null=False)
    action = models.CharField(max_length=100, default='direct')
    # Ajoutez d'autres champs spécifiques à votre modèle
    class Meta:
        db_table = 'orbitcommande'
class DétailsCommande(models.Model):
    idet=models.AutoField(primary_key=True)
    commande = models.ForeignKey(Commande, related_name='details', on_delete=models.CASCADE)
    idpro = models.IntegerField(null=False)
    quantite= models.IntegerField( null=False)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs spécifiques à votre modèle DétailsCommande
    class Meta:
         db_table = 'orbitdetailcom'
class Precommande(models.Model):
    idprecom = models.AutoField(primary_key=True)
    idpro = models.IntegerField(null=False)
    idclt = models.IntegerField(null=False)
    date = models.DateTimeField(default=datetime.now)
    nbrjour=models.IntegerField(default=30)
    etat = models.IntegerField(default=0)
    prix = models.DecimalField(max_digits=10, decimal_places=2 , default=10.20)
    description = models.TextField(null=False, default="description du  produit")
    class Meta:
         db_table = 'orbitprecommande'
class Compte(models.Model):
    idpcompt= models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=100, decimal_places=2, default=00.00)
    idclt = models.IntegerField(null=False)
    etat = models.IntegerField(default=0)
    class Meta:
         db_table = 'orbitcompte'
class Notification(models.Model):
    idnot = models.AutoField(primary_key=True)
    etat = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    typenot = models.CharField(max_length=100, default='direct')
    idclt = models.IntegerField(null=False ,default="1")
    message = models.TextField()
    class Meta:
        db_table = 'ordbitnotification'




#python manage.py makemigrations --name changed_my_model  home









