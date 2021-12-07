class Player :

    def __init__(self, name, number) -> None:
        """
            This class can be used to define player name, number and player attributes. 
            Specific skill set can also be added in this.
        """
        
        self.PLAYER_NAME = name
        self.PLAYER_NUMBER = number
        self.NODE_OBJ = None

    def set_node_obj(self, obj):
        self.NODE_OBJ = obj
    
    def get_node_obj(self):
        return self.NODE_OBJ

    def get_name(self):
        return self.PLAYER_NAME
    
    def get_number(self):
        return self.PLAYER_NUMBER


