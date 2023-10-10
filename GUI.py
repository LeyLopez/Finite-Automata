import sys 
sys.path.insert(0, 'C:\\Users\\leidi\\AppData\\Roaming\\Python\\Python38\\site-packages')
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, QAction, QActionGroup
from PySide6.QtWidgets import *
from gtts import gTTS
from playsound import playsound
import matplotlib as matp
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg
import networkx as nx
import os
import gettext

matp.use('Qt5Agg')

directorio_actual = os.getcwd()
localedir = os.path.join(directorio_actual, 'locale')

gettext.bindtextdomain('myapp', localedir)
gettext.textdomain('myapp')

class Interface(QMainWindow):

    def __init__(self, automata):

        plt.rcParams['toolbar'] = 'None'

        super().__init__()

        self.automata = automata

        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(self.automata.get_status())
        self.graph.add_weighted_edges_from(self.generate_edges())

        # INICIALIZAR LAS OPCIONES DE LOS MENÚ
        self.languages_menu = None
        self.ingles_action = None
        self.portugues_action = None
        self.espanol_action = None

        # PARA GENERAR LOS MENÚ DE LOS IDIOMAS
        self.languages_group = QActionGroup(self)
        self.languages_group.setExclusive(True)

        self.create_interface()


    def create_interface(self, idioma = 'es'):

        translations = gettext.translation('mensajes', localedir, languages=[idioma])
        translations.install()
        _ = translations.gettext

        # NOMBRE Y TAMAÑO DE LA VENTANA
        self.setWindowTitle(_("Autómata"))
        self.setGeometry(100, 100, 800, 600)

        # WIDGET PRNCIPAL
        widget = QWidget()
        self.setCentralWidget(widget)

        # ACTUALIZAR EL MENU DE IDIOMAS
        if self.languages_menu:
            self.language_text_update()

        # BARRA DE MENU PARA CAMBIAR IDIOMA
        menu_bar = self.menuBar()

        if not self.languages_menu:

            self.languages_menu = menu_bar.addMenu(_("Idiomas"))

        if not self.ingles_action:

            self.ingles_action = QAction(_("Inglés"), self)
            self.languages_menu.addAction(self.ingles_action)
            self.ingles_action.setCheckable(True)
            self.languages_group.addAction(self.ingles_action)

        self.ingles_action.triggered.connect(lambda: self.change_language('en'))

        if not self.portugues_action:

            self.portugues_action = QAction(_("Francés"), self)
            self.languages_menu.addAction(self.portugues_action)
            self.portugues_action.setCheckable(True)
            self.languages_group.addAction(self.portugues_action)

        self.portugues_action.triggered.connect(lambda: self.change_language('fr'))

        if not self.espanol_action:

            self.espanol_action = QAction(_("Español"), self)
            self.languages_menu.addAction(self.espanol_action)
            self.espanol_action.setCheckable(True)
            self.languages_group.addAction(self.espanol_action)
            self.espanol_action.setChecked(True)

        self.espanol_action.triggered.connect(lambda: self.change_language('es'))

        # LAYOUT PRINCIPAL
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # QLABEL PARA MOSTRAR MENSAJE
        speed_label = QLabel(_("Verificar palabra"))
        layout.addWidget(speed_label )

        # QLINEEDIT PARA INGRESAR LA CADENA
        self.string_linee = QLineEdit()
        layout.addWidget(self.string_linee)

        string_label = QLabel(_("Velocidad"))
        layout.addWidget(string_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(5)
        self.slider.setValue(1)
        layout.addWidget(self.slider)

        # BOTÓN PARA PROCESAR
        process_button = QPushButton(_("Verificar"))
        process_button.clicked.connect(self.process)
        layout.addWidget(process_button)

        # CREAR UN WIDGET TIPO LIENZO PARA MOSTRAR LA IMAGEN
        self.scene = QGraphicsScene()
        self.canvas = QGraphicsView(self.scene)
        layout.addWidget(self.canvas)

        # QLABEL PARA MOSTRAR LA IMAGEN
        self.picture_label = QLabel()
        layout.addWidget(self.picture_label)

    def process_word(self, word):

        current_status = self.automata.get_initial_status()

        self.update_nodes(current_status)

        for symbols in word:

            if (current_status, symbols) in self.automata.get_transitions():

                self.update_edges(current_status, self.automata.get_transitions()[(current_status, symbols)])
                current_status = self.automata.get_transitions()[(current_status, symbols)]
                self.update_nodes(current_status)

            else:

                return False

        return current_status in self.automata.get_final_status()

    def process(self):

        if self.process_word(self.string_linee.text()):

            self.process_voice(self.traduction("La palabra es aceptada"))
            QMessageBox.information(self, self.traduction("Resultado"), self.traduction("La palabra es aceptada"))

        else:

            self.process_voice(self.traduction("La palabra no es aceptada"))
            QMessageBox.warning(self, self.traduction("Resultado"), self.traduction("La palabra no es aceptada"))


    def generate_edges(self):

        edges = set()

        for key in self.automata.get_transitions():

            edges.add((key[0], self.automata.get_transitions()[key], key[1]))

        return edges

    def update_nodes(self, status):

        nx.draw(self.graph, self.automata.get_position(), with_labels = True, node_color = ['blue' if node == status else 'red' for node in self.graph.nodes()])
        self.draw_labes()

        plt.savefig('output.png', dpi = 300, format = 'png', bbox_inches = 'tight')
        self.update_picture()

        plt.pause(1 / self.slider.value())

    def update_edges(self, initial_status, final_status):

        nx.draw(self.graph, self.automata.get_position(), with_labels = True, node_color = "red")
        nx.draw_networkx_edges(self.graph, self.automata.get_position(), edgelist = {(initial_status, final_status)}, edge_color = "blue")

        # OBTIENE EL PESO DE CADA ARISTA
        weight = nx.get_edge_attributes(self.graph, 'weight')
        # DIBUJA EL GRAFO CON LOS PESOS DE CADA ARISTA
        nx.draw_networkx_edge_labels(self.graph, self.automata.get_position(), edge_labels = weight)

        nx.draw_networkx_edge_labels(self.graph, self.automata.get_position(), edge_labels = {(initial_status, final_status): weight[(initial_status, final_status)]}, font_color = "blue")

        plt.savefig('output.png', dpi = 300, format = 'png', bbox_inches ='tight')
        self.update_picture()

        plt.pause(1 / self.slider.value())

    def draw_labes(self):

        # OBTIENE EL PESO DE CADA ARISTA
        weight = nx.get_edge_attributes(self.graph, 'weight')
        # DIBUJA EL GRAFO CON LOS PESOS DE CADA ARISTA
        nx.draw_networkx_edge_labels(self.graph, self.automata.get_position(), edge_labels = weight)

    def update_picture(self):

        pixmap = QPixmap("output.png")
        item = self.scene.addPixmap(pixmap)
        item.setPos(0, 0)

        self.canvas.fitInView(item)

    def process_voice(self, texto):

        objeto = gTTS(text = texto, lang = self.get_language(), slow = False)
        objeto.save("mensaje.mp3")

        playsound("mensaje.mp3", block = False)

        os.remove("mensaje.mp3")

    def change_language(self, language):

        if language == 'en':
            self.ingles_action.setChecked(True)
            locale = 'en'

        elif language == 'pt':
            self.portugues_action.setChecked(True)
            locale = 'pt'

        else:
            self.espanol_action.setChecked(True)
            locale = 'es'

        gettext.install('mensajes', localedir, names=("ngettext",))
        gettext.translation('mensajes', localedir, languages=[locale]).install()

        self.create_interface(locale)

    def get_language(self):

        if self.ingles_action.isChecked():

            return 'en'

        elif self.portugues_action.isChecked():

            return 'pt'

        elif self.espanol_action.isChecked():

            return 'es'

    def traduction(self, mensaje):
        language = self.get_language()
        translations = gettext.translation('mensajes', localedir, languages=[language])
        translations.install()
        _ = translations.gettext

        return _(mensaje)

    def language_text_update(self):
        self.ingles_action.setText(self.traduction("Inglés"))
        self.espanol_action.setText(self.traduction("Español"))
        self.portugues_action.setText(self.traduction("Portugués"))
        self.languages_menu.setTitle(self.traduction("Idiomas"))
        
        
        
        
        
        
        
        
        
            
            
            
    
    
        
        
