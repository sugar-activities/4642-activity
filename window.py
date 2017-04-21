#!/usr/bin/python
import gtk
import gobject


OPTIONS = ['a', 'b', 'c', 'd']
OPT_LENGHT = 4
DELAY = 2000


class MyApp():

    def __init__(self):
        window = gtk.Window()
        principalVbox = gtk.VBox()
        window.connect('destroy', self.destroy)
        window.set_title('Audio Pattern')
        window.set_position(gtk.WIN_POS_CENTER)
        window.set_default_size(800, 600)
        window.connect('key_press_event', self.__on_key_press_event)
        
        cabeceraHbox = gtk.HBox()
	jugarButton = gtk.Button()
	principalVbox.pack_start(cabeceraHbox, fill=False)
	jugarButton.set_label('JUGAR')
	cabeceraHbox.pack_start(jugarButton, fill=False)
        jugarButton.set_size_request(150, 50)

        #jugarButton.connect('clicked', self.__button_clicked_cb, 'CLICKED')
        #jugarButton.connect('enter', self.__button_clicked_cb, 'ENTER')
        #jugarButton.connect('activate', self.__button_clicked_cb, 'ACTIVATE')
        #jugarButton.connect('leave', self.__button_clicked_cb, 'LEAVE')
        #jugarButton.connect('pressed', self.__button_clicked_cb, 'PRESSED')
        #jugarButton.connect('released', self.__button_clicked_cb, 'RELEASED')
        #jugarButton.connect('BUTTON_PRESS', self.__button_clicked_cb, 'BUTTON_PRESS')
        #key_press_event
        cancelarButton = gtk.Button()
	cancelarButton.set_label('CANCELAR')
	cabeceraHbox.pack_start(cancelarButton, fill=False)
	cancelarButton.connect('clicked', self.__button_clicked_cb, 'CANCELAR')
	cuerpoHbox = gtk.HBox()
	cancelarButton.set_size_request(150, 50)
	
	seleccionadosTable = gtk.Table(4, 1, True)
	seleccionadoUnoButton = gtk.Button()
	seleccionadoDosButton = gtk.Button()
	seleccionadoTresButton = gtk.Button()
	#resultadoButton = gtk.Button()
	
	opcionesTable = gtk.Table(3,3, True)
	opcionUno = gtk.Button()
	opcionDos = gtk.Button()
	opcionTres = gtk.Button()
	opcionCuatro = gtk.Button()
	opcionCinco = gtk.Button()
	opcionSeis = gtk.Button()
	opcionSiete = gtk.Button()
	opcionOcho = gtk.Button()
	opcionNueve = gtk.Button()	
	       
        window.add(principalVbox)
        principalVbox.add(cabeceraHbox)
        principalVbox.add(cuerpoHbox)
                       
        cabeceraHbox.add(jugarButton)
        cabeceraHbox.add(cancelarButton)
        
        cuerpoHbox.add(seleccionadosTable)
	cuerpoHbox.add(opcionesTable)
	
	seleccionadosTable.attach(seleccionadoUnoButton, 0, 1, 0, 1)
	seleccionadosTable.attach(seleccionadoDosButton, 0, 1, 1, 2)
	seleccionadosTable.attach(seleccionadoTresButton, 0, 1, 2, 3)
	#seleccionadosTable.attach(selecionadoUnoButton, 0, 1, 0, 1)
		
	opcionesTable.attach( opcionUno, 0, 1, 0, 1)
	opcionesTable.attach( opcionDos, 1, 2, 0, 1)
	opcionesTable.attach( opcionTres, 2, 3, 0, 1)
	opcionesTable.attach( opcionCuatro, 0, 1, 1, 2)
	opcionesTable.attach( opcionCinco, 1, 2, 1, 2)
	opcionesTable.attach( opcionSeis, 2, 3, 1, 2)
	opcionesTable.attach( opcionSiete, 0, 1, 2, 3)
	opcionesTable.attach( opcionOcho, 1, 2, 2, 3)
	opcionesTable.attach( opcionNueve, 2, 3, 2, 3)
		
	window.show_all()
	
    def destroy(self, window, data=None):
        gtk.main_quit()
        
    def __button_clicked_cb(self, window, data=None):
        print(data)
       
    def __on_key_press_event(self, widget, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        print "Key %s (%d) was pressed" % (keyname, event.keyval)
        if keyname == 'space':
            print "Dentro del IF"
            widget_focus = widget.get_focus
            #print widget_focus.get_tab_label
  

if __name__ == "__main__":
    my_app = MyApp()
    gtk.main()
