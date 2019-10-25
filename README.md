# Food_Swap
A program that communicates with the Open Food Facts API and allows users who
want to eat better and be healthier to find replacement foods for the ones
they wish to leave behind.

# Requirements and installations
1. Clone from GitHub = https://github.com/Cecilesg/Food_Swap

2. Launch terminal in local repository Food_Swap

3. In terminal = mysql -u root -p

2. In MySQL = CREATE DATABASE IF NOT EXISTS myfoodswap CHARACTER SET 'utf8';

3. In MySQL = exit;

4. In terminal = pip install -r requirements.txt

5. In text editor open db_set_reset.py and database.py and fill in MySQL
username and password

6. In terminal = python3 food_swap.py

# How the program works:
At first the program will format our MySQL database called myfoodswap, 
contact the API and make the OpenFoodFacts data available by filling in the
database.

In a second time the program will ask the user what they want to consult in 
the database.

Next the program will call up the data chosen only if it fits the 
requirements in place. The amount of data is fixed and readable because of a 
designed layout.

The user must then choose a category of products from the ones they summoned. A 
list of product names will be displayed and user must choose the product they 
wish to swap for a better one.

The program will return a comparable product from the same category with a 
better grade.

The user can decide to save the result or not, start a new search or quit the 
program.
