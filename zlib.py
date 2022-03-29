# -------------------------------
# Core
class Core:
    _ancho = 1000
    _alto = 1000
    _fps = 100
    _bg_color = 20.
    _bg_alpha = 240.
    _imprimir_fotograma = True
    
    __fotograma = 0
    
    @property
    def ancho(self): return self._ancho
    @property
    def alto(self): return self._alto
    @property
    def fps(self): return self._fps
    @property
    def bg_color(self): return self._bg_color
    @property
    def bg_alpha(self): return self._bg_alpha
    @property
    def fotograma(self): return self.__fotograma
    @property
    def centro_x(self): return self.ancho / 2
    @property
    def centro_y(self): return self.alto / 2
    
    def procesar_fotograma(self):
        self._contar_fotograma()
    
    # Privados ---------------
    def _contar_fotograma(self):
        if self._imprimir_fotograma: print(self.fotograma)
        self.__fotograma += 1

c = Core()

class ConCore:
    _core = c
    
    @property
    def c(self): return self._core
