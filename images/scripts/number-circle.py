import svgwrite
from svgwrite import cm, mm
import math

width=250
height=250
sw=1
cx=width/2.0
cy=height/2.0
segment_count = 8 
radius = min(width, height)/2.0-50
marker_length = 0.15*radius # in cm


dwg = svgwrite.Drawing('../number-circle-signed-binary.svg', profile='tiny', size=(f'{width}', f'{height}'),viewBox=(f'0 0 {width} {height}'))
shapes = dwg.add(dwg.g(id='shapes', fill='white'))

radius_str = str(radius)
circle = dwg.circle(center=(cx, cy), r=radius_str, stroke='black', stroke_width=sw)
shapes.add(circle)

label_group = svgwrite.container.Group(style='font-size:1rem;font-family:sans-serif;fill:black;dominant-baseline:central;text-anchor:middle;text-rendering:geometricPrecision')

segment_length = 2*math.pi/segment_count
for segment_number in range(0, segment_count):
    rad = segment_number*segment_length-math.pi/2.0
    
    sx = (radius-marker_length/2.0) * math.cos(rad) +cx
    sy = (radius-marker_length/2.0) * math.sin(rad) +cy
    ex = (radius+marker_length/2.0) * math.cos(rad) +cx
    ey = (radius+marker_length/2.0) * math.sin(rad) +cy

    lx = 1.2 * (radius+marker_length/2.0) * math.cos(rad) + cx
    ly = 1.2 * (radius+marker_length/2.0) * math.sin(rad) + cy

    llx = 1.4 * (radius+marker_length/2.0) * math.cos(rad) + cx
    lly = 1.4 * (radius+marker_length/2.0) * math.sin(rad) + cy    

#    label_line = dwg.line((ex, ey), (lx, ly), stroke='red', stroke_width=sw)
#    shapes.add(label_line)

    if segment_number > 3:
        label = dwg.text(str(f"-{(8-segment_number):03b}"), insert=(lx, ly))
    else:
        label = dwg.text(str(f"{segment_number:03b}"), insert=(lx, ly))
        
    label_group.add(label)
    shapes.add(label_group)
    
    line = dwg.line((sx, sy), (ex, ey), stroke='black', stroke_width=sw)
    shapes.add(line)



dwg.save()
