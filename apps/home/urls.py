# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import  *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    # The home page
    #path('', views.index, name='home'),
path("",  index, name="indexurlpro"),

    path("login", loginin , name="connecterurnjjl"),
    path("indexentre", indexentre , name="connecterurlgh"),

path("commande/idpro=<int:idpro>&idclt=<int:idclt>", commande , name="connecterurlgghhhjh"),
path("compte/idu=<int:idu>", voircompte , name="connecterurlgghhhjh"),
#path("precommande/idpro=<int:idpro>&idclt=<int:idclt>", precommande , name="connecterurlgghhhjh"),
path("traitecommande", traitecommande , name="connecterurlgghhhjh"),
path("listenoti/nom=<str:nom>", listenotific , name="connecterurrfflgghhhjh"),
path("traitecommande/voirdtl/idcom=<int:idcom>", voirdlt , name="connecterurrfflgghhhjh"),
#path("listcre/voircpt/idclt=<int:idclt>", voircpt , name="connecterurrfflgghhhjh"),
#path("ajoucom/<str:lstcom>", voircpt , name="connecterurrfflgghhhjh"),
    ####gestion des  commandes
path("affichecommande/idclt=<int:idclt>", affichecommande , name="connecteruvhrlgghhhjh"),
path("ajoutcommande/idclt=<int:idclt>", ajoutproduct , name="connecteruvhrlgghhhjh"),
path("commandedirect/idpro=<int:idpro>&idclt=<int:idclt>", commande , name="connecterurlgghhhjh"),
path("affichefactures/idclt=<int:idclt>", affichefactures , name="connecteruvhrlgghhhjh"),
path("affichenotification/idclt=<int:idclt>", affichenotication , name="connecteruvhrlgghhhjh"),


###Fin  gestion des  commandes
    ##Gestion profil
#path("profil/idu=<int:idu>", afficheprofil , name="connecterurlgghhhjh"),

    ##fin gestion profil



    path("bienvent", loginentre, name="connecterurl"),
    #path("",  product_list, name="productlist"),
    #path('', include('product_app.urls')),
    path("crercomptevr", creationUser),
    path("traitecompte",  traitercompte),
    path('updateuu/idu=<int:idu>', update_user , name="updateu"),
    path('ajouter', ajouter, name="updateu"),
    #path('traiteupdate', trateupdate, name="updateutrou"),
    path('updateuu/traiteupdate', trateupdate, name="updateutr"),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
####gestion des  precommandes
path("traiteprecommande", traiteprecommande , name="connecterurlgghhhjh"),
path("afficheecheance/idclt=<int:idclt>", affichecheancepre , name="connecteruvhrlgghhhjh"),
path("affichenotificationpre/idclt=<int:idclt>", affichenotificationpre , name="connecteruvhrlgghhhjh"),

path("afficheprecommande/idclt=<int:idclt>", precommande , name="connecteruvhrlgghhhjh"),
path("ajoutprecommande/idclt=<int:idclt>", ajoutproductpre, name="connecteruvhrlgghhhjh"),
path("precommande/idpro=<int:idpro>&idclt=<int:idclt>", ajouprecommande , name="connecterurlgghhhjh"),
#path("affichefactures/idclt=<int:idclt>", affichefactures , name="connecteruvhrlgghhhjh"),
path("afficheecheancepre/idclt=<int:idclt>", affichecheancepre , name="connecteruvhrlgghhhjh"),
path("affichenotification/idclt=<int:idclt>", affichenotication , name="connecteruvhrlgghhhjh"),


###Fin  gestion des  precommandes
## Gestion de  demende de credit
path("traitedmd/idpro=<int:idpro>&idclt=<int:idclt>", traitedeemnadecrd  , name="connecterurlgghhhjh"),
path("dmdecheance/iddmd=<int:iddmd>", affichecheancedmd , name="connecteruvhrlgghhhjh"),
#path("affichenotificationdmd/idclt=<int:idclt>", affichenotificationdmd, name="connecteruvhrlgghhhjh"),

path("affichedmdcredit/idclt=<int:idclt>", demandecredit , name="connecteruvhrlgghhhjh"),
path("ajoutproduitdmd/idclt=<int:idclt>", ajoutproductpredmd, name="connecteruvhrlgghhhjh"),
path("condition/idpro=<int:idpro>&idclt=<int:idclt>", conditiondmc , name="connecterurlgghhhjh"),
#path("affichefactures/idclt=<int:idclt>", affichefactures , name="connecteruvhrlgghhhjh"),
path("affichenotificationdmd/idclt=<int:idclt>", affichenoticationdmd , name="connecteruvhrlgghhhjh"),

###Fin recharger credit
## Deconnexion
path("deconex", deconnexion , name="connecteruvhrlgghhhjh"),
##Voir profil
path("profil/idu=<int:idu>", afficheprofil , name="connecterurlgghhhjh"),
###Gestion entreorise
path("listcre/nom=<str:nom>", listecredit , name="connecterurlgghhhjh"),
path("client/nom=<str:nom>", listclient , name="connecterurlgghhhjh"),
path("notification/nom=<str:nom>", lsitedmdcredit , name="connecterurlgghhhjh"),
path("voirnotificationent/idclt=<int:idclt>&iddmd=<int:iddmd>", voirnotification  , name="connecterurlgghh"),

path("valider/iddmd=<int:iddmd>", validerdmd ," dyugdgfhf "),
path("refuser/iddmd=<int:iddmd>", refuserdmd  ,"dgdgdgjhbv"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
