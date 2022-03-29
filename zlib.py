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
class Posicion:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self): return self._x
    
    def reasignar_x(self, nueva_x):
        self._x = nueva_x
        
    @property
    def y(self): return self._y

    def reasignar_y(self, nueva_y):
        self._y = nueva_y
    
    def reasignar(self, nueva_x, nueva_y):
        self._x = nueva_x
        self._y = nueva_y
    
    def __str__(self):
        return "Posicion.x: " + str(self.x) + " Posicion.y: " + str(self.y)
    
    

# -----------------------------------------------------------
# Dibujo
class Dibujo(ConCore):
    def dibujar(self): levantarExcepcion("ERROR: No implementado", self)

class DibujoPrincipal(Dibujo):
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
# Mixins
class ConPosicion:
    _posicion = None
    
    @property
    def posicion(self): return self._posicion


# -----------------------------------------------------------
# Utils
class ExportadorDeFotogramas(ConCore):
    def __init__(self, frecuencia_exportacion=1, ceros_n_fotograma=5):
        
        self._frecuencia_exportacion = frecuencia_exportacion
        self._ceros_n_fotograma = ceros_n_fotograma
        self._codigo_seq = str(random(99999)).zfill(5)
    
    @property
    def frecuencia_exportacion(self): return self._frecuencia_exportacion
    @property
    def ceros_n_fotograma(self): return self._ceros_n_fotograma
    
    def __call__(self):
        if (self.c.fotograma % self.frecuencia_exportacion) == 0:
            save("frames/" + self._codigo_seq + "/" + str(self.c.fotograma).zfill(self.ceros_n_fotograma) + ".png")
    
    def exportar_fin(self):
        save("output/FINAL-" + self._codigo_seq + ".png")



class GenaradorRuido:
    _noise_offset = 0.0
    
    def __init__(self, incremento, amplitud_fija=1):
        self._incremento = incremento
        self._amplitud_fija = amplitud_fija
        self._semilla_random = int(random(90000))
        
    
    def __call__(self):
        self._incrementar_offset()
        noiseSeed(self._semilla_random)
        return noise(self.noise_offset)
    
    @property
    def incremento(self): return self._incremento
    
    @property
    def amplitud_fija(self): return self._amplitud_fija
    
    @property
    def noise_offset(self): return self._noise_offset
    
    def _incrementar_offset(self):
        self._noise_offset += self.incremento
