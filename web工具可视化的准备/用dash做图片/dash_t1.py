# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children=u'你好 Dash'),

    html.Div(children='''
        Dash: 一个基于Python的Web应用框架
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': u'学生'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'老师'},
            ],
            'layout': {
                'title': 'Dash 数据可视化'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)  # debug=True, hot reload is enabled
    #app.run_server(dev_tools_hot_reload=False) #dev_tools_hot_reload=False, hot reload ie disabled
