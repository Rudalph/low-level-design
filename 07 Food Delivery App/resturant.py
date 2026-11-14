import threading

class Resturant:
    def __init__(self, res_id, res_name, res_loc, menu):
        self.res_id = res_id
        self.res_name = res_name
        self.res_loc = res_loc
        self.menu = menu
    
    def get_resturant_details(self):
        return {
            'Resturant Id' : self.res_id,
            'Resturant Name' : self.res_name,
            'Resturant Location' : self.res_loc,
            'Menu' : self.menu
        }
        
class ResturantManager:
    __instance = None
    __lock = threading.Lock()
    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)
                    return cls.__instance
        return cls.__instance
            
    def __init__(self):
        self.all_resturants = []
        
    def add_resturants(self, Resturant):
        self.all_resturants.append(Resturant)
    
    def remove_resturant(self, Resturant):
        if Resturant in self.all_resturants:
            self.all_resturants.remove(Resturant)
        