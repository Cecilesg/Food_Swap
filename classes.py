from math import ceil
import requests
from termcolor import colored

# It's important to remember that the more we request specifics of a
# product the less probability we have to find matching products for the
# database.

class Category:
    """Class representing object category"""

    def __init__(self, name, nb, en, url, id):
        """Category class builder"""
        self.name = name  # Category name
        self.nb_products = nb  # Number of products in category
        self.name_en = en  # Product name in English
        self.url = url  # Category url
        self.pages = ceil(self.nb_products / 20)  # Pages of pdts in category
        self.id = id  # Category ID

    def display_category(self):
        """Method to display category info in a readable lay out"""
        print(colored("\n#####################################################",
                      'magenta'))
        print(self.id, " - ", end=" ")
        print(self.name, end="      ")
        print("(", self.name_en, ")")
        print("\t Nombre de produits :", self.nb_products, end=" ")
        print("\t Nombre de pages :", self.pages)
        print("\t", self.url)
        print(colored("\n#####################################################",
                      'magenta'))

    def get_product_api(self, page):
        """Method to retrieve a product page from a category"""
        url = self.url + "/" + str(page) + ".json"
        p = requests.get(url)
        products = p.json()
        return products

    @staticmethod
    def get_categories_api():
        """Method to find categories from the OpenFooFacts API"""
        print(colored("\n... Patientez ... Votre requête est en cours ...",
                      'green'))
        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        categories = r.json()
        nb_categories = categories.get("count")
        print(colored("\n{} catégories présentes sur le site.\n",
                      'green').format(nb_categories))
        # OFF has about 12800 categories. Let's select only a dozen.
        return categories


class Product:
    """Class representing object product"""

    instance_counter = 0

    def __init__(self, name, url, grade, id, category, store, image_url):
        """Product class builder"""
        self.name = name  # product_name_fr # generic_name # categories
        self.grade = grade
        self.url = url
        self.bar_code = id
        self.category = category
        self.image_url = image_url
        self.store = store
        self.clean_product()

    def display_product(self):
        """Method that displays product info"""
        print(colored("-------------------------------------------------------",
                      'magenta'))
        print(colored("Nom : \t", 'magenta'), self.name, end="      ")
        # product_name_fr # generic_name # categories
        print(colored("Note : \t", 'magenta'), self.grade.upper())
        print(colored("url : \t", 'magenta'), self.url)
        print(colored("Code barre : \t", 'magenta'), self.bar_code)
        print(colored("Catégorie : \t", 'magenta'), self.category)
        print(colored("En vente ici : \t", 'magenta'), self.store, end="      ")
        print(colored("Image : ", 'magenta'), self.image_url)
        print(colored("-------------------------------------------------------",
                      'magenta'))

    def clean_product(self):
        """Method that presents products with better grade lay out"""
        if self.grade in ["a", "b", "c", "d", "e"]:
            self.grade = self.grade.upper()
        elif self.grade not in ["A", "B", "C", "D", "E"]:
            print(self.grade)
