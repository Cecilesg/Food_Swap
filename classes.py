from math import ceil
import requests

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
        print("\n####################################")
        print(self.id, " - ", end=" ")
        print(self.name, end="      ")
        print("(", self.name_en, ")")
        print("\t Nombre de produits :", self.nb_products, end=" ")
        print("\t Nombre de pages :", self.pages)
        print("\t", self.url)
        print("\n####################################")

    def get_product_api(self, page):
        """Method to retrieve a product page from a category"""
        url = self.url + "/" + str(page) + ".json"
        p = requests.get(url)
        products = p.json()
        return products

    @staticmethod
    def get_categories_api():
        """Method to find categories from the OpenFooFacts API"""
        print("... Patientez ... Votre requête est en cours ...")
        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        categories = r.json()
        nb_categories = categories.get("count")
        print(" {} catégories présentes sur le site.".format(nb_categories))
        # OFF has about 12800 categories. Let's select only a dozen.
        return categories


class Product:
    """Class representing object Product"""

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
        self.best_product()

    def display_product(self):
        """Method that displays product info"""
        print("--------------------------------------------")
        print("Nom : \t", self.name, end="      ")
        # product_name_fr # generic_name # categories
        print("Note : \t", self.grade.upper())
        print("url : \t", self.url)
        print("Code barre : \t", self.bar_code)
        print("Catégorie : \t", self.category)
        print("En vente ici : \t", self.store, end="      ")
        print("Image : ", self.image_url)
        print("--------------------------------------------")

    def best_product(self):
        """Method that presents our product in a better way"""
        if self.grade in ["a", "b", "c", "d", "e"]:
            self.grade = self.grade.upper()
        elif self.grade not in ["A", "B", "C", "D", "E"]:
            print(self.grade)
