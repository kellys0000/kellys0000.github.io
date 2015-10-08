#bar graph to show the categories used by each party FOR ALL YEARS COMBiNED

import plotly.plotly as py
from plotly.graph_objs import *
import sys
from collections import defaultdict

#Plotly account info..
py.sign_in("kellys0000","5crb1ipjk0")

#create data structure
data_dict = defaultdict(dict)

data_file = open(sys.argv[1],'r')
for line in data_file:
    split_line = line.split('\t')
    category = int(split_line[0])
    word = split_line[1]
    party_info = split_line[2:]
    for party in party_info:
        split_party_info = party.split(':')
        party_name = split_party_info[0]
        amount = len(split_party_info[1].split(','))
        if party_name in data_dict[category].keys():
            data_dict[category][party_name] += amount
        else:
            data_dict[category][party_name] = amount

print data_dict

category_names_dict = {1:'Healthcare',
                       2:'Education',
                       3:'Equality',
                       4:'Class equality',
                       5:'Labor issues',
                       6:'Business',
                       7:'Foreign policy',
                       8:'Crime/legal system',
                       9:'Environment',
                       10:'Taxes',
                       11:'Welfare',
                       12:'Innovation/future',
                       13:'Economy',
                       16:'Immigration',
                       17:'Infrastructure/housing',
                       18:'Youth/children',
                       19:'Elderly',
                       20:'Rural/urban',
                       22:'Culture',
                       23:'Family',
                       24:'Democracy',
                       25:'Peace/conflict',
                       26:'Freedom'}

reverse_category_names_dict = {'Healthcare':1,
                               'Education':2,
                               'Equality':3,
                               'Class equality':4,
                               'Labor issues':5,
                               'Business':6,
                               'Foreign policy':7,
                               'Crime/legal system':8,
                               'Environment':9,
                               'Taxes':10,
                               'Welfare':11,
                               'Innovation/future':12,
                               'Economy':13,
                               'Immigration':16,
                               'Infrastructure/housing':17,
                               'Youth/children':18,
                               'Elderly':19,
                               'Rural/urban':20,
                               'Culture':22,
                               'Family':23,
                               'Democracy':24,
                               'Peace/conflict':25,
                               'Freedom':26}

##### CREATE X & Y AXES)
def create_y(category_names_dict):
    """y axis is list of categories (in numerical order)"""
    y_list = []
    for x in range(1,27):
        if x in category_names_dict.keys():
            y_list.append(category_names_dict[x])
    return y_list

#create_y(category_names_dict)

def create_x(y, name, reverse_category_names_dict, data_dict):
    x = []
    for cat_name in y:
        cat_code = int(reverse_category_names_dict[cat_name])
#        print 'CAT CODE: ' + str(cat_code)
        if name not in data_dict[cat_code].keys():
#            print 'no value for ' + name
            x.append(0)
        else:
            #print data_dict[cat_code][name]
            x.append(data_dict[cat_code][name])
    return x
################

y_axis = create_y(category_names_dict)
for x in y_axis:
    print x
#name = 'c'

#print create_x(y, name, reverse_category_names_dict, data_dict)

####### BEGIN CREATING GRAPH #############
### one trace for each party
lower_name = 'c'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
trace1 = Bar(
    y = y_axis,
    name = 'C',
    x = x_axis,
    orientation = 'h',
    marker = Marker(
        color = 'rgba(55, 128, 191, 0.6)',
        line = Line(
            color = 'rgba(55, 128, 191, 1.0)',
            width = 1,
        )
    )
)

lower_name = 'fp'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
trace2 = Bar(
    y = y_axis,
    name='FP',
    x = x_axis,
    orientation = 'h',
    marker = Marker(
        color = 'rgba(255, 153, 51, 0.6)',
        line = Line(
            color = 'rgba(255, 153, 51, 1.0)',
            width = 1,
        )
    )
)

lower_name = 'kd'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
trace3 = Bar(
    y = y_axis,
    name='KD',
    x = x_axis,
    orientation = 'h',
    marker = Marker(
        color = 'rgba(155, 100, 51, 0.6)',
        line = Line(
            color = 'rgba(255, 153, 51, 1.0)',
            width = 1,
        )
    )
)

lower_name = 'm'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
trace4 = Bar(
    y = y_axis,
    name='M',
    x = x_axis,
    orientation = 'h',
    marker = Marker(
        color = 'rgba(255, 153, 100, 0.6)',
        line = Line(
            color = 'rgba(255, 153, 51, 1.0)',
            width = 1,
        )
    )
)

lower_name = 's'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
trace5 = Bar(
    y = y_axis,
    x = x_axis,
    name='S',
    orientation = 'h',
    marker = Marker(
        color = 'rgba(255, 153, 51, 0.6)',
        line = Line(
            color = 'rgba(255, 153, 51, 1.0)',
            width = 1,
        )
    )
)

print '-------MP-------'
lower_name = 'mp'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
print x_axis
trace6 = Bar(
    y = y_axis,
    name='MP',
    x = x_axis,
    orientation = 'h',
    marker = Marker(
        color = 'rgba(255, 153, 51, 0.6)',
        line = Line(
            color = 'rgba(255, 153, 51, 1.0)',
            width = 1,
        )
    )
)

lower_name = 'v'
x_axis = create_x(y_axis, lower_name, reverse_category_names_dict, data_dict)
trace7 = Bar(
    y = y_axis,
    name='V',
    x = x_axis,
    orientation = 'h',
    marker = Marker(
        color = 'rgba(255, 153, 51, 0.6)',
        line = Line(
            color = 'rgba(255, 153, 51, 1.0)',
            width = 1,
        )
    )
)



data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
layout = Layout(
    barmode='stack'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='marker-h-bar')






