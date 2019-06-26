import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['Love', 'Buv', 'Cuv', 'Duv']
ibu_values=[35, 60, 85, 75]
abv_values=[36, 70, 80, 69]
color1='lightblue'
color2='darkgreen'

bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name='Sam',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name='Jess',
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Sam/Jess relationship - aka how much we do each of the following things'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Hi Billy'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href='https://github.com/austinlasseter/flying-dog-beers'),
    html.Br(),
    html.A('Data Source', href='https://www.flyingdog.com/beers/'),
    ]
)

if __name__ == '__main__':
    app.run_server()
