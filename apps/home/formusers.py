from django import forms
from .models import Users, Entreprise, DmdCredit, Product, Commande, Compte


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        # fields = "__all__"
        exclude = ['dateinsu']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})
        # Accepter uniquement les images


class FormLogin(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['emailu', 'mdpu']


class Formmdp(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['emailu', 'mdpu']


class Formodifie(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['image']


class ForEntreprise(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = "__all__"


class ForDmdCredit(forms.ModelForm):
    class Meta:
        model = DmdCredit
        fields = "__all__"


class ForDmdProduit(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ForDmdComm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
class Formcpt(forms.ModelForm):
    class Meta:
        model = Compte
        fields =["montant"]
