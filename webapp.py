from functions.frontend import generate_heatmap
import webbrowser
import json

# Define Frontend File Name
frontend_filename = 'welsh_coastal_path_heatmap.html'

# Load in frontend data
with open('welsh_coastal_path_segments.json') as f:
    wcp_data = json.load(f)

# Generate frontend visuals
generate_heatmap(wcp_data, frontend_filename)
webbrowser.open(frontend_filename)
