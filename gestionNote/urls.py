
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from gestionNote.allViews import *

urlpatterns = [
    path('login/', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name='logout'),
    path('acceuil/', views.show_home, name="accueil"),

    # ajax url
    url(r'^matiere/choix/ajax/', ajax.select_matiere, name='select_matiere'),
    url(r'^note/show_form/ajax/', ajax.show_form, name='show_form'),

    # chefInformatique url
    path('listChefInformatique', chefInformatiqueView.chefInformatiqueList, name="listChefInfo"),
    path('updateChefInformatique', chefInformatiqueView.chefInformatiqueUpdate, name="updateChefInfo"),
    path('deleteChefInformatique', chefInformatiqueView.chefInformatiqueDelete, name="deleteChefInfo"),

    # professeur url
    path('listProfesseur', professeurView.listProfesseur, name="listProfesseur"),
    path('updateProfesseur', professeurView.professeurUpdate, name="updateProfesseur"),
    path('deleteProfesseur', professeurView.professeurDelete, name="deleteProfesseur"),

    # principal url
    path('listPrincipal', principalView.principalList, name="listPrincipal"),
    path('updatePrincipal', principalView.principalUpdate, name="updatePrincipal"),
    path('deletePrincipal', principalView.principalDelete, name="deletePrincipal"),

    # parent url
    path('listParent', parentView.parentList, name="listParent"),
    path('updateParent', parentView.parentUpdate, name="updateParent"),
    path('deleteParent', parentView.parentDelete, name="deleteParent"),

    # Eleve url
    path('listEleve', eleveView.eleveList, name="listEleve"),
    path('updateEleve', eleveView.eleveUpdate, name="updateEleve"),
    path('deleteEleve', eleveView.eleveDelete, name="deleteEleve"),

    # Matière url
    path('listMatiere', matiereView.matiereList, name="listMatiere"),
    path('updateMatiere', matiereView.matiereUpdate, name="updateMatiere"),
    path('deleteMatiere', matiereView.matiereDelete, name="deleteMatiere"),

    # Module url
    path('listModule', moduleView.moduleList, name="listModule"),
    path('updateModule', moduleView.moduleUpdate, name="updateModule"),
    path('deleteModule', moduleView.moduleDelete, name="deleteModule"),

    # Classe url
    path('listClasse', classeView.classeList, name="listClasse"),
    path('updateClasse', classeView.classeUpdate, name="updateClasse"),
    path('deleteClasse', classeView.classeDelete, name="deleteClasse"),

    # Specialite url
    path('listSpecialite', specialiteView.specialiteList, name="listSpecialite"),
    path('updateSpecialite', specialiteView.specialiteUpdate, name="updateSpecialite"),
    path('deleteSpecialite', specialiteView.specialiteDelete, name="deleteSpecialite"),

    # trimestre url
    path('listTrimestre', trimestreView.trimestreList, name="listTrimestre"),
    path('updateTrimestre', trimestreView.trimestreUpdate, name="updateTrimestre"),
    path('deleteTrimestre', trimestreView.trimestreDelete, name="deleteTrimestre"),

    # sequence url
    path('listSequence', sequenceView.sequenceList, name="listSequence"),
    path('updateSequence', sequenceView.sequenceUpdate, name="updateSequence"),
    path('deleteSequence', sequenceView.sequenceDelete, name="deleteSequence"),

    # Note url
    path('EnregistrerNote', noteView.enregistrerNote, name="enregistrerNote")
]