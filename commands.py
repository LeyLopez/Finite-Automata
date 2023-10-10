from abc import ABC, abstractclassmethod

class Command(ABC):
    
    @abstractclassmethod
    def execute(self):
        pass
    
class ProcessStringCommand(Command):
    def __init__(self, gui, input_string):
        self.automata_gui=gui
        self.input_string=input_string
        
    def execute(self):
        self.automata_gui.process_string(self.input_string)