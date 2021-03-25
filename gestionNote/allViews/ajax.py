from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *
from gestionNote.models import *

@login_required(login_url="/login/")
def select_matiere(request):
    matieres = [];
    classe = Classe.objects.get(pk=request.GET.get('classe'))
    matiere_prof = Professeur.objects.get(professeurUser_id=request.user.id).professeurMatiere.all()

    for m in classe.classeMatiere.all():
        for c in matiere_prof:
            if (m.id == c.id):
                matieres.append(m)

                # matieres.

    return render(request, 'ajax/_choix_matiere.html', {'matieres': matiere_prof})

@login_required(login_url="/login/")
def show_form(request):
    eleve = Eleve.objects.filter(classe_id=request.GET.get('classe'))
    return render(request, 'ajax/_enregistrerNote.html', {'listEleve': eleve, 'sequence': request.GET.get('sequence'), 'classe': request.GET.get('classe'), 'matiere': request.GET.get('matiere')})
