from database import *
from classes import *
import db_set_reset
from termcolor import colored


# Constants
LIMIT_PAGES = 6
base_url = "https://fr.openfoodfacts.org/categorie/"  # Add produit/i.json
product_nb = LIMIT_PAGES
total_product = 0
total_load = 0
total_analysis = 0

print(colored("---------------------------------------------------------------",
              'blue'))
print(colored("1. Création et initialisation de la base de données.", 'blue'))
print(colored("2. Utiliser directement l'application.", 'blue'))
print(colored("0. Quitter le programme.", 'blue'))
print(colored("---------------------------------------------------------------",
              'blue'))
choice = int(input(colored("\n ----> ", 'blue')))

menu = True
if choice == 1:
    db_set_reset.reset()
    # We should only call the API on first use
    instance = Database()
    categories = Category.get_categories_api()
    nb_to_display = int(input(colored("Combien de catégories voulez-vous "
                                      "télécharger ? ", 'magenta')))
    # We start with the number of products per category
    for i in range(1, nb_to_display + 1):
        category = Category(
            categories["tags"][i].get("name"),
            categories["tags"][i].get("products"),
            categories["tags"][i].get("id"),
            categories["tags"][i].get("url"),
            i,
        )
        category.display_category()
        total_product += category.nb_products
        instance.set_category(category)
        for page in range(1, product_nb + 1):
            products = category.get_product_api(page)
            for k in range(20):  # Beware this doesn't work on last page
                total_analysis += 1
                try:
                    product = Product(
                        products["products"][k].get("product_name", colored(
                            "XXX", 'red')),
                        products["products"][k].get("url", colored(
                            "Missing url", 'red')),
                        products["products"][k].get("nutrition_grade_fr", "E"),
                        products["products"][k].get("id", colored(
                            "Missing bar_code", 'red')), i,
                        products["products"][k].get("stores", colored(
                            "Missing information", 'red')),
                        products["products"][k].get("image_url", colored(
                            "Missing information", 'red')),
                    )
                    product.display_product()
                    try:
                        instance.set_product(product)
                        total_load += 1
                    except:
                        print(colored("Produit rejeté de la base de données.",
                                      'red'))
                except:
                    print(colored("Produit rejeté pour cause d'informations "
                          "essentielles manquantes.", 'red'))
    print(
        colored("\nCes {} catégories contiennent {} produits, dont {} ont été "
                "analysés et retenus dans la base de données.".format(
                 nb_to_display, total_product, total_analysis, total_load),
                'green')
    )
elif choice == 0:
    menu = False

# If database already exists
instance = Database()
start_menu = True
while start_menu and menu:
    print(colored("-----------------------------------------------------------",
                  'blue'))
    print(colored("1. Afficher les catégories et faire une recherche.", 'blue'))
    print(colored("2. Consulter les favoris sauvegardés.", 'blue'))
    print(colored("0. Quitter le programme.", 'blue'))
    print(colored("-----------------------------------------------------------",
                  'blue'))
    choice = int(input(colored("\n ----> ", 'blue')))
    if choice == 1:
        instance.display_all_categories()
        choice = int(input(colored("\nNuméro de la catégorie : \n ----> ",
                                   'magenta')))
        list = instance.display_product_from_category(choice)
        choice = int(input(colored("\nChoisissez un produit : \n ----> ",
                                   'magenta')))
        print(colored("\n"
                      "----------------------Votre choix----------------------",
                      'green'))

        product = Product(
            list[choice - 1][2],
            list[choice - 1][1],
            list[choice - 1][3],
            list[choice - 1][0],
            list[choice - 1][4],
            list[choice - 1][5],
            list[choice - 1][6],
        )
        product.display_product()
        print(colored("\n"
                      "--------------------Votre substitut--------------------",
                      'green'))
        list = instance.search_swap(product.category, product.grade)
        swap = Product(
            list[0][2],
            list[0][1],
            list[0][3],
            list[0][0],
            list[0][4],
            list[0][5],
            list[0][6],
        )
        swap.display_product()
        choice = input(colored("\nSauvegardez votre choix dans les favoris ? "
                       "O/N\n ", 'green')).upper()
        if choice == "O":
            instance.set_favorite(swap)
        elif choice == "N":
            pass
        else:
            print(colored("\nC'est la mauvaise réponse, vous recommencez.",
                          'yellow'))
            pass
    elif choice == 2:
        instance.display_all_favorites()
    elif choice == 0:
        print(colored("\nMerci et au revoir.", 'magenta'))
        start_menu = False
    else:
        print(colored("\nMerci de choisir 1, 2 ou 0 à l'aide de votre clavier.",
                      'yellow'))

print(colored("\nVous quittez le programme.", 'magenta'))
