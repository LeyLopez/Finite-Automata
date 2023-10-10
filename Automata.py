class Automata:
    def __init__(self, status, transitions, initial_status, final_status, position):
        self.status=status
        self.transitions=transitions
        self.initial_status=initial_status
        self.final_status=final_status
        self.position=position
        
        
    def get_status(self):
        return self.status
    
    def get_transitions(self):
        return self.transitions
    
    def get_initial_status(self):
        return self.initial_status
    
    def get_final_status(self):
        return self.final_status
    
    def get_position(self):
        return self.position
    
    