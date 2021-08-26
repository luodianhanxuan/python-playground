import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import ts

app = dash.Dash('Hello World')

px.line()

app.layout = html.Div([
    html.H1("股票日行情"),
    dcc.Input(id='stock_id1', value="600036.SH", type='text'),
    dcc.Graph(id='stock_daily', figure="fig"),
])


@app.callback(Output('stock_daily', 'figure'),
              [
                  Input('stock_id1', 'value'),
              ])
def update_graph(stock_id1):
    stk1_basic = ts.api.stock_basic(ts_code=stock_id1)
    stk1_daily = ts.api.daily(ts_code=stock_id1)
    stk1_daily = stk1_daily.iloc[::-1]
    lst = [datetime.datetime.strptime(i, '%Y%m%d') for i in stk1_daily.trade_date]
    return {
        'data': [
            {
                'x': pandas.Series(lst),
                'y': stk1_daily['close'],
                'name': stk1_basic.loc[0, 'name'] + str("收盘价"),

            },
            {
                'x': pandas.Series(lst),
                'y': stk1_daily['open'],
                'name': stk1_basic.loc[0, 'name'] + str("开盘价"),
                "yaxis": 'y2'
            }

        ],
        'layout': go.Layout(
            title='股票开收盘',
            yaxis=dict(
                title='收盘'
            ),
            yaxis2=dict(
                title='开盘',
                # titlefont=dict(
                #     color='rgb(148, 103, 189)'
                # ),
                # tickfont=dict(
                #     color='rgb(148, 103, 189)'
                # ),
                overlaying='y',
                side='right'
            )
        )
    }

    # app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


if __name__ == '__main__':
    app.run_server()
