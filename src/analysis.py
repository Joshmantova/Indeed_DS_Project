import pandas as pd

list_of_locations = ['CO', 'CA', 'NY', 'WA', 'UT', 'FL']

df_CO = pd.read_csv('df_CO')
df_CA = pd.read_csv('df_CA')
df_NY = pd.read_csv('df_NY')
df_WA = pd.read_csv('df_WA')
df_UT = pd.read_csv('df_UT')
df_FL = pd.read_csv('df_FL')

# df_all = pd.concat(pd.read_csv('df_CO'), pd.read_csv('df_CA'), pd.read_csv('df_NY'), pd.read_csv('df_WA'), pd.read_csv('df_UT'), pd.read_csv('df_FL'))

list_of_dfs = []
for state in list_of_locations:
    list_of_dfs.append(f'df_{state}')

# for df in list_of_dfs:
#     pd.read_csv(df)

df_all = pd.concat((df_CO, df_CA, df_NY, df_WA, df_UT, df_FL))



print(df_all.reset_index())