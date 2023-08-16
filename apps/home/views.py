# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from datetime import datetime

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

#from .formusers import UsersForm, FormLogin, Formodifie
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from apps.authentication.forms import UsersForm
from apps.home.formusers import FormLogin, Formodifie
from apps.home.models import Users, Product, Entreprise, DmdCredit, Commande, DétailsCommande, Compte, Precommande, \
    Notification, dmdecheance

#from .models import Users, Entreprise, DmdCredit, Product, Commande, DétailsCommande, Precommande, Compte




"""
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
"""


#####Mon code
@csrf_exempt
def index(request):
    #idpro = idpro
   formi = FormLogin()
   return render(request, 'home/login.html', {'form': formi})


def creationUser(request):
    form = UsersForm()

    return render(request, 'home/crercompte.html', {'form': form})


# Creer  utilisateur
@csrf_exempt
def traitercompte(request):
    if request.method == "POST":
        # form = EmployeeForm(request.POST , request.FILES)
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
            form.save()
           # formi = FormLogin()
            # return render(request, 'index.html', {'form': formi})
            #return redirect("/monespace")
            formi = FormLogin()
            return  render(request, 'home/login.html', {'form': formi})
        else:
            form = UsersForm()
            return render(request, 'home/crercompte.html', {'form': form})
    else:
        form = UsersForm()
        return render(request, 'home/crercompte.html', {'form': form})


@csrf_exempt
def connecterUser(request, id):
    userbn = Users.objects.get(emailu=id)
    return render(request, 'home/bienvenue.html', {'userbn': userbn})


@csrf_exempt
def loginin(request):
    if request.method == 'POST':
        email = request.POST['emailu']
        password = request.POST['mdpu']

        try:
            user = Users.objects.get(emailu=email, mdpu=password)
            if user :
                  return render(request, 'home/index.html', {'userlog': user})
            userlog = user
        except Users.DoesNotExist:
            # L'utilisateur n'existe pas
            formi = FormLogin()
            error_message = 'Cet email n\'est pas enregistré.'
            return render(request, 'home/login.html', {'error_message': error_message,'form':formi})
        error_message = 'Mot de passe incorrect. Veuillez réessayer.'
        formi = FormLogin()
    return render(request, 'home/login.html', {'form': formi}, {'error_message': error_message})


### Modification de  profil
@csrf_exempt
def update_user(request, idu):
    userup = Users.objects.get(idu=idu)
    # delattr(userup, 'image')
    formuserup = Formodifie(instance=userup)
    # formuserup= Formodifie()
    return render(request, 'updatepro.html', {'userup': formuserup})


@csrf_exempt
def trateupdate(request):
    userup = Users.objects.get(emailu=request.POST['emailu'])
    if request.method == 'POST':
        emailu = request.POST['emailu']
        nompreu = request.POST['nompreu']
        mdpu = request.POST['mdpu']
        adresseu = request.POST['adresseu']
        entreprise = request.POST['entreprise']
        sectu = request.POST['sectu']
        postu = request.POST['postu']
        # image=request.POST['image']
        # Cganger
        userup.emailu = emailu
        userup.nompreu = nompreu
        userup.mdpu = mdpu
        userup.entreprise = entreprise
        userup.adresseu = adresseu
        userup.sectu = sectu
        userup.postu = postu = emailu
        # userup.image=image
        # sauvegarder
        userup.save()
        return render(request, 'bienvenue.html', {'userlog': userup})

    else:
        form = UsersForm(instance=userup)
        return render(request, 'updatepro.html', {'userup': form})


## Traitemnt mdpoub
def mdpu(request):
    if request.method == 'POST':

        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save(
                request=request,
                from_email=DEFAULT_FROM_EMAIL,
                email_template_name='mdpoub.html',
                subject_template_name='mdpoubsubject.txt',
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()

    return render(request, 'mdpoub.html', {'form': form})


@csrf_exempt
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': 1})


@csrf_exempt
def lstpro(request):
    products = [
        {
            "idpro": 1,
            "mimage": "image1.jpg",
            "price": 10.99,
            "description": "Description du produit 1"
        },
        {
            "idpro": 2,
            "mimage": "image2.jpg",
            "price": 19.99,
            "description": "Description du produit 2"
        },
        {
            "idpro": 3,
            "mimage": "image3.jpg",
            "price": 5.99,
            "description": "Description du produit 3"
        }
    ]
    return render(request, 'product_list.html', {'products': products})

##traitement du panier
@csrf_exempt
def ajouter(request):
    for product in products:
        # Vérifier si l'ID du produit correspond à l'ID recherché
        if product['idpro'] == request.Post['idpro']:
            # Si l'ID correspond, vous pouvez accéder à l'élément ici
            # print(product)
            product_details = product
            return render(request, 'ajouter.html', {'products': product_details})
            # break  # Sortir de la boucle une fois que l'élément est trouvé





@csrf_exempt
def listecredit(request, nom):
    # lst=DmdCredit.objects.get(noment=nom, status=1)
    lst = DmdCredit.objects.filter(noment=nom, status=1)
    # usercre = Users.objects.filter(idu=lst.values('idclt'))
    # usercre = Users.objects.get(idu=lst.idclt)
    return render(request, 'home/listecredit.html', {'usercre': lst, 'noment': nom})


@csrf_exempt
def listenotific(request, nom):
    # lst=DmdCredit.objects.get(noment=nom, status=1)
    lst = DmdCredit.objects.filter(noment=nom, status=0)
    ent=Entreprise.objects.get(nom=nom)
    # usercre = Users.objects.filter(idu=lst.values('idclt'))
    # usercre = Users.objects.get(idu=lst.idclt)
    return render(request, 'home/listenoti.html', {'usercre': lst, 'ent': ent})
@csrf_exempt
def listclient(request, nom):
    lst=DmdCredit.objects.filter(noment=nom, status=0)
    ent=Entreprise.objects.get(nom=nom)
    #lst = Users.objects.filter(entreprise=nom)
    # usercre = Users.objects.filter(idu=lst.values('idclt'))
    # usercre = Users.objects.get(idu=lst.idclt)
    return render(request, 'home/listclient.html', {'usercre': lst, 'ent': ent})


@csrf_exempt
def  lsitedmdcredit(request, nom):
    ent=Entreprise.objects.get(nom=nom)
    lst = DmdCredit.objects.filter(noment=nom, status=0)
    # usercre = Users.objects.filter(idu=lst.values('idclt'))
    # usercre = Users.objects.get(idu=lst.idclt)
    return render(request, 'home/listnotificatentre.html', {'list': lst , "ent":ent})





@csrf_exempt
def voirnotification(request, idclt, iddmd):
    dmdu=DmdCredit.objects.get(iddmd=iddmd)
    userup = Users.objects.get(idu=idclt)
    dmd=DmdCredit.objects.get(iddmd=iddmd)
    ent = Entreprise.objects.get(nom=dmdu.noment)
    return render(request, 'home/voirdmdcredit.html', {'usercre': userup,'dmd':dmd,"ent":ent})

    # return render(request, 'index.html', {'form': formi},{'error_message': error_message})
@csrf_exempt
def validerdmd(request,iddmd):
    dmdu=DmdCredit.objects.get(iddmd=iddmd)
    dmdup= DmdCredit.objects.get(iddmd=iddmd).update(status=1)
    ent=Entreprise.objects.get(nom= dmdu.noment)
    DmdCredit.objects.update_or_create(iddm=iddmd, defaults={'status': 1})

    # b5.name = "New name"
    #>> > b5.save()
    '''
    sta=1
    dmdu.status=sta
    dmdu.noment=dmdup.noment
    dmdu.idclt=dmdup.idclt
    dmdu.nomclt=dmdup.nomclt
    dmdu.idpro=dmdup.idpro
    dmdu.description=dmdup.description
    dmdu.noment=dmdup.noment
    dmdu.dateexpir=dmdup.dateexpir
    dmdu.datedebut=dmdup.datedebut
    dmdu.etatpayer=dmdup.etatpayer
    dmdu.montant=dmdup.montant
    '''
    #dmd=DmdCredit.objects.get(iddmd=iddmd)
    dmdu.save()

    lst = DmdCredit.objects.filter(noment=dmdu.noment, status=0)
    return render(request, 'home/listnotificatentre.html', {'lst': lst, "ent":ent})
    #userup = Users.objects.get(idu=idclt)
    #dmd=DmdCredit.objects.get(iddmd=iddmd)
    #return render(request, 'home/voirdmdcredit.html', {'usercre': userup,'dmd':dmd})

@csrf_exempt
def refuserdmd(request, iddmd):
    dmdu = DmdCredit.objects.get(iddmd=iddmd)
    DmdCredit.objects.get(iddmd=iddmd).delete()
    ent = Entreprise.objects.get(nom=dmdu.noment)
    lst = DmdCredit.objects.filter(noment=dmdu.noment, status=0)
    #dmd.delete()

    #dmd.save()
    return render(request, 'home/listnotificatentre.html', {'list': lst,"ent":ent})

    #userup = Users.objects.get(idu=idclt)
    dmd=DmdCredit.objects.get(iddmd=iddmd)
    #return render(request, 'home/voirdmdcredit.html', {'usercre': userup,'dmd':dmd})



@csrf_exempt
def ajoucom_view(request, lstcom):
    # Divisez la chaîne de caractères en une liste d'éléments
    ma_liste = lstcom.split(',')
    # Créez un nouvel objet Commande en utilisant les éléments de la liste
    nouvelle_commande = Commande(idlct=ma_liste[0], idpro=ma_liste[1], action=ma_liste[2])
    # Sauvegardez l'objet Commande dans la base de données
    nouvelle_commande.save()
    return redirect("")


@csrf_exempt
def traitecommande(request):
    idpro = request.POST['idpro']
    idclt = request.POST['idclt']
    qt = request.POST['qt']
    pro = Product.objects.get(idpro=idpro)
    usercmd = Users.objects.get(idu=idclt)
    # com=Commande()
    commande = Commande(date=datetime.now(), etat=0, total=int(pro.price) * qt, vandor="v9096", idclt=idclt,
                        idpro=idpro, action="direct")
    commande.save()
    details_commande = DétailsCommande.objects.create(
        commande=commande,
        idpro=idpro,
        quantite=qt,
        prix_unitaire=pro.price
    )
    details_commande.save()

    lst = Commande.objects.filter(idclt=idclt)
    return render(request, "affichecomm.html",
                  {"deta": details_commande, "com": commande, "usercmd": usercmd, "lst": lst})


@csrf_exempt
def voirdlt(request, idcom):
    det = DétailsCommande.objects.get(commande_id=idcom)
    com = Commande.objects.get(idcom=det.commande_id)
    user = Users.objects.get(idu=com.idclt)
    pro = Product.objects.get(idpro=com.idpro)
    return render(request, "detailcom.html", {"detcom": det, "com": com, "pro": pro, "user": user})


@csrf_exempt
def voircompte(request, idu):
    ucom = Users.objects.get(idu=idu)
    cpt = Compte.objects.get(idclt=idu)
    return render(request, "affichecompte.html", {"ucom": ucom, "cpt": cpt})


####Gestion des comande


@csrf_exempt
def affichecommande(request, idclt):
    lst = Commande.objects.filter(idclt=idclt)

    user = Users.objects.get(idu=idclt)
    return render(request, "home/ui-tables.html", {"lst": lst, 'userlog': user})


@csrf_exempt
def ajoutproduct(request, idclt):
    products = Product.objects.all()
    user = Users.objects.get(idu=idclt)
    return render(request, 'home/product_list.html', {'products': products, 'userlog': user})


@csrf_exempt
def commande(request, idpro, idclt):
    return render(request, "formqt.html", {"idpro": idpro, "idclt": idclt})


@csrf_exempt
def commande(request, idpro, idclt):
    user = Users.objects.get(idu=idclt)
    return render(request, "home/formqt.html", {"idpro": idpro, "idclt": idclt, 'userlog': user})


@csrf_exempt
def traitecommande(request):
    idpro = request.POST['idpro']
    idclt = request.POST['idclt']
    user = Users.objects.get(idu=idclt)
    qt = request.POST['qt']
    pro = Product.objects.get(idpro=idpro)
    usercmd = Users.objects.get(idu=idclt)
    # com=Commande()
    commande = Commande(date=datetime.now(), etat=0, total=int(pro.price) * qt, vandor="v9096", idclt=idclt,
                        idpro=idpro, action="direct")
    commande.save()
    details_commande = DétailsCommande.objects.create(
        commande=commande,
        idpro=idpro,
        quantite=qt,
        prix_unitaire=pro.price
    )
    details_commande.save()
    lst = Commande.objects.filter(idclt=idclt)
    return render(request, "home/ui-tables.html",
                  {"deta": details_commande, "com": commande, "usercmd": usercmd, "lst": lst, 'userlog': user})


def affichefactures(request, idclt):
    user = Users.objects.get(idu=idclt)
    lst = Commande.objects.filter(idclt=idclt, etat=0)
    # det = DétailsCommande.objects.get(commande_id=idcom)
    # com = Commande.objects.get(idcom=det.commande_id)
    # user = Users.objects.get(idu=com.idclt)
    # pro = Product.objects.get(idpro=com.idpro)
    return render(request, "home/factures.html", {"lstfac": lst, "userlog": user})


def affichenotication(request, idclt):
    user = Users.objects.get(idu=idclt)
    lst = Commande.objects.filter(idclt=idclt, etat=0)
    # det = DétailsCommande.objects.get(commande_id=idcom)
    # com = Commande.objects.get(idcom=det.commande_id)
    # user = Users.objects.get(idu=com.idclt)
    # pro = Product.objects.get(idpro=com.idpro)
    return render(request, "home/listnotificat.html", {"lst": lst, "userlog": user})

    # return render(request, "formqt.html", {"idpro": idpro, "idclt": idclt, 'userlog': user})


#####Fin  gestion des commandes

##Gestion profil

def afficheprofil(request, idu):
    ucom = Users.objects.get(idu=idu)
    # cpt = Compte.objects.get(idclt=idu)
    return render(request, "home/page-user.html", {"userlog": ucom})


##fin gestion profil
##GeStion precommade
def precommande(request, idclt):
    lst = Precommande.objects.filter(idclt=idclt)
    ucom = Users.objects.get(idu=idclt)
    return render(request, "home/afficheprecomm.html", {"userlog": ucom,'lst':lst})
@csrf_exempt
def ajoutproductpre(request, idclt):
    products = Product.objects.all()
    user = Users.objects.get(idu=idclt)
    return render(request, 'home/preproduct_list.html', {'products': products, 'userlog': user})


@csrf_exempt
def ajouprecommande(request, idpro, idclt):
    user = Users.objects.get(idu=idclt)
    return render(request, "home/formnbrjour.html", {"idpro": idpro, "idclt": idclt, 'userlog': user})

@csrf_exempt
def affichecheancepre(request , idclt):
    user = Users.objects.get(idu=idclt)
    lst = Precommande.objects.filter(idclt=idclt)

    return render(request, "home/affichecheancepre.html", {"lst": lst, 'userlog': user})
@csrf_exempt
def affichenotificationpre(request , idclt):
    user = Users.objects.get(idu=idclt)
    lst = Notification.objects.filter(idclt=idclt, typenot="pre")
    return render(request, "home/affichenotificationpre.html", {"lst": lst, 'userlog': user})



@csrf_exempt
def traiteprecommande(request):
    idpro = request.POST['idpro']
    idclt = request.POST['idclt']
    nbrj = request.POST['nbrj']
    pro = Product.objects.get(idpro=idpro)
    usercmd = Users.objects.get(idu=idclt)


    precom = Precommande(idpro=idpro, idclt=idclt, nbrjour=nbrj, prix=pro.price, description=pro.description)
    precom.save()
    lstpre = Precommande.objects.filter(idclt=idclt)
    lst = Precommande.objects.filter(idclt=idclt)
    return render(request, "home/afficheprecomm.html", {"userlog":usercmd,"com": commande, "usercmd": usercmd, "lstpre": lstpre,"lst":lst})

##fin precommande
###afficheecheance
##GESTIOIN DEMANDE  DE  CREDIT



###Fin de  demanade
##python manage.py makemigrations --name changed_my_model home
##GESTION ENTREPRISE
#####Gestion entreprise
@csrf_exempt
def indexentre(request):
    # idpro = idpro
    # formi = FormLogin()
    # return render(request, 'index.html', {'form': formi, 'idpro':idpro})
    return render(request, 'home/indexentre.html')


@csrf_exempt
def loginentre(request):
    if request.method == 'POST':
        noment = request.POST['noment']
        password = request.POST['mdpent']
        try:
            ent = Entreprise.objects.get(nom=noment, mdpent=password)

            return render(request, 'home/bienvenueentre.html', {'ent': ent})
            userlog = user
        except Users.DoesNotExist:
            # L'utilisateur n'existe pas
            error_message = 'Cet email n\'est pas enregistré.'
            return redirect("indexent ")
            # return render(request, 'index.html', {'error_message': error_message})
        error_message = 'Mot de passe incorrect. Veuillez réessayer.'
        # formi = FormLogin()
    return redirect("indexent ")
### gestion des  demandes  credits
@csrf_exempt
def affichenoticationdmd (request , idclt):
    user = Users.objects.get(idu=idclt)
    lst = Notification.objects.filter(idclt=idclt, typenot="cred")
    return render(request, "home/affichenotificationdmd.html", {"lst": lst, 'userlog': user})

@csrf_exempt
def affichecheancedmd(request, iddmd):
    dmd=DmdCredit.objects.get(iddmd=iddmd)
    user = Users.objects.get(idu=dmd.idclt)
    lst = dmdecheance.objects.filter(dmdcre=iddmd)

    return render(request, "home/afficheecheance.html", {"lst": lst, 'dmd':dmd,'userlog': user})
@csrf_exempt
def demandecredit(request, idclt):
    lst = DmdCredit.objects.filter(idclt=idclt)
    ucom = Users.objects.get(idu=idclt)
    return render(request, "home/affichedmdcredit.html", {"userlog": ucom,'lst':lst})
@csrf_exempt
def  ajoutproductpredmd(request, idclt):
    products = Product.objects.all()
    user = Users.objects.get(idu=idclt)
    return render(request, 'home/dmdcreproduct_list.html', {'products': products, 'userlog': user})
def conditiondmc(request, idclt, idpro):
    products = Product.objects.get(idpro=idpro)
    user = Users.objects.get(idu=idclt)
    return render(request, 'home/dmdcreproductcondition.html', {'productdmd': products, 'userlog': user})

@csrf_exempt
def traitedeemnadecrd(request, idpro,idclt):
    products = Product.objects.get(idpro=idpro)
    user = Users.objects.get(idu=idclt)
    "" """

        # Récupérez les données du formulaire
        idclt = request.POST['idclt']
        nomclt = request.POST['nomclt']
        noment = request.POST['noment']
        status = request.POST['status']
        idpro = request.POST['idpro']
        dateexpir = datetime.strptime(request.form['dateexpir'], '%Y-%m-%d')
        debit = float(request.POST['debit'])
        etatpayer = request.POST['etatpayer']
        montant = float(request.POST['montant']
     """

        # Créez un objet DmdCredit avec les valeurs du formulaire
    dmd= DmdCredit(
            idclt=user.idu,
            nomclt=user.nompreu,
            noment=user.entreprise,
            status=0,
            idpro=products.idpro,
            description=products.description,
            dateexpir="2023-08-04 00:00:00+02",
            debit=40.000,
            etatpayer=0,
            montant=products.price
        )



    dmd.save()
    dmdech = dmdecheance.objects.create(
        dmdcre=dmd,
        idclt=user.idu
    )
    dmdech.save()
    lst = DmdCredit.objects.filter(idclt=idclt)
    ucom = Users.objects.get(idu=idclt)
    return render(request, "home/affichedmdcredit.html", {"userlog": ucom, 'lst': lst})
    return render(request, 'home/dmdcreproduct_list.html')


###Deconnexion
def deconnexion(request):
    formi = FormLogin()
    return render(request, 'home/login.html', {'form': formi})































