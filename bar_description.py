# Testing the waters

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'process-design-primer', 'public-apis']

plot_dicts = [
    {"value": 62625, 'label':'Description of Awesome Python'},
    {"value": 57493, 'label':'Description of Process Design Primer'},
    {"value": 51476, 'label':'Description of Public APIs'}
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')
