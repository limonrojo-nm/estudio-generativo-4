from config import _config

# -----------------------------------------------------------
# Excepciones
def levantarExcepcion(msg, obj=None):
    obj_detail = " @ " + str(obj.__class__) if obj is not None else ""
    print(msg + obj_detail)
    raise Exception()





# -----------------------------------------------------------
# Core
class Core:
    """
    Espera en _config un diccionario con la forma:
        CONFIG = {
            "ancho": 1000,
            "alto": 1000,
            "fps": 100,
            "bg_color": 20.,
            "imprimir_fotograma": True,    
        }
    """
    _config = _config
    __fotograma = 0
    
    @property
    def config(self): return self._config
    @property
    def ancho(self): return self.config.ancho
    @property
    def alto(self): return self.config.alto
    @property
    def fps(self): return self.config.fps
    @property
    def bg_color(self): return self.config.bg_color
    @property
    def reimprimir_fondo_en_fotograma(self): return self.config.reimprimir_fondo_en_fotograma
    
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
    def _imprimir_fotograma(self): return self.config.imprimir_fotograma
    
    def _contar_fotograma(self):
        if self._imprimir_fotograma: print(self.fotograma)
        self.__fotograma += 1

c = Core()

class ConCore:
    _core = c
    
    @property
    def c(self): return self._core



# -----------------------------------------------------------
# Value Objects
class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self): return self._x
    
    @property
    def y(self): return self._y

# -----------------------------------------------------------
# Dibujo
class Dibujo:
    def dibujar(self): levantarExcepcion("ERROR: No implementado", self)

class DibujoPrincipal(Dibujo, ConCore):
    def __init__(self, dibujos):
        """
        @dibujos: [Dibujo]
        """
        self.dibujos = dibujos
    
    def dibujar(self):
        self._manejar_reset_fondo()
        for dibujo in self.dibujos:
            dibujo.dibujar()
    
    # Privados ---------------
    def _manejar_reset_fondo(self):
        if self.c.reimprimir_fondo_en_fotograma:
            pushStyle()
            fill(*self.c.bg_color)
            noStroke()
            rect(0, 0, self.c.ancho, self.c.alto)
            popStyle()


# -----------------------------------------------------------
# Utils
class ExportadorDeFotogramas:
    def __init__(self, core, frecuencia_exportacion=1, ceros_n_fotograma=5):
        self._c = core
        self._frecuencia_exportacion = frecuencia_exportacion
        self._ceros_n_fotograma = ceros_n_fotograma
        self._codigo_seq = str(random(99999)).zfill(5)
    
    @property
    def c(self): return self._c
    @property
    def frecuencia_exportacion(self): return self._frecuencia_exportacion
    @property
    def ceros_n_fotograma(self): return self._ceros_n_fotograma
    
    def __call__(self):
        if (self.c.n_fotograma % self.frecuencia_exportacion) == 0:
            save("frames/" + self._codigo_seq + "/" + str(self.c.n_fotograma).zfill(self.ceros_n_fotograma) + ".png")
    
    def exportar_fin(self):
        save("output/FINAL-" + self._codigo_seq + ".png")
