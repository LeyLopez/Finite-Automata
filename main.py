from Automata import Automata
from GUI import Interface
from PySide6.QtWidgets import QApplication

import sys

def iniciar():

    automata = create_automata()
    aplicacion = QApplication(sys.argv)
    root = Interface(automata)
    root.show()
    sys.exit(aplicacion.exec())


def create_automata():
    status = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'}
    transitions = {

        ("q0", "a"): "q1",
        ("q1", "a"): "q2",
        ("q2", "b"): "q3",
        ("q3", "b"): "q6",
        ("q3", "a"): "q4",
        ("q4", "b"): "q5",
        ("q5", "b"): "q7",
        ("q5", "a"): "q8", 
        ("q8", "b"): "q9",
        ("q9", "b"): "q10",
        ("q9", "a"): "q11",
        ("q11", "b"): "q12",
        ("q12", "b"): "q13"
    }
    initial_status = 'q0'
    final_status = {'q6','q7', 'q10', 'q13' }
    position = {
        "q0": (1, 0),
        "q1": (1, 1),
        "q2": (2, 2),
        "q3": (3, 1),
        "q4": (5, 1),
        "q5": (5, 0),
        "q6": (3, 0),
        "q7": (5, -1),
        "q8": (8, 0),
        "q9": (8, -1),
        "q10": (8, -2),
        "q11": (11, -1),
        "q12": (14, -1),
        "q13": (14, -2)
        }

    automata = Automata(status, transitions, initial_status, final_status, position)
    return automata

iniciar()