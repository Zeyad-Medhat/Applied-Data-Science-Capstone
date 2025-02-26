# Import required libraries
import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center',
                                               'color': '#503D36',
                                               'font-size': 40}
                                               ),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site_dropdown',
                                                options=[
                                                    {'label': 'All Sites', 'value': 'ALL'},
                                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'}
                                                ],
                                                value='ALL',
                                                placeholder="Select Launch Site",
                                                searchable=True
                                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                min=0, max=10000, step=1000,
                                marks={0: '0',
                                    2500: '2500',
                                    5000: '5000',
                                    7500: '7500',
                                    10000: '10000'},
                                value=[0, 10000]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site_dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Filter the dataframe to show only successful launches (class == 1)
        successful_launches = spacex_df[spacex_df['class'] == 1]
        
        # Group by Launch Site and count the number of successful launches
        pie_data = successful_launches.groupby('Launch Site').size().reset_index(name='count')
        
        # Create the pie chart for successful launches per site
        fig = px.pie(pie_data, 
                     names='Launch Site',  # Launch sites are the categories
                     values='count',       # Count of successful launches per site
                     title="Total Success Launches by Site")
        
    else:
        # Filter by the selected site - show the success/failure distribution
        pie_data = spacex_df[spacex_df['Launch Site'] == entered_site].groupby('class').size().reset_index(name='count')
        
        # Create the pie chart for success/failure distribution for the selected site
        fig = px.pie(pie_data, 
                     names='class',  # Use 'class' for the pie chart (0: failure, 1: success)
                     values='count',  # Count the number of successful and failed launches
                     title=f"Total Success Launches for site {entered_site}")
        
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site_dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_plot(selected_site, payload_range):
    min_payload, max_payload = payload_range
    
    # Filter by the selected payload range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= min_payload) & 
                             (spacex_df['Payload Mass (kg)'] <= max_payload)]
    
    if selected_site == 'ALL':
        # If "ALL" sites are selected, show scatter for all sites
        fig = px.scatter(filtered_df, 
                         x='Payload Mass (kg)', 
                         y='class', 
                         color='Booster Version Category', 
                         title='Correlation between Payload and success for All Sites',
                         labels={'Payload Mass (kg)': 'Payload Mass (kg)', 'class': 'Launch Outcome'},
                         category_orders={'class': [0, 1]})
    else:
        # If a specific site is selected, filter the data by site
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(filtered_df, 
                         x='Payload Mass (kg)', 
                         y='class', 
                         color='Booster Version Category', 
                         title=f'Correlation between Payload and success for {selected_site}',
                         labels={'Payload Mass (kg)': 'Payload Mass (kg)', 'class': 'Class'},
                         category_orders={'class': [0, 1]})
    
    return fig
# Run the app
if __name__ == '__main__':
    app.run_server(debug= True,port=8050)
