import pandas as pd


df = pd.read_csv("student.csv")
df['Pass/Fail'] = None
df2 = pd.read_csv("grading.csv")

for i in range(0,len(df)):
	if df2.loc[i,'Grading'] > 30 :
		df.loc[i,'Pass/Fail'] = "Pass"
	else:
		df.loc[i,'Pass/Fail'] = 'Fail'
df.to_csv('student.csv')