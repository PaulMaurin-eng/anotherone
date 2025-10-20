#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 13:07:19 2025

@author: paulmaurin
"""

from pydantic import BaseModel

# Définition du modèle
class Utilisateur(BaseModel):
    id: int
    nom: str
    age: int

# Données reçues (par exemple depuis une API)
donnees = {"id": "1", "nom": "Alice", "age": 25}

# Validation avec Pydantic
utilisateur = Utilisateur(**donnees)

print(utilisateur)
print(utilisateur.id)   # → 1 (converti automatiquement en int)