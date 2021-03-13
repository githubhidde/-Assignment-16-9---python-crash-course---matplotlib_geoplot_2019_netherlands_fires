import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# My system gets stressed if I read the entire file, so I set this limit.
num_rows = 5_000

# Explore the structure of the data.
dates = []
filename = '2019_netherlands_fires.csv'
with open(filename, encoding="utf8") as file:
	reader = csv.reader(file)
	header_row = next(reader)

	# print(header_row)

	latitude, longitude, brightness, hover_texts = [], [], [], []
	row_num = 0
	for row in reader:
		lat = float(row[0])
		lon = float(row[1])
		bright = float(row[2])
		date = row[5]
		time = row[6]
		time = time[0:2] + ":" + time[2:4]
		latitude.append(lat)
		longitude.append(lon)
		brightness.append(bright)
		hover_texts.append(date + " measured time " + time)

		row_num += 1
		if row_num == num_rows:
			break

# Map the world fires.
data = [{
	'type': 'scattergeo',
	'lon': longitude,
	'lat': latitude,
	'text': hover_texts,
	'marker': {
		'size': [bright/10 for bright in brightness],
		'color': brightness,
		'colorscale': 'YlOrRd',
		'reversescale': True,
		'colorbar': {'title': 'Brightness'},
	'reversescale': False,
	},
}]

title = "Fires in the Netherlands(2019)."
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='2019_netherlands_fires.html')
