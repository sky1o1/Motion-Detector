from motion import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource


df["start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%m:%s")
df["end_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%m:%s")
cds = ColumnDataSource(df)


p = figure(x_axis_type='datetime', height=200, width=550, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
# p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@start_string"), ("End", "@end_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)
output_file("Graph.html")

show(p)