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
        listEleve = request.POST.getlist('idEleve')
        compt = 0
        if listNote:
            for note_el in listNote:
                # Ici on
                print(request.POST.get('idEleve'))
                note = Note()
                note.codeNote = note_el
                note.sequence = Sequences.objects.get(pk=request.POST.get('sequence'))
                note.matiere = Matiere.objects.get(pk=request.POST.get('matiere'))
                note.classe_n = Classe.objects.get(pk=request.POST.get('classe'))
                note.eleve = Eleve.objects.get(pk=listEleve[compt])
                # note.is_staff = False
                note.save()
                compt += 1

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})
        else:
            error = "Erreur d'enregistrement des note"
            return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'error': error})
    
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})


@login_required(login_url="/login/")
def noteUpdate(request):
    
    template_name = 'operation/modifierNote/modifierNote.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    # listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        noteQuery = Note.objects.filter(pk=request.POST.get('id'))

        listIdNote = request.POST.getlist('idNote')
        listNote = request.POST.getlist('note')
        compt = 0

        print(compt)

        for note in listIdNote:
            noteQuery = Note.objects.filter(pk=note)

            if noteQuery:
                notee = Note.objects.get(pk=note)

                Note.objects.filter(pk=note).update(
                    codeNote = listNote[compt]
                )

                compt += 1

        msg = "Opération effectuer avec succèss"
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})

@login_required(login_url="/login/")
def showNote(request):
    
    template_name = 'operation/showNote/showNote.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})


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

#         noteQuery = Note.objects.filter(pk=request.POST.get('id'))

#         if noteQuery:
#             # activer ou suspendre un chef informatique
#             if request.POST.get('is_active') == 'True':
#                 noteQuery.update(is_active=True)
#                 msg = "Opération effectué avec succèss"

#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#             elif request.POST.get('is_active') == 'False':
#                 noteQuery.update(is_active=False)
#                 msg = "Opération effectué avec succèss"

#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#         else:
#             error = "Erreur de suppression"
#             return render(request, template_name, {'error': error, 'listSequence': listSequence, 'listClasse': listClasse})
#     else:
#         return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})

