from zlib import Dibujo, ConPosicion, Posicion, GenaradorRuido



class Particula(Dibujo, ConPosicion):
    _conectada = False
    _amplitud_ruido = 3
    _vitalidad = 20
    
    def __init__(self):
        self._ngen_x = GenaradorRuido(0.02)
        self._ngen_y = GenaradorRuido(0.02)
        self._ngen_circ = GenaradorRuido(0.02)
        self._iniciar_posicion()
        self._randomizar_posicion()
        
        
    def alimentar(self): self._vitalidad += random(.2, 1)
     
    def dibujar(self, factory):
        self._randomizar_posicion()
        pushStyle()
        stroke(10)
        strokeWeight(10)
        # point(self.posicion.x,
        #       self.posicion.y)
        noFill()
        strokeWeight(3)
        circle(self.posicion.x,
              self.posicion.y, self._ngen_circ()*30+self._vitalidad)
        popStyle()
        
        self._cansarse(factory)
    
    def conectar(self, hermana):
        pushStyle()
        stroke(40)
        strokeWeight(2)
        line(self.posicion.x,
              self.posicion.y,
              hermana.posicion.x,
              hermana.posicion.y)
        popStyle()
        hermana.alimentar()
    
    
    
    # Privados ----------------
    def _iniciar_posicion(self):
        x = random(0+self.c.ancho*self._ngen_x(), self.c.ancho-self.c.ancho*self._ngen_x())
        y = random(0+self.c.ancho*self._ngen_y(), self.c.alto-self.c.ancho*self._ngen_y())
        self._posicion = Posicion(x, y)
        
    def _randomizar_posicion(self):
        
        r_x = (self.posicion.x + (self._ngen_x()*self._amplitud_ruido*2 -self._amplitud_ruido)) % self.c.ancho
        r_y = (self.posicion.y + (self._ngen_y()*self._amplitud_ruido*2 -self._amplitud_ruido)) % self.c.alto
        self.posicion.reasignar(r_x, r_y)


    def _cansarse(self, factory):
        self._vitalidad -= random(.2, 1)
        if self._vitalidad < 0:
            factory._particulas.remove(self)



class ParticulaFactory(Dibujo):
    _particulas = []
    
    def __init__(self, cantidad=1):
        self._generar_particulas(cantidad)
    
    def dibujar(self):
        # hermana_anterior = None
        for particula in self._particulas:
            particula.dibujar(self)
            particula.conectar(self.mas_cercana(particula))
            # if hermana_anterior is not None:
            #     particula.conectar(hermana_anterior)
            # hermana_anterior = particula
    
    def mas_cercana(self, buscadora):
        """
        """
        cercana = None
        menor_distancia = float("inf")
        
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
