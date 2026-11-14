from menu import Menu
resturant01_menu = Menu()
resturnat02_menu = Menu()
resturant01_menu.add_dishes([['Burger', 100], ['Pizza', 200], ['Cake', 300]])
resturnat02_menu.add_dishes([['Rice', 500], ['Chicken', 600], ['Coke', 700]])

from resturant import Resturant, ResturantManager
resturnat01 = Resturant('res_01', 'resturant_01', 'res1_loc', resturant01_menu)
resturnat02 = Resturant('res_02', 'resturant_02', 'res2_loc', resturnat02_menu)
resturnat_manager = ResturantManager()
resturnat_manager.add_resturants(resturnat01)