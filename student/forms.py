from django import forms
from .models import StudentModel


class StudentForm(forms.Form):
    P_CHOICES =[
        ("1", "L2 II"),  
        ("2", "L2 CSI"),
        ("3", "LPTA 4 II"),
    ] 
    
    D_CHOICES =[
        ("1", "INFORMATIQUE"),  
        ("2", "GESTION"),
    ] 
    
    S_CHOICES =[
        ("1", "M"),  
        ("2", "F"),
    ] 
    
    nom = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white", 'placeholder':"votre Nom "}))
    postnom = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white", 'placeholder':"votre Postnom "}))
    sexe = forms.ChoiceField(widget=forms.Select(attrs={"class":"block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"}), choices=S_CHOICES)
    promotion = forms.ChoiceField(widget=forms.Select(attrs={"class":"block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"}), choices=P_CHOICES)
    departement = forms.ChoiceField(widget=forms.Select(attrs={"class":"block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"}), choices=D_CHOICES)
    langage = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white", 'placeholder':"Siaisr le langage de programmation "}))
    directeur = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white", 'placeholder':"Veuillez saisir le nom de votre directeur "}))
    codirecteur = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white", 'placeholder':"Veuillez saisir le nom de votre Co directeur"}))
    sujet = forms.CharField(widget=forms.Textarea(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",'rows':"8"}))
    problematique = forms.CharField(widget=forms.Textarea(attrs={'class':"appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",'rows':"8"}))
