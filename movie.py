from logger import *
from art import *
from colorama import Fore, Back, Style


class Movie : 

    def __init



movieList = {}

def clearConsole() : 
    clear = "\n" * 100
    print(clear)

def mainMenuMessage() :
    tprint("MOVIE  LIST ",font="rnd-large")
    print(Fore.GREEN + "Bonjour et bienvenue sur notre liste de films\n\n [1] - Créer et ajouter un film \n [2] - Supprimer un film de la liste \n [3] - Afficher la liste des films ordre alphabetique\n [4]  - Afficher la liste des films détaillée\n [5] - Afficher les genres\n [6] - Recherche de films par genre")
    action = input('Choisissez une action : ')
    actFromMainMenu(action)

def actFromMainMenu(action) : 
    match action :
        case "1" :
            clearConsole()
            nom_film = input("Saisissez le nom du film : ")
            clearConsole()
            genre_film = input("Saisissez le genre du film : ")
            clearConsole()
            is_favorite = input("Est-il favori ? (True / False) : ")
            clearConsole()
            addMovie(createMovie(nom_film, genre_film, is_favorite))
            print('Le film a été ajouté')
            mainMenuMessage()
        case "2" :
            clearConsole()
            nom_film = input("Saisissez le nom du film à supprimer ")
            deleteMovie(nom_film)
            mainMenuMessage()
        case "3" :
            clearConsole()
            print(get_names())
            mainMenuMessage()
        case "4" :
            clearConsole()
            display_all()
            mainMenuMessage()
        case "5" :
            clearConsole()
            get_genres()
            mainMenuMessage()
        case "6" :
            clearConsole()
            searchedgenre = input("Saisissez le genre recherché : ")
            print(get_names_by_genre(searchedgenre))
            mainMenuMessage()
            



def createMovie(nom, genre, favori = False) :
    movie = {
        'nom': nom,
        'genre': genre,
        'favori': favori
    }

    return movie


def addMovie(movie) :
    nom = movie['nom']
    movieList[nom] =  movie['genre'], movie['favori']
    log("Le film " + nom + " a bien été ajouté à la liste")
def deleteMovie(movieName) :
        try :
            log("Le film " + str(movieList[movieName]) + " a bien été supprimé de la liste")
            del movieList[movieName]
        
        except KeyError as e: 
            print (f"{e} : Nous ne pouvons pas supprimer ce film car il n'existe pas ")
            log(f"Le film {e} existe pas et peut pas etre supprime")
def get_names() :
    sortedList = sorted(list(movieList.keys()))
    return sortedList

"""
Affiche tout les films presents dans la liste des films avec leur genre et si ils sont dans la liste des favoris 
"""
def display_all() :
    print("Bienvenue sur notre liste de film ! \n\n ")
    for nom in movieList :
        genre = movieList[nom][0]
        if movieList[nom][1] == True :
            infavoriteString = "est en favori"
        else:
            infavoriteString = "n'est pas en favori"

        print(f'{nom} - est un film de genre {genre} et {infavoriteString}')


"""
Obtenir diverses informations à partir d'un genre
"""
def get_genres() :
    countgenre = 0
    listgenre = []
    for nom in movieList :
        if movieList[nom][0] in listgenre :
            continue
        else :
            listgenre.append(movieList[nom][0])
            print("- " + movieList[nom][0])
            countgenre += 1

    print(f"Un total de {countgenre} genres ") 

"""
Permet de renvoyer tout les films en fonction de leur genre 
ordre alphabetique
"""
def get_names_by_genre(searchedgenre) :
    liste = []
    for nom in movieList :
        if(movieList[nom][0] == searchedgenre) :
            liste.append(nom)
    return sorted(list(liste)) 