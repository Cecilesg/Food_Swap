import mysql.connector  # mysql-connector-python cf. requirements.txt


def reset():
    # Fill with your own MySQL user name and password
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="insert_your_pasword",)
    # You must create myfoodswap local database in your MySQL
    # We use mysql-connector-python to execute MySQL commands in MySQL
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS myfoodswap")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS myfoodswap")
    mycursor.execute("USE myfoodswap")

    ############################################################################
    #                              Tables Creation                             #
    ############################################################################

    mycursor.execute("CREATE TABLE IF NOT EXISTS Categories("
                     "id_category INT NOT NULL AUTO_INCREMENT,"
                     "name VARCHAR(255),"
                     "PRIMARY KEY (id_category)) ENGINE=InnoDB")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Products("
                     "id_product VARCHAR(255),"
                     "url VARCHAR(255),"
                     "name VARCHAR(255),"
                     "grade ENUM('A','B','C','D','E') NOT NULL,"
                     "category INT,"
                     "store VARCHAR(255),"
                     "image VARCHAR(255),"
                     "PRIMARY KEY (id_product)) ENGINE=InnoDB")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Favorites(product "
                     "VARCHAR(255))")

    ############################################################################
    #                             Tables Modification                          #
    ############################################################################

    mycursor.execute("ALTER TABLE Products "
                     "ADD CONSTRAINT fk_categories FOREIGN KEY (category) \
                     REFERENCES Categories(id_category)")
    mycursor.execute("ALTER TABLE Favorites "
                     "ADD CONSTRAINT fk_products FOREIGN KEY (product) \
                     REFERENCES Products(id_product)")
