# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:24:09 2023
@author: Alan
"""

import math
import random

def create_svg(filename, num_electrons, orbit_radius, electron_radius, electron_speed, element_name):
    # calcola le coordinate dell'orbita dell'atomo
    orbit_points = []
    for angle in range(0, 360, 5):
        x = 100 + orbit_radius * math.cos(math.radians(angle))
        y = 100 + orbit_radius * math.sin(math.radians(angle))
        orbit_points.append((x, y))

    #calcolo offset per orbite degli elettroni
    el_offset = 360 / num_electrons
    # crea il documento SVG
    svg_lines = []
    svg_lines.append('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">')
    svg_lines.append('<rect x="0" y="0" width="100%" height="100%" fill="black"/>')
    
    #disegna il nucleo
    # Genera 5 colori casuali
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for i in range(5)]
    # Crea il gradiente lineare con i colori casuali
    gradient = '<linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">'
    for i, color in enumerate(colors):
        offset = i * 100 // (len(colors)-1)
        gradient += f'<stop offset="{offset}%" stop-color="{color}"><animate attributeName="stop-color" values="{color};#{colors[(i+1)%len(colors)]}" dur="10s" repeatCount="indefinite" /></stop>'
    gradient += '</linearGradient>'
    svg_lines.append(gradient)
    svg_lines.append('<circle id="nucleus" cx="100" cy="100" r="15" fill="url(#grad)" />')
        
    # disegna l'orbita dell'atomo
    svg_lines.append('<circle cx="100" cy="100" r="%d" fill="none" stroke="blue" />' % orbit_radius)
    #scrivo il nome dell'elemento al centro
    svg_lines.append(f'<text x="100" y="105" font-size="15" fill="black" text-anchor="middle" >{element_name}</text>')
    # disegna gli elettroni che orbitano attorno all'atomo
    for i in range(num_electrons):
        svg_lines.append('<circle id="elettrone%d" cx="%d" cy="%d" r="%d" fill="yellow" />' % (i, orbit_points[0][0], orbit_points[0][1], electron_radius))
        svg_lines.append('<animateTransform xlink:href="#elettrone%d" attributeName="transform" attributeType="XML" type="rotate" from="%d 100 100" to="%d 100 100" dur="%.2f" repeatCount="indefinite" />' % (i, el_offset*i, (360+(el_offset*i)), electron_speed))
        #svg_lines.append(f'<animateTransform xlink:href="#elettrones{str(i)}" attributeName="transform" attributeType="XML" type="rotate" from="0 100 100" to="360 100 100" dur="{str(electron_speed)}" repeatCount="indefinite" />')
    # definisce l'animazione per gli elettroni
    

    # chiude il documento SVG
    svg_lines.append('</svg>')

    # salva il documento SVG in un file
    with open(filename, 'w') as f:
        f.write('\n'.join(svg_lines))

# Filename 
# 1 ==> Number of electrons
# 2 ==> Orbit Radius
# 3 ==> Electron radius
# 4 ==> electron speed
# 5 ==> Element name 
#            file     | 1|  2| 3| 4|   5|
create_svg('atomo.svg', 2, 40, 3, 5, 'He')
