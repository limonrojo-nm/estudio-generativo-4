from zlib import c, DibujoPrincipal
from dibujo import ParticulaFactory

dibujo_principal = DibujoPrincipal([ParticulaFactory(1000)])

def setup():
    size(c.ancho, c.alto)
    frameRate(c.fps)
    background(*c.bg_color)

def draw():
    dibujo_principal.dibujar()
    c.procesar_fotograma()
    # exportador_fotogramas()
