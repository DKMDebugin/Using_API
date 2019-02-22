 # This module creates a visualization for the data gotten from hn_submission.py to be stored in a json file

import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


filename = 'submission-dicts.json'

# read from json file
submission_dicts = []
with open(filename) as f:
    submission_dicts = json.load(f)

title, submission_datas = [], []
for submission_dict in submission_dicts:
    # build title List
    title.append(submission_dict['title'])

    if not submission_dict['comments'] == 0:
        # build submission data
        submission_data = {
            'value': submission_dict['comments'],
            'label': submission_dict['title'],
            'xlink': submission_dict['link']
        }

        # add to submission list
        submission_datas.append(submission_data)


# make visualization
my_style = LS('#336', base_style=LCS)
#
# create configuration
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 2
my_config.major_label_font_size = 18 # y-axis label that mark increments of 5000
my_config.truncate_label = 5 # truncate longer names than 15
my_config.show_y_guides = False # hides horizontal lines
my_config.width = 1000

# visualization instance
bar_chart = pygal.Bar(my_config, style=my_style)
# visualization settings
bar_chart.title = 'Active Discussions Happening on Hacker News'
bar_chart.x_labels = title


bar_chart.add('', submission_datas)

bar_chart.render_to_file('hn_submission.svg')
