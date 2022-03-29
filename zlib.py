from config import CONFIG


# -------------------------------
# Core
class Core:
    """
    Espera en _config un diccionario con la forma:
        CONFIG = {
            "ancho": 1000,
            "alto": 1000,
            "fps": 100,
            "bg_color": 20.,
            "bg_alpha": 240.,
            "imprimir_fotograma": True,    
        }
    """
    _config = CONFIG
    __fotograma = 0
    
    @property
    def config(self): return self._config
    @property
    def ancho(self): return self.config["ancho"]
    @property
    def alto(self): return self.config["alto"]
    @property
    def fps(self): return self.config["fps"]
    @property
    def bg_color(self): return self.config["bg_color"]
    @property
    def bg_alpha(self): return self.config["bg_alpha"]
    
    @property
    def fotograma(self): return self.__fotograma
    @property
    def centro_x(self): return self.ancho / 2
    @property
    def centro_y(self): return self.alto / 2
    
    def procesar_fotograma(self):
        self._contar_fotograma()
    
    # Privados ---------------
    @property
    def _imprimir_fotograma(self): return self.config["imprimir_fotograma"]
    
    def _contar_fotograma(self):
        if self._imprimir_fotograma: print(self.fotograma)
        self.__fotograma += 1

c = Core()

class ConCore:
    _core = c
    
    @property
    def c(self): return self._core



# -------------------------------
# Excepciones

def levantarExcepcion(msg, obj=None):
    obj_detail = " @ " + str(obj.__class__) if obj is not None else ""
    print(msg + obj_detail)
    raise Exception()
