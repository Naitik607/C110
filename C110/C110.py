import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

mean = st.mean(data)
print("population mean:-",mean)
std_dev = st.stdev(data)

dataset = []

for i in range(0,100):
  random_index = random.randint(0,len(data))
  value = data[random_index]
  dataset.append(value)

mean = st.mean(dataset)
std_dev = st.stdev(dataset)
 
def random_set_of_mean(counter):
  dataset = []
  for i in range(0,counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)

  mean = st.mean(dataset)

  return mean

def show_fig(mean_list):
  df = mean_list
  mean = st.mean(df)
  fig = ff.create_distplot([df],["reading_time"],show_hist=False)
  fig.add_trace(go.Scatter(x=[mean,mean],y=[0.1],mode="lines",name = "MEAN"))
  fig.show()

def setup():
  mean_list = []
  for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

  show_fig(mean_list)
  mean = st.mean(mean_list)
  print("sampling mean:-",mean)

setup()