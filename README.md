# Food_Swap
A program that communicates with the OpenFoodFacts API and allows users to find replacement foods for the ones they wish to swap.

# Requirements and installations
1. Clone from GitHub = https://github.com/Cecilesg/Food_Swap

2. Launch terminal in local repository Food_Swap

3. In terminal = pip install -r requirements.txt

4. In text editor open db_set_reset.py and database.py and fill in MySQL
username and password

6. In terminal = python3 food_swap.py

# How the app works:
When the user runs the program, the app will start by asking them to choose
what action to take.

If it is the first time the user runs the program, the app will create and
design the myfoodswap MySQL database. Then it will contact the the OpenFoodFacts
API to request the amount of product categories available.

The user can then decide how many categories they wish to consult and
therefor the app will insert into myfoodswap database a number of products from
these categories as long as they fit the product parameters.

The user will be prompted with a new choice to search within the database
categories for a product they wish to swap with a healthier replacement.

The app algorithm will answer them with the best graded product in the
category of their choice. The user has the choice to insert that product into
their favorites, which is another table of the myfoodswap database.

The user can use their uploaded categories again for another
swap, consult their favorites, or quit or start over.
