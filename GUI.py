from typing import Optional
from PySide6.QtCore import *
import PySide6.QtCore
from PySide6.QtGui import QPixmap, QAction, QActionGroup
from PySide6.QtWidgets import *
import PySide6.QtWidgets
from gtts import gTTS
from playsound import playsound

import matplotlib as matp
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg

import networkx as nx
import gettext
import os

matp.use('Qt5Agg')

directorio_actual = os.getcwd()
localedir = os.path.join(directorio_actual, 'locale')

gettext.bindtextdomain('Finite_automata', localedir)
gettext.textdomain('Finite_automata')

class Interface(QMainWindow):
    def __init__(self, automata):
        
        plt.rcParams['toolbar'] = 'None'
    
        super().__init__()
        self.automata=automata
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(self.automata.get_status())
        self.graph.add_weighted_edges_from(self.generate_edge())
        
        
        self.languages_menu = None
        self.ingles_action = None
        self.frances_action = None
        self.espanol_action = None
        
        
        self.language_group = QActionGroup(self)
        self.language_group.setExclusive(True)
        
        self.create_interface()
        
    def create_interface(self, language='es'):
        translations=gettext.translation('mensaje', localedir, languages=[language])
        translations.install()
        _=translations.gettext
        
        self.setWindowTitle(_("AFND"))
        self.setGeometry(100, 100, 800, 600)
        
        widget=QWidget()
        self.setCentralWidget(widget)
        
        if self.languages_menu:
            self.update_language_menu_text()
            
        menu_bar=self.menuBar()
        if not self.languages_menu:
            self.languages_menu=menu_bar.addMenu(_("Idiomas"))       
            
        if not self.ingles_action:
            self.ingles_action = QAction(_("Inglés"), self)
            self.languages_menu.addAction(self.ingles_action)
            self.ingles_action.setCheckable(True)
            self.language_group.addAction(self.ingles_action)
        self.ingles_action.triggered.connect(lambda: self.change_language('en'))
        
        if not self.espanol_action:
            self.espanol_action = QAction(_("Español"), self)
            self.languages_menu.addAction(self.espanol_action)
            self.espanol_action.setCheckable(True)
            self.language_group.addAction(self.espanol_action)
        self.espanol_action.triggered.connect(lambda: self.change_language('es'))
        
        if not self.frances_action:
            self.frances_action = QAction(_("Francés"), self)
            self.languages_menu.addAction(self.frances_action)
            self.frances_action.setCheckable(True)
            self.language_group.addAction(self.frances_action)
        self.frances_action.triggered.connect(lambda: self.change_language('fr'))
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
    
    
        
        
