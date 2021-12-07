from player import Player

class Node : 

    def __init__(self, name=None, number=None) -> None:
        """
            Define attributes for the nodes : x/y position, outgoing links to other nodes
        """
        self.__PLAYER = Player(name, number)
        self.__X_POS = None
        self.__Y_POS = None
        self.__outgoing_links = [] #thinking that this will be a list of dictionaries, {'node_obj':obj, 'strength': euclidean_dist}

    def set_x_pos(self, x):
        self.__X_POS = x

    def set_y_pos(self, y):
        self.__Y_POS = y    

    def get_x_pos(self):
        return self.__X_POS

    def get_y_pos(self):
        return self.__Y_POS

    def get_player_name(self):
        return self.__PLAYER.get_name()
    
    def get_player_number(self):
        return self.__PLAYER.get_number()
        
        