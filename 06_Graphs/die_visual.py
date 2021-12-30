from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


# Create a D6.
die = Die()

# Make some rolls and store the result in a list
results = []
for rol_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the result
frecuencies = []
for value in range(1, die.num_sides+1):
    frecuency = results.count(value)
    frecuencies.append(frecuency)

# Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frecuencies)]
x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of results'}

m_layout = Layout(title='Result of rolling D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': m_layout}, filename='d6.html')


print(frecuencies) 
