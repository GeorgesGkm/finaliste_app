from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import StudentModel
from .forms import StudentForm

def home(request, *args, **kwargs):
    context={}
    return render(request, 'home.html', context)


def save_student_form(form):
    if form.is_valid():
        data = form.cleaned_data 
        StudentModel.objects.create(
            nom=data['nom'],
            postnom=data['postnom'],
            sexe=data['sexe'],
            promotion=data['promotion'],
            departement=data['departement'],
            langage=data['langage'],
            directeur=data['directeur'],
            codirecteur=data['codirecteur'],
            sujet=data['sujet'],
            problematique=data['problematique']
        )

@csrf_exempt
def index(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            save_student_form(form)
            return redirect('depots')  # Redirigez l'utilisateur vers une autre vue après l'enregistrement
    else:
        form = StudentForm()
    context['form'] = form
    return render(request, 'forms.html', context)

