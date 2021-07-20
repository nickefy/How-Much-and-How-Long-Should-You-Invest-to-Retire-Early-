import pandas as pd

# Standard plotly imports
import plotly as py
import plotly.tools as tls
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import cufflinks

# Using plotly + cufflinks in offline mode
init_notebook_mode(connected=True)
cufflinks.go_offline(connected=True)

# Using Jupyter Notebook
# Plotting snp500 data
df = pd.read_csv("C:/Nick/Excel Files/csv/snp500.csv", nrows=15000)
df = df[['Year','Average Closing Price','Year Open','Year Close','Annual Returns','10 Year Rolling Returns','15 Year Rolling Returns','20 Year Rolling Returns']]

## adding a column with colors
df["Annual Returns Int"] = df['Annual Returns'].str.rstrip('%').astype('float') / 100.0
df["Color"] = np.where(df["Annual Returns Int"]<0, 'indianred', 'limegreen')

# Plot
fig = go.Figure()
fig.add_trace(
    go.Bar(name='Net',
           x=df['Year'],
           y=df['Annual Returns Int'],
           marker_color=df['Color']))
fig.update_layout(barmode='stack')
fig.update_layout(title = 'S&P500 - Historical Annual Returns')
fig.show()


# Plotting inflation data
df = pd.read_csv("C:/Nick/Excel Files/csv/inflationUS.csv", nrows=15000)
df = df[['Year','Inflation Rate (%)','Annual Change']]
## adding a column with colors
df["Inflation Rate Int"] = df['Inflation Rate (%)'].str.rstrip('%').astype('float') / 100.0
df["Color"] = np.where(df["Inflation Rate Int"]<0, 'limegreen', 'indianred')

# Plot
fig = go.Figure()
fig.add_trace(
    go.Bar(name='Net',
           x=df['Year'],
           y=df['Inflation Rate Int'],
           marker_color=df['Color']))
fig.update_layout(barmode='stack')
fig.update_layout(title = 'Inflation Rate (US)')
fig.show()

# Plotting Expense vs Returns

df = pd.read_csv("C:/Nick/Excel Files/csv/simulation.csv")
df2 = pd.read_csv("C:/Nick/Excel Files/csv/simulation50.csv")
df3 = pd.read_csv("C:/Nick/Excel Files/csv/simulation70.csv")


data= [
go.Scatter(x=df['Date'], y=df['Expenses with Inflation'],
                mode='lines',
                name='Inflated Expense'),
go.Scatter(x=df['Date'], y=df['Annual Returns'],
                    mode='lines+markers',
                    name='Annual Returns'),
go.Scatter(x=df['Date'], y=df2['Expenses with Inflation'],
                mode='lines',
                name='Inflated Expense'),
go.Scatter(x=df['Date'], y=df2['Annual Returns'],
                    mode='lines+markers',
                    name='Annual Returns'),
go.Scatter(x=df['Date'], y=df3['Expenses with Inflation'],
                mode='lines',
                name='Inflated Expense'),
go.Scatter(x=df['Date'], y=df3['Annual Returns'],
                    mode='lines+markers',
                    name='Annual Returns'),]

#defining list_updatemenus
list_updatemenus = [{'label': 'Invest 30%',
  'method': 'update',
  'args': [{'visible': [True, True, False, False, False, False]}, {'title': '(Annual) Inflated Expense vs Investment Returns'}]},
 {'label': 'Invest 50%',
  'method': 'update',
  'args': [{'visible': [False, False, True, True, False, False]}, {'title': '(Annual) Inflated Expense vs Investment Returns'}]},
  {'label': 'Invest 70%',
  'method': 'update',
  'args': [{'visible': [False, False, False, False, True, True]}, {'title': '(Annual) Inflated Expense vs Investment Returns'}]}]

#defining layout
layout=go.Layout(title='Yearly Expense vs Annual Returns over 10 Years',updatemenus=list([dict(buttons= list_updatemenus)]))
#defining figure and plotting
fig = go.Figure(data, layout)
iplot(fig)