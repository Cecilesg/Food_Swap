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

print("-----------------------------------------------------------------------")
print("1. Création et initialisation de la base de données.")
print("2. Utiliser directement l'application.")
print("0. Quitter le programme.")
print("-----------------------------------------------------------------------")
choice = int(input("\n"))

if choice == 1:
    db_set_reset.reset()
    # We should only call the API on first use
    instance = Database()
    categories = Category.get_categories_api()
    nb_to_display = int(input("Combien de catégories voulez-vous télécharger "
                              "? "))
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
                        products["products"][k].get("product_name", "XXX"),
                        products["products"][k].get("url", "missing url"),
                        products["products"][k].get("nutrition_grade_fr", "E"),
                        products["products"][k].get("id", "Missing "
                                                                "bar_code"), i,
                        products["products"][k].get("stores", "Missing "
                                                             "information"),
                        products["products"][k].get("image_url", "Missing "
                                                                 "information"),
                    )
                    product.display_product()
                    try:
                        print("peanut")
                        instance.set_product(product)
                        total_load += 1
                    except:
                        print("Produit rejeté de la base de données.")
                        pass
                except:
                    print("Produit rejeté pour cause d'informations "
                          "essentielles manquantes.")
    print(
        "\n Ces {} catégories contiennent {} produits, dont {} ont été "
        "analysés et retenus dans la base de données.".format(
            nb_to_display, total_product, total_analysis, total_load)
    )
# If database already exists
else:
    instance = Database()

start_menu = True
while start_menu:
    print("-------------------------------------------------------------------")
    print("1. Afficher les catégories et faire une recherche.")
    print("2. Consulter les favoris sauvegardés.")
    print("0. Quitter le programme.")
    print("-------------------------------------------------------------------")
    choice = int(input())
    if choice == 1:
        instance.display_all_categories()
        choice = int(input("Numéro de la catégorie : \n"))
        list = instance.display_product_from_category(choice)
        choice = int(input("Choisissez un produit : \n"))
        print("--------------------------Votre choix--------------------------")

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
        print("------------------------Votre substitut------------------------")
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
        choice = input("Sauvegardez votre choix dans les favoris ? "
                       "O/N\n").upper()
        if choice == "O":
            instance.set_favorite(swap)
        elif choice == "N":
            pass
        else:
            print("Merci de choisir O ou N à l'aide de votre clavier.")
            pass
    elif choice == 2:
        instance.display_all_favorites()
    elif choice == 0:
        print("Merci et au revoir.")
        start_menu = False
    else:
        print("Merci de choisir 1, 2 ou 0 à l'aide de votre clavier.")
