import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
reminded_savings=[]
not_reminded_savings=[]
all_savings=[]
with open("data_story.csv",newline="")as f:
    reader=csv.reader(f)
    savings=list(reader)
savings.pop(0)
total_entry=len(savings)
people_given_reminder=0
for i in savings:
    all_savings.append(float (i[0]))
    if(int (i[3])==1):
        reminded_savings.append(float(i[0]))
        people_given_reminder=people_given_reminder+1
    else:
        not_reminded_savings.append(float(i[0]))
fig=go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[people_given_reminder,(total_entry - people_given_reminder)]))
fig.show()  


#mean of the reminded savings
reminded_mean=statistics.mean(reminded_savings)
print("Mean of the reminded_mean:")
print(reminded_mean)

#median of the reminded savings
reminded_median=statistics.median(reminded_savings)
print("Median of the reminded_median:")
print(reminded_median)

#mode of the reminded savings
reminded_mode=statistics.mode(reminded_savings)
print("Mode of the reminded_mode:")
print(reminded_mode)

#standard deviation of the reminded savings
reminded_std_dev=statistics.stdev(reminded_savings)
print("Standard_Deviation of the reminded_std_dev:")
print(reminded_std_dev)

#mean of all savings
all_savings_mean=statistics.mean(all_savings)
print("Mean of the all_savings:")
print(all_savings_mean)

#median of all savings
all_savings_median=statistics.median(all_savings)
print("Median of the all_savings:")
print(all_savings_median)

#mode of all savings
all_savings_mode=statistics.mode(all_savings)
print("Mode of the all_savings:")
print(all_savings_mode)

#Standard deviation of all savings
all_savings_std_dev=statistics.stdev(all_savings)
print("Standard Deviation of the all_savings:")
print(all_savings_std_dev)


#mean of the not reminded savings
not_reminded_mean=statistics.mean(not_reminded_savings)
print("Mean of the not_reminded_mean:")
print(not_reminded_mean)

#median of the not_reminded savings
not_reminded_median=statistics.median(not_reminded_savings)
print("Median of the not_reminded_median:")
print(not_reminded_median)

#mode of the not_reminded savings
not_reminded_mode=statistics.mode(not_reminded_savings)
print("Mode of the not_reminded_mode:")
print(not_reminded_mode)

#standard deviation of the not_reminded savings
not_reminded_std_dev=statistics.stdev(not_reminded_savings)
print("Standard_Deviation of the not_reminded_std_dev:")
print(not_reminded_std_dev)






       

