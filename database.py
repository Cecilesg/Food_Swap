import mysql.connector  # mysql-connector-python cf. Requirement.txt
from config import *

# We define a single class to interact with our database
class Database:
    """A class to interact with myfoodswap database"""

    def __init__(self):
        """Database class builder"""
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # Fill in your user name
            passwd="insert_your_password",  # Fill in your password
            database="myfoodswap",  # Create your local database myfoodswap
        )
        self.mycursor = self.mydb.cursor()

    ############################################################################
    #                            Data Insertion                                #
    ############################################################################

    def set_category(self, category):
        """Method that inserts categories into the database"""
        sql = """INSERT INTO Categories(name) VALUES (%s)"""
        val = (category.name,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def set_product(self, product):
        """Method that adds a product into the database"""
        print("coucou")
        sql = """INSERT INTO Products(id_product, url, name, grade, category, 
                store, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (
            product.bar_code,
            product.url,
            product.name,
            product.grade,
            product.category,
            product.store,
            product.image_url
        )
        print(val)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "fiche produit insérée.")


    def set_favorite(self, product):
        """Method that registers user favorite products in the database"""
        sql = """INSERT INTO Favorites(product)\
                VALUES(%s)"""
        val = (product.bar_code,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    ############################################################################
    #                               Data Selection                             #
    ############################################################################

    def get_all_categories(self):
        """Method that returns all database categories"""
        self.mycursor.execute("SELECT * FROM Categories")
        return self.mycursor.fetchall()

    def display_all_categories(self):
        """Method to display all database categories"""
        list = self.get_all_categories()
        for i in range(len(list)):
            print(list[i][0], ".\t", list[i][1])

    def get_product_from_category(self, id):
        """Method that returns all products from a category based on its id"""
        sql = """SELECT * FROM Products WHERE category = (%s)"""
        val = (id,)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def display_product_from_category(self, id):
        """Method to display all products from any given category"""
        list = self.get_product_from_category(id)
        for i in range(len(list)):
            print(i + 1, ".\t", list[i][2], "(", list[i][3], ")")
        return list

    def get_all_favorites(self):
        """Method that returns all favorites registered in the database"""
        sql = """SELECT * 
                FROM Products 
                INNER JOIN Favorites 
                ON Products.id_product = Favorites.product"""
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def display_all_favorites(self):
        """Method to display all favorite poducts"""
        list = self.get_all_favorites()
        for i in range(len(list)):
            print(i + 1, ".\t", list[i][2], "(", list[i][3], ")")

    def search_swap(self, cat, grade):
        """Method that returns products from category cat with a better grade"""
        sql = """Select *
                From Products
                WHERE category = (%s) AND grade <= (%s)
                ORDER BY grade"""
        val = (cat, grade)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()
