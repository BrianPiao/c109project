import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("StudentsPerformance.csv")
data = df ["reading score"].tolist()

mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
std = st.stdev(data)

first_std_start, first_std_end = mean-std, mean+std
second_std_start, second_std_end = mean-(2*std) , mean+(2*std)
third_std_start, third_std_end = mean-(3*std) , mean+(3*std)

fig = ff.create_distplot ([data],["reading score"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines+markers", name="MEAN" ))

fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0,0.17], mode="lines+markers", name="first_std_start"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0,0.17], mode="lines+markers", name="first_std_end"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0,0.17], mode="lines+markers", name="second_std_start"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0,0.17], mode="lines+markers", name="second_std_end"))
fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[0,0.17], mode="lines+markers", name="third_std_start"))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0,0.17], mode="lines+markers", name="third_std_end"))

fig.show()

data_within_1_std = [result for result in data if result > first_std_start and result < first_std_end]
data_within_2_std = [result for result in data if result > second_std_start and result < second_std_end]
data_within_3_std = [result for result in data if result > third_std_start and result < third_std_end]


print("Mean of the data is ---> {} ".format( mean ) )
print("Median of the data is ---> {} ".format( median ) )
print("Mode of the data is ---> {} ".format( mode ) )
print("Standard Dev of the data is ---> {} ".format( std ) )
print("\n")
print("{} % of data lies within 1st standard deviation".format( len(data_within_1_std) * 100.0/len(data) ) )
print("{} % of data lies within 2nd standard deviation".format( len(data_within_2_std) * 100.0/len(data) ) )
print("{} % of data lies within 3rd standard deviation".format( len(data_within_3_std) * 100.0/len(data) ) )