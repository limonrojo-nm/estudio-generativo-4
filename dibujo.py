from zlib import Dibujo, ConPosicion, Posicion, GenaradorRuido

ngen_x = GenaradorRuido(0.001)
ngen_y = GenaradorRuido(0.001)

class Particula(Dibujo, ConPosicion):
    def __init__(self):
        self._iniciar_posicion()
        self._randomizar_posicion()
        
    
    def dibujar(self):
        self._randomizar_posicion()
        pushStyle()
        stroke(10)
        strokeWeight(10)
        point(self.posicion.x,
              self.posicion.y)
        popStyle()
    
    def conectar(self, hermana):
        pushStyle()
        stroke(40)
        strokeWeight(2)
        line(self.posicion.x,
              self.posicion.y,
              hermana.posicion.x,
              hermana.posicion.y)
        popStyle()
    
    # Privados ----------------
    def _iniciar_posicion(self):
        self._posicion = Posicion(0, 0)
        
    def _randomizar_posicion(self):
        r_x = random(0, self.c.ancho)
        r_y = random(0, self.c.alto)
        self.posicion.reasignar(r_x,r_y)





class ParticulaFactory(Dibujo):
    _particulas = []
    
    def __init__(self, cantidad=1):
        self._generar_particulas(cantidad)
    
    def dibujar(self):
        # hermana_anterior = None
        for particula in self._particulas:
            particula.dibujar()
            particula.conectar(self.mas_cercana(particula))
            # if hermana_anterior is not None:
            #     particula.conectar(hermana_anterior)
            # hermana_anterior = particula
    
    def mas_cercana(self, buscadora):
        """
        """
        cercana = None
        menor_distancia = float(999999999)
        
        for particula in self._particulas:
            if particula != buscadora:
                distancia_actual = dist(buscadora.posicion.x,buscadora.posicion.y,
                                        particula.posicion.x,particula.posicion.y)
                if distancia_actual <= menor_distancia:
                    menor_distancia = distancia_actual
                    cercana = particula
        
        return cercana
                
    
    
    # Privados ----------------
    def _generar_particulas(self, cantidad):
        for _ in range(cantidad):
            self._particulas.append(Particula())
