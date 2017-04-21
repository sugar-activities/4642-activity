# Copyright 2013 Ma. Beatriz Vierci, Ana Belen Trinidad Candia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk
import logging
import random

from gettext import gettext as _

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityButton
from sugar.activity.widgets import ActivityToolbox
from sugar.activity.widgets import TitleEntry
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ShareButton
from ConfigParser import SafeConfigParser
from subprocess import Popen

class AudioPatternActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()
        
        separator = gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()
	
        principalVbox = gtk.VBox(False, 50)
        cabeceraHbox = gtk.HBox()
	jugarButton = gtk.Button()
	principalVbox.pack_start(cabeceraHbox, fill=False)
	jugarButton.set_label('JUGAR')
	jugarButton.connect('focus-in-event', self.__say_text)

	labels_generados = ''
	
	cabeceraHbox.pack_start(jugarButton, fill=False)
        jugarButton.set_size_request(150, 50)

        
	cancelarButton = gtk.Button()
	cancelarButton.set_label('CANCELAR')
	cancelarButton.connect('focus-in-event', self.__say_text)
	cabeceraHbox.pack_start(cancelarButton, fill=False)
	cancelarButton.connect('clicked', self.__button_clicked_cb, 'CANCELAR')
	cuerpoHbox = gtk.HBox(False, 20)
	cancelarButton.set_size_request(150, 50)
	
	seleccionadosTable = gtk.Table(4, 1, True)

	seleccionadoUnoButton = gtk.Button()
	seleccionadoDosButton = gtk.Button()
	seleccionadoTresButton = gtk.Button()
	self.resultadoButton = gtk.Button()

	seleccionadosTable.set_size_request(200, 400)
	
	
	opcionesTable = gtk.Table(3,3, True)
	self.opcionUno = gtk.Button()
	
	self.opcionDos = gtk.Button()
	self.opcionTres = gtk.Button()
	self.opcionCuatro = gtk.Button()
	self.opcionCinco = gtk.Button()
	self.opcionSeis = gtk.Button()
	self.opcionSiete = gtk.Button()
	self.opcionOcho = gtk.Button()
	self.opcionNueve = gtk.Button()	
	
	self.opcionUno.connect('focus-in-event', self.__say_text)
	self.opcionDos.connect('focus-in-event', self.__say_text)
	self.opcionTres.connect('focus-in-event', self.__say_text)
	self.opcionCuatro.connect('focus-in-event', self.__say_text)
	self.opcionCinco.connect('focus-in-event', self.__say_text)
	self.opcionSeis.connect('focus-in-event', self.__say_text)
	self.opcionSiete.connect('focus-in-event', self.__say_text)
	self.opcionOcho.connect('focus-in-event', self.__say_text)
	self.opcionNueve.connect('focus-in-event', self.__say_text)
	
	self.set_canvas(principalVbox)
	self.connect('key-press-event', self.__on_key_press_event, seleccionadoUnoButton, seleccionadoDosButton, seleccionadoTresButton, 			      jugarButton)
      
        cabeceraHbox.add(jugarButton)
        cabeceraHbox.add(cancelarButton)
        
	
	principalVbox.add(cabeceraHbox)
        principalVbox.add(cuerpoHbox)
	
        cuerpoHbox.add(seleccionadosTable)
	cuerpoHbox.add(opcionesTable)
	
	seleccionadosTable.attach(seleccionadoUnoButton, 0, 1, 0, 1, 10, 20, 10, 5)
	seleccionadoUnoButton.set_size_request(180, 80)

	seleccionadosTable.attach(seleccionadoDosButton, 0, 1, 1, 2, 10, 30, 10, 5)
	seleccionadoDosButton.set_size_request(180, 80)
	
	seleccionadosTable.attach(seleccionadoTresButton, 0, 1, 2, 3, 10, 20, 10, 5)
	seleccionadoTresButton.set_size_request(180, 80)

	seleccionadosTable.attach(self.resultadoButton, 0, 1, 3 , 4, 10, 20, 10, 5)
	self.resultadoButton.set_size_request(180, 80)

	seleccionadosTable.set_row_spacings(5)
	seleccionadosTable.set_col_spacings(10)

	opcionesTable.attach( self.opcionUno, 0, 1, 0, 1, 10, 10)
	self.opcionUno.set_size_request(180, 80)

	opcionesTable.attach( self.opcionDos, 1, 2, 0, 1, 10, 10)
	self.opcionDos.set_size_request(180, 80)

	opcionesTable.attach( self.opcionTres, 2, 3, 0, 1, 10, 10)
	self.opcionTres.set_size_request(180, 80)
	
	opcionesTable.attach( self.opcionCuatro, 0, 1, 1, 2, 10, 10)
	self.opcionCuatro.set_size_request(180, 80)
	
	opcionesTable.attach( self.opcionCinco, 1, 2, 1, 2, 10, 10)
	self.opcionCinco.set_size_request(180, 80)	
	
	opcionesTable.attach( self.opcionSeis, 2, 3, 1, 2, 10, 10)
	self.opcionSeis.set_size_request(180, 80)

	opcionesTable.attach( self.opcionSiete, 0, 1, 2, 3, 10, 10)
	self.opcionSiete.set_size_request(180, 80)

	opcionesTable.attach( self.opcionOcho, 1, 2, 2, 3, 10, 10)
	self.opcionOcho.set_size_request(180, 80)

	opcionesTable.attach( self.opcionNueve, 2, 3, 2, 3, 10, 10)
	self.opcionNueve.set_size_request(180, 80)

	opcionesTable.set_row_spacings(50)
	opcionesTable.set_col_spacings(10)
	
	principalVbox.show_all()
	
        
    def __button_clicked_cb(self, window, data=None):
        print(data)
       
    def __on_key_press_event(self, widget, event, uno, dos, tres, jugar):
        keyname = gtk.gdk.keyval_name(event.keyval)	
        widget_focus = widget.get_focus()
        label = widget_focus.get_label()
	if keyname == 'space' and label != '' and label != 'JUGAR' and label != 'CANCELAR' and widget_focus != uno and widget_focus != dos and 		   widget_focus != tres:	
            logging.debug(label)
            if uno.get_label() == ' ':
                uno.set_label(label)
                widget_focus.set_label('')
            else:
                if dos.get_label() == ' ':
                    dos.set_label(label)
                    widget_focus.set_label('')
                else:
                    if tres.get_label() == ' ':
                        tres.set_label(label)
                        widget_focus.set_label('')
			self.__verificar_resultado(uno.get_label(), dos.get_label(), tres.get_label())
			
	elif keyname == 'Return' and label == 'JUGAR':
		labels_generados = []
		labels_generados = self.__cargar_labels()		
		uno.set_label(' ')
		dos.set_label(' ')
		tres.set_label(' ')
		self.resultadoButton.set_label(' ')
		self.opcionUno.set_label(labels_generados[0])	
		self.opcionDos.set_label(labels_generados[1])
		self.opcionTres.set_label(labels_generados[2])
		self.opcionCuatro.set_label(labels_generados[3])
		self.opcionCinco.set_label(labels_generados[4])
		self.opcionSeis.set_label(labels_generados[5])
		self.opcionSiete.set_label(labels_generados[6])
		self.opcionOcho.set_label(labels_generados[7])
		self.opcionNueve.set_label(labels_generados[8])

            
    def __on_enter_event(self, widget, event):
        widget_focus = widget.get_focus()
        logging.debug(widget_focus.get_label())
        
    def __say_text(self, widget, event):
    	label = widget.get_label()
    	logging.debug(label)
    	self.say(label)
    	
    def say(self, text):
        Popen(['espeak', '-v', 'es', text])
   
    def __generar_labels(self):
	parser = SafeConfigParser()
        parser.read('config.ini')

	lista = []
	secciones = parser.sections()
	combinaciones = []
	for i in range (9):
		for section_name in secciones:
			opciones = parser.options(section_name)
			indice = random.randint(0, len(opciones) - 1)			
			lista.append(opciones[indice])

		combinaciones.append(lista)
		lista = []	
	return combinaciones
	
	
    def __verificar_combinaciones(self, combinacionesUno, combinacionesDos, CombinacionesTres):	
	bandera = False
	for fila in range(6):
		if(combinacionesUno[0]== combinacionesDos[0] and combinacionesUno[0]== CombinacionesTres[0] or
		   combinacionesUno[1]== combinacionesDos[1] and combinacionesUno[1]== CombinacionesTres[1] or
		   combinacionesUno[2]== combinacionesDos[2] and combinacionesUno[2]== CombinacionesTres[2]):
			bandera = True
			
		elif ((combinacionesUno[0]!= combinacionesDos[0] and combinacionesUno[0]!= CombinacionesTres[0] and 
		       combinacionesDos[0] != CombinacionesTres[0]) and (combinacionesUno[1]!= combinacionesDos[1] and
		       combinacionesUno[1]!= CombinacionesTres[1] and combinacionesDos[1] != CombinacionesTres[1]) and
		       (combinacionesUno[2]!= combinacionesDos[2] and combinacionesUno[2]!= CombinacionesTres[2]) and 
		       combinacionesDos[2] != CombinacionesTres[2]):
			bandera = True				
				
	return bandera



    def __cargar_labels(self):
	
	combinaciones = self.__generar_labels()

	bandera = False
	fila = 0
	while(bandera != True and fila < 6 ):
		combinaciones = self.__generar_labels()
		
		bandera = self.__verificar_combinaciones(combinaciones[fila], combinaciones[fila +1 ],  combinaciones[fila +2 ] )
		fila = fila +1

	labels_generados = []
	cadena_label = ''
	
	
	for i in range (9):
		cadena_label = combinaciones[i][0] + ' ' + combinaciones[i][1] + ' de ' + combinaciones[i][2]
		labels_generados.append(cadena_label)
		cadena_label = ''
	return labels_generados

    def __verificar_resultado(self, uno, dos, tres):
	logging.debug(uno)
	logging.debug(dos)
	logging.debug(tres)
	unoLista = uno.split(' ')
	unoLista.remove('de')
	dosLista = dos.split(' ')
	dosLista.remove('de')
	tresLista = tres.split(' ')
	tresLista.remove('de')

	bandera = self.__verificar_combinaciones(unoLista, dosLista, tresLista)	
	
	if(bandera):
		self.resultadoButton.set_label('Ganaste!')
		self.say('Ganaste!')		
	else:
		self.resultadoButton.set_label('Intentalo de Nuevo!')
		self.say('Intentalo de nuevo!')
    		
    		
   



