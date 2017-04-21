La actividad consiste en seleccionar figuras que tengan caracterísitcas similares o sean totalemtne diferentes.
La actividad va dirigida a niños con discapacidad visual.

----------------------------------------------------------------------------------------------------------------------

Pasos del Audio Pattern

Va a existir una clase, donde se relacione Figuras con Sonidos y Estado. Dónde el estado puede ser: Vacio, Escuchado, Seleccionado

1. El Sistema muestra 9 figuras
2. El Usuario inicia recorriendo las figuras con las teclas direccionales
3. Cuando se posiciona sobre una figura, tiene dos opciones
	a) Click Izquierdo: Para escuchar
		- El estado de la figura cambia a Escuchado
		- La figura queda habilitada para ser seleccionada
		- La figura puede volver a ser escuchada si el usuario lo desea
	b) Click Derecho: Para seleccionar
		- Si el estado de la figura es 'Vacio', no podrá ser seleccionada y el sistema lanzará una advertencia de sonido
		- Si el estado de la figura es 'Escuchado', cambia a 'Seleccionado' y la figura entra al conjunto de los seleccionados
4. En el Área de Seleccionados hay tres lugares para se llenados con las selecciones hechas por el usuario. Una vez completa el área, el Sistema comunica al usuario si las selecciones fueron válidas o no.
5. El juego se reinicia automáticamente
