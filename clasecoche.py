#!/usr/bin/env python

# -*- coding: utf-8 -*-

class Coches:
    
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "negro"

    def elColor(self):
        return self.color

miCoche = Coches("mustang", "2017")
print(miCoche.elColor())


class CochesDeportivo(Coches):
    
    def __init__(self,marca,modelo, velMax):
        Coches __init__(self, marca, modelo)
            
           

    def elColor(self):
        return self.color

miCoche = Coches("mustang", "2017")
print(miCoche.elColor())

#FIN
#editamos para ver cambios
  

  
