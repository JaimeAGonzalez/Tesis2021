#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 20:13:20 2021

@author:JaimeNunez
"""

import sympy as sp
import numpy as np

def Rotacion(TipoR):
    
    #Rotacion del Sistema p,u,v,w
    vars=sp.symbols('alpha phi theta')
    
    #Tipo de Rotacion: X-Alpha,Y-Phi,Z-Theta
    if TipoR=='RotacionX':
        MatrizRotacion=sp.Matrix([[1,0,0,0],
        [0,sp.cos(vars[0]),-1*sp.sin(vars[0]),0],
        [0,sp.sin(vars[0]),sp.cos(vars[0]),0],
        [0,0,0,1]])
        
    elif TipoR=='RotacionY':
          MatrizRotacion=sp.Matrix([[sp.cos(vars[1]),0,sp.sin(vars[1]),0],
          [0,1,0,0],
          [-sp.sin(vars[1]),0,sp.cos(vars[1]),0],
          [0,0,0,1]])
          
    elif TipoR=='RotacionZ':
          MatrizRotacion=sp.Matrix([[sp.cos(vars[2]),-sp.sin(vars[2]),0,0],
           [sp.sin(vars[2]),sp.cos(vars[2]),0,0],
           [0,0,1,0],
           [0,0,0,1]])       
   
    return MatrizRotacion