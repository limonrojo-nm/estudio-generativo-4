from zlib import c, DibujoPrincipal, ExportadorDeFotogramas
from dibujo import ParticulaFactory

dibujo_principal = DibujoPrincipal([ParticulaFactory(100)])
exportador_fotogramas = ExportadorDeFotogramas(1)



def setup():
    size(c.ancho, c.alto)
    frameRate(c.fps)
    background(*c.bg_color)

def draw():
    
    dibujo_principal.procesar_fotograma()
    
    c.procesar_fotograma()
    # exportador_fotogramas()
