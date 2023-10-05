#!/usr/bin/env python3

import json

cars = {
    'Toyota': ['Camry', 'Corolla', 'Prius'],
    'Honda': ['Civic', 'Accord', 'CR-V'],
    'Ford': ['F-150', 'Focus', 'Escape'],
    'Chevrolet': ['Silverado', 'Malibu', 'Equinox'],
    'Volkswagen': ['Jetta', 'Passat', 'Tiguan'],
    'BMW': ['3 Series', '5 Series', 'X5'],
    'Mercedes-Benz': ['C-Class', 'E-Class', 'GLC'],
    'Audi': ['A4', 'Q5', 'A6'],
    'Nissan': ['Altima', 'Rogue', 'Maxima'],
    'Hyundai': ['Elantra', 'Tucson', 'Santa Fe']
}

print(json.dumps(cars, indent=4))
