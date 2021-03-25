from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def enregistrerNote(request):
    
    template_name = 'operation/enregistrerNote/enregistrerNote.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    # listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        
        listNote = request.POST.getlist('note')
        if listNote:
            for note_el in listNote:
                # Ici on
                note = Note()
                note.codeNote = note_el
                note.sequence = Sequences.objects.get(pk=request.POST.get('sequence'))
                note.matiere = Matiere.objects.get(pk=request.POST.get('matiere'))
                note.eleve = Eleve.objects.get(pk=request.POST.get('idEleve'))
                # note.is_staff = False
                note.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})
        else:
            error = "Erreur d'enregistrement des note"
            return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'error': error})
    
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})


# @login_required(login_url="/login/")
# def sequenceUpdate(request):
#     """
#     Cette fonction permet de modifier les informations du chef informatique
#     """
#     template_name = 'Paramètre/listSequence/listSequence.html'
#     listSequence = Note.objects.filter(is_active=True)
#     listClasse = Classe.objects.filter(is_active=True)
#     listClasse = Classe.objects.filter(is_active=True)
#     msg = ""
#     error = ""
#     if request.method == 'POST':
#         sequenceQuery = Note.objects.filter(pk=request.POST.get('id'))

#         numero_sequence = request.POST.get('numero_sequence')

#         if sequenceQuery:
#             note = Note.objects.get(pk=request.POST.get('id'))

#             if Note.objects.filter(Q(numero_sequence=numero_sequence) & ~Q(pk=note.id)):
#                 error = "Impossible de modifier le libelle car "+numero_sequence+" est déjà lié à une matière.Veuillez choisir un autre libelle"
#                 return render(request, template_name, {'error': error, 'numero_sequence': numero_sequence, 'listSequence': listSequence})
#             else:
#                 Note.objects.filter(pk=request.POST.get('id')).update(
#                     numero_sequence = numero_sequence,
#                     trimestre = Classe.objects.get(pk=request.POST.get('trimestre'))
#                     trimestre = Classe.objects.get(pk=request.POST.get('trimestre'))
#                 )

#                 msg = "Opération effectuer avec succèss"
#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#     else:
#         return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})


# @login_required(login_url="/login/")
# def sequenceDelete(request):
#     """
#     Cette fonction permet de désactiver et d'activer un chef informatique
#     """
#     template_name = 'Paramètre/listSequence/listSequence.html'
#     listSequence = Note.objects.filter(is_active=True)
#     listClasse = Classe.objects.filter(is_active=True)
#     listClasse = Classe.objects.filter(is_active=True)
#     msg = ""
#     error = ""

#     if request.method == "POST":

#         sequenceQuery = Note.objects.filter(pk=request.POST.get('id'))

#         if sequenceQuery:
#             # activer ou suspendre un chef informatique
#             if request.POST.get('is_active') == 'True':
#                 sequenceQuery.update(is_active=True)
#                 msg = "Opération effectué avec succèss"

#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#             elif request.POST.get('is_active') == 'False':
#                 sequenceQuery.update(is_active=False)
#                 msg = "Opération effectué avec succèss"

#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#         else:
#             error = "Erreur de suppression"
#             return render(request, template_name, {'error': error, 'listSequence': listSequence, 'listClasse': listClasse})
#     else:
#         return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})

