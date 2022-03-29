from zlib import c, DibujoPrincipal, ExportadorDeFotogramas
from dibujo import ParticulaFactory

dibujo_principal = DibujoPrincipal([ParticulaFactory(50)])
exportador_fotogramas = ExportadorDeFotogramas(1)



def setup():
    size(c.ancho, c.alto)
    frameRate(c.fps)
    background(*c.bg_color)

def draw():
    dibujo_principal.dibujar()
    c.procesar_fotograma()
    exportador_fotogramas()
