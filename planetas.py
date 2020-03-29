#!/usr/bin/env python

# -*- coding: utf-8 -*-

class Planetas:

   def __init__(self, nombre, diametro, distanciasol):

       self.nombre = nombre

       self.diametro = diametro

       self.distancia = distanciasol

   def getDiametro(self):

       return str(self.diametro) + ' km de diámetro'

   def getDistanciaSol(self):

       return str(self.distancia) + ' millones de km'

   def __str__(self):

       return 'Planeta ' + self.nombre

 

tierra = Planetas('Tierra', 12756, 149.6)

print(tierra.getDiametro())
























"""
class Planetas:

   def __init__(self, nombre, diametro, distanciasol):

       self.nombre = nombre

       self.diametro = diametro

       self.distancia = distanciasol

   def getDiametro(self):

       return str(self.diametro) + ' km de diámetro'

   def getDistanciaSol(self):

       return str(self.distancia) + ' millones de km'

   def __str__(self):

       return 'Planeta ' + self.nombre
    
tierra = Planetas('Tierra', 12756, 149.6)

print(type(tierra))

"""
