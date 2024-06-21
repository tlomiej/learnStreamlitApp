import plotly.express as px


def make_choropleth(input_df,input_color_theme, selected_column_id, selected_column_value, geojsondata):
    fig = px.choropleth(
        input_df,
        geojson=geojsondata,
        locations='Kod',
        featureidkey='properties.kod',
        color=selected_column_value,
        color_continuous_scale=input_color_theme,
        range_color=(min(input_df[selected_column_value]), max(input_df[selected_column_value])),
        labels={selected_column_value: 'Value'},
        projection="mercator"
    )

    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350,
        geo=dict(
            projection_scale=6,
            center={"lat": 52, "lon": 19},
            visible=True
        )

    )

    return fig