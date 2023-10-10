from Automata import Automata
from Commands import AutomataGUI
from PySide6.QtWidgets import QApplication

import sys

def iniciar():

    automata = create_automata()
    aplicacion = QApplication(sys.argv)
    root = AutomataGUI(automata)
    root.show()
    sys.exit(aplicacion.exec())


def create_automata():
    status = {'A', 'B', 'C', 'D', 'E', 'F'}
    transitions = {
        ('A', 'a'): 'B',
        ('A', 'b'): 'C',
        ('B', 'a'): 'D',
        ('C', 'a'): 'E',
        ('C', 'b'): 'F',
        ('D', 'a'): 'E',
        ('D', 'b'): 'F',
        ('E', 'a'): 'F'
    }
    initial_status = 'A'
    final_status = {'F'}
    # POSICIÓN DE LOS NODOS (COLOCADOS ARBITRARIAMENTE)
    position = {

        'A': (0, 0),
        'B': (1, 1),
        'C': (1, -1),
        'D': (2, 2),
        'E': (1, 0),
        'F': (2, -2)

        }

    automata = Automata(status, transitions, initial_status, final_status, position)
    return automata

iniciar()