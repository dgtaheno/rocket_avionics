import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import serial
import threading
import time
import plotly.graph_objs as go

# CSV file mode
DATA_FILE = "data.csv"

# Cargar datos del archivo (modo post-vuelo)
df = pd.read_csv(DATA_FILE)

# Crear la app Dash
app = dash.Dash(__name__)
app.title = "Rocket Avionics Dashboard"

# Diseño del dashboard
app.layout = html.Div([
    html.H1("🚀 Rocket Avionics Dashboard"),
    
    html.Div([
        html.Div([
            html.H4("📍 GPS Position"),
            dcc.Graph(id='map-plot')
        ], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.H4("📈 Altitude Over Time"),
            dcc.Graph(id='altitude-plot'),
        ], style={'width': '49%', 'display': 'inline-block'}),
    ]),

    html.Div([
        html.H4("📊 Acceleration Z (Vertical)"),
        dcc.Graph(id='acc-plot'),
    ]),

    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)  # Cada 1s
])

# Callback para actualizar gráficas
@app.callback(
    Output('map-plot', 'figure'),
    Output('altitude-plot', 'figure'),
    Output('acc-plot', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    df = pd.read_csv(DATA_FILE)  # Reload CSV
    fig_map = go.Figure(go.Scattergeo(
        lon = df['lon_deg'],
        lat = df['lat_deg'],
        mode = 'markers+lines',
        marker=dict(size=6),
    ))
    fig_map.update_geos(fitbounds="locations")
    fig_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

    fig_alt = go.Figure()
    fig_alt.add_trace(go.Scatter(x=df['timestamp_ms'], y=df['altitude_m'], name="Altitude"))
    fig_alt.update_layout(xaxis_title="Time (ms)", yaxis_title="Altitude (m)")

    fig_acc = go.Figure()
    fig_acc.add_trace(go.Scatter(x=df['timestamp_ms'], y=df['accZ_m_s2'], name="accZ"))
    fig_acc.update_layout(xaxis_title="Time (ms)", yaxis_title="Acc Z (m/s²)")

    return fig_map, fig_alt, fig_acc

# Ejecutar servidor local
if __name__ == '__main__':
    app.run(debug=True)
