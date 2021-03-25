from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def matiereList(request):
    
    template_name = 'Paramètre/listMatière/listMatiere.html'
    listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        matiere = Matiere.objects.filter(nom_Matiere=request.POST.get('nom_Matiere'), is_active=True)
        if not matiere:
            # Ici on
            matiere = Matiere()
            matiere.codeMatiere = request.POST.get('codeMatiere').lower()
            matiere.nom_Matiere = request.POST.get('nom_Matiere').lower()
            # matiere.is_staff = False
            matiere.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listMatiere': listMatiere, 'msg': msg})
        else:
            error = "Cette matière existe déjà"
            return render(request, template_name, {'listMatiere': listMatiere, 'error': error, 'codeMatiere': request.POST.get('codeMatiere'), 'nom_Matiere': request.POST.get('nom_Matiere')})
    
    else:
        return render(request, template_name, {'listMatiere': listMatiere})


@login_required(login_url="/login/")
def matiereUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'Paramètre/listMatière/listMatiere.html'
    listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        matiereQuery = Matiere.objects.filter(pk=request.POST.get('id'))

        codeMatiere = request.POST.get('codeMatiere')
        nom_Matiere = request.POST.get('nom_Matiere')

        if matiereQuery:
            matiere = Matiere.objects.get(pk=request.POST.get('id'))

            if Matiere.objects.filter(Q(codeMatiere=codeMatiere) & ~Q(pk=matiere.id)):
                error = "Impossible de modifier le code car: "+codeMatiere+" existe déjà. Veuillez choisir un autre code"
                return render(request, template_name, {'error': error, 'codeMatiere': codeMatiere, 'nom_Matiere': nom_Matiere, 'listMatiere': listMatiere})
            elif Matiere.objects.filter(Q(nom_Matiere=nom_Matiere) & ~Q(pk=matiere.id)):
                error = "Impossible de modifier le libelle car "+nom_Matiere+" est déjà lié à une matière.Veuillez choisir un autre nom"
                return render(request, template_name, {'error': error, 'codeMatiere': codeMatiere, 'nom_Matiere': nom_Matiere, 'listMatiere': listMatiere})
            else:
                Matiere.objects.filter(pk=request.POST.get('id')).update(
                    codeMatiere = codeMatiere,
                    nom_Matiere = nom_Matiere
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listMatiere': listMatiere})
    else:
        return render(request, template_name, {'listMatiere': listMatiere})


@login_required(login_url="/login/")
def matiereDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'Paramètre/listMatière/listMatiere.html'
    listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        matiereQuery = Matiere.objects.filter(pk=request.POST.get('id'))

        if matiereQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                matiereQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listMatiere': listMatiere})
            elif request.POST.get('is_active') == 'False':
                matiereQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listMatiere': listMatiere})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listMatiere': listMatiere})
    else:
        return render(request, template_name, {'listMatiere': listMatiere})

