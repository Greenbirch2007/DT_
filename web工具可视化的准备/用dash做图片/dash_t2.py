# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
} # 定义颜色

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children=u'你好 Dash',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
    ), #设置字体背景颜色，设置字体颜色

    html.Div(children='''Dash: 一个基于Python的Web应用框架''', style={
        'textAlign': 'center',
        'color': colors['text']
    }), #设置字体居中，设置字体颜色

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': u'水果'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'蔬菜'},
            ],
            'layout': {
                'title': 'Dash 数据可视化',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
]) #设置绘图背景为黑色，设置其他区域背景为黑色

if __name__ == '__main__':
    app.run_server(debug=True)
