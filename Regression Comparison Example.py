#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

prediction1 = pd.read_csv('prediction_results1.csv', names = ['BranchId', 'Date', 'Stock Sales', 'Prediction 1', 'NA'],
                              header = 0)
prediction2 = pd.read_csv('prediction_results2.csv', names = ['BranchId', 'Date', 'Total Sales', 'Prediction 2', 'NA'],
                              header = 0)
del prediction1['NA'], prediction2['NA']

#merge tables
prediction_comp = pd.merge(prediction1, prediction2, how = 'inner', on = ['BranchId', 'Date'])

#create comparison columns
prediction_comp['Diff 1'] = prediction_comp['Stock Sales'] - prediction_comp['Prediction 1']
prediction_comp['Diff 2'] = prediction_comp['Total Sales'] - prediction_comp['Prediction 2']
prediction_comp['Abs Diff 1'] = abs(prediction_comp['Stock Sales'] - prediction_comp['Prediction 1'])
prediction_comp['Abs Diff 2'] = abs(prediction_comp['Total Sales'] - prediction_comp['Prediction 2'])
prediction_comp['Percent Diff 1'] = prediction_comp['Abs Diff 1'] / prediction_comp['Stock Sales']
prediction_comp['Percent Diff 2'] = prediction_comp['Abs Diff 2'] / prediction_comp['Total Sales']

prediction_comp['Date'] = pd.to_datetime(prediction_comp['Date'])
prediction_comp.sort_values(by=['Date'])
print(prediction_comp)


# In[2]:


print("Summary Statistics\n")
print("Prediction 1")
print("Sum of Differences: ", prediction_comp['Diff 1'].sum())
print("Sum of Abs Differences: ", prediction_comp['Abs Diff 1'].sum())
print("Average Percent Difference: ", prediction_comp['Percent Diff 1'].mean())
print("Median Percent Difference: ", prediction_comp['Percent Diff 1'].median())
print()
print("Prediction 2")
print("Sum of Differences: ", prediction_comp['Diff 2'].sum())
print("Sum of Abs Differences: ", prediction_comp['Abs Diff 2'].sum())
print("Average Percent Difference: ", prediction_comp['Percent Diff 2'].mean())
print("Median Percent Difference: ", prediction_comp['Percent Diff 2'].median())


# In[3]:


print("Percent Difference Counts\n")
print("Prediction 1")
print("All: ", prediction_comp['Percent Diff 1'].count())
print("0-5%: ", prediction_comp[(prediction_comp['Percent Diff 1'] > 0) & (prediction_comp['Percent Diff 1'] <= .05)].shape[0])
print("5-10%: ", prediction_comp[(prediction_comp['Percent Diff 1'] > 0.05) & (prediction_comp['Percent Diff 1'] <= .1)].shape[0])
print("10-20%: ", prediction_comp[(prediction_comp['Percent Diff 1'] > 0.1) & (prediction_comp['Percent Diff 1'] <= .2)].shape[0])
print("20-50%: ", prediction_comp[(prediction_comp['Percent Diff 1'] > 0.2) & (prediction_comp['Percent Diff 1'] <= .5)].shape[0])
print(">50%: ", prediction_comp[prediction_comp['Percent Diff 1'] > 0.5].shape[0])

print()
print("Prediction 2")
print("All: ", prediction_comp['Percent Diff 2'].count())
print("0-5%: ", prediction_comp[(prediction_comp['Percent Diff 2'] > 0) & (prediction_comp['Percent Diff 2'] <= .05)].shape[0])
print("5-10%: ", prediction_comp[(prediction_comp['Percent Diff 2'] > 0.05) & (prediction_comp['Percent Diff 2'] <= .1)].shape[0])
print("10-20%: ", prediction_comp[(prediction_comp['Percent Diff 2'] > 0.1) & (prediction_comp['Percent Diff 2'] <= .2)].shape[0])
print("20-50%: ", prediction_comp[(prediction_comp['Percent Diff 2'] > 0.2) & (prediction_comp['Percent Diff 2'] <= .5)].shape[0])
print(">50%: ", prediction_comp[prediction_comp['Percent Diff 2'] > 0.5].shape[0])

