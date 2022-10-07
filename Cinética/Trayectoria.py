#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:33:37 2021

@author:Jaime Nunez
"""

import sympy as sp

def Trayectoria(H0,H,T,Tmax):
    
    #Variables Simbolicas
    h0, h, t, tmax=sp.symbols('h0 h t tmax')
    
    #Trayectoria
    TR=[0]*len(T)
    ST=h0+h*(10*(t/tmax)**3 -15*(t/tmax)**4 +6*(t/tmax)**5)
    
    for i in range(len(T)):
       NT=ST.subs({h0:H0, h:H, t:T[i], tmax:Tmax})
       TR[i]=NT
    
    return TR
