from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def classeList(request):
    
    template_name = 'Paramètre/listClasse/listClasse.html'
    listClasse = Classe.objects.filter(is_active=True)
    listModule = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        classe = Classe.objects.filter(libelle_classe=request.POST.get('libelle_classe'), is_active=True)
        if not classe:
            # Ici on
            modules = request.POST.getlist('module')
            classe = Classe()
            classe.codeClasse = request.POST.get('codeClasse').lower()
            classe.libelle_classe = request.POST.get('libelle_classe').lower()
            classe.niveau_classe = request.POST.get('niveau_classe')
            # classe.is_staff = False
            classe.save()

            if(modules):
                for module in modules:
                    classe.module.add(Modules.objects.get(pk=module))

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listClasse': listClasse, 'listModule': listModule, 'msg': msg})
        else:
            error = "Ce classe existe déjà"
            return render(request, template_name, {'listClasse': listClasse, 'listModule': listModule, 'error': error, 'codeClasse': request.POST.get('codeClasse'), 'libelle_classe': request.POST.get('libelle_classe'), 'niveau_classe': request.POST.get('niveau_classe')})
    
    else:
        return render(request, template_name, {'listClasse': listClasse, 'listModule': listModule})


@login_required(login_url="/login/")
def classeUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'Paramètre/listClasse/listClasse.html'
    listClasse = Classe.objects.filter(is_active=True)
    listModule = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        classeQuery = Classe.objects.filter(pk=request.POST.get('id'))

        codeClasse = request.POST.get('codeClasse')
        libelle_classe = request.POST.get('libelle_classe')
        niveau_classe = request.POST.get('niveau_classe')

        if classeQuery:
            classe = Classe.objects.get(pk=request.POST.get('id'))
            modules = request.POST.getlist('module')

            if Classe.objects.filter(Q(codeClasse=codeClasse) & ~Q(pk=classe.id)):
                error = "Impossible de modifier le code car: "+codeClasse+" existe déjà. Veuillez choisir un autre code"
                return render(request, template_name, {'error': error, 'codeClasse': codeClasse, 'libelle_classe': libelle_classe, 'niveau_classe': niveau_classe, 'listClasse': listClasse, 'listModule': listModule})
            elif Classe.objects.filter(Q(libelle_classe=libelle_classe) & ~Q(pk=classe.id)):
                error = "Impossible de modifier le libelle car "+libelle_classe+" est déjà lié à une matière.Veuillez choisir un autre libelle"
                return render(request, template_name, {'error': error, 'codeClasse': codeClasse, 'libelle_classe': libelle_classe, 'niveau_classe': niveau_classe, 'listClasse': listClasse, 'listModule': listModule})
            else:
                Classe.objects.filter(pk=request.POST.get('id')).update(
                    codeClasse = codeClasse,
                    libelle_classe = libelle_classe,
                    niveau_classe = niveau_classe
                )
                if modules:
                    for module in modules:
                        classe.module.add(module)

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listClasse': listClasse, 'listModule': listModule})
    else:
        return render(request, template_name, {'listClasse': listClasse, 'listModule': listModule})


@login_required(login_url="/login/")
def classeDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'Paramètre/listClasse/listClasse.html'
    listClasse = Classe.objects.filter(is_active=True)
    listModule = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        classeQuery = Classe.objects.filter(pk=request.POST.get('id'))

        if classeQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                classeQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listClasse': listClasse, 'listModule': listModule})
            elif request.POST.get('is_active') == 'False':
                classeQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listClasse': listClasse, 'listModule': listModule})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listClasse': listClasse, 'listModule': listModule})
    else:
        return render(request, template_name, {'listClasse': listClasse, 'listModule': listModule})

