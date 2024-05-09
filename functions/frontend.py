import polyline
import folium


def generate_heatmap(activity_data: list, frontend_filename: str):

    # Generate folium map object
    m = folium.Map(tiles='cartodb positron',
                   location=[52.4837, -3.5],
                   zoom_start=7)

    # Iterate through activities
    for activity in activity_data:

        # Collect and decode activity polyline
        curve = activity["polyline"]
        data = polyline.decode(curve)

        # Plot gps data on map object
        folium.PolyLine(data,
                        color='#fc4c02',
                        weight=2,
                        opacity=1,
                        tooltip=activity['name']).add_to(m)

        # Add marker to map object based on activity starting position
        folium.Marker(location=activity['start_latlng']).add_to(m)

    m.save(frontend_filename)
