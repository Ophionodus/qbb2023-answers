#!/usr/bin/env python

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv("aau1043_dnm.csv")


dnmDict = {}

for dnm_i in df.index:
	pbid = df.loc[dnm_i, 'Proband_id']
	parent = df.loc[dnm_i, 'Phase_combined']

	if pbid not in dnmDict:
		dnmDict[pbid] = [0,0]

	if parent == 'father':
		dnmDict[pbid][1] += 1
	elif parent == 'mother':
		dnmDict[pbid][0] += 1

deNovoCountDF = pd.DataFrame.from_dict(dnmDict, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])

df2 = pd.read_csv("aau1043_parental_age.csv")
df2 = df2.set_index('Proband_id')
combined = pd.concat([deNovoCountDF,df2], axis=1, join='outer',)
#print(combined)
dads = {}
moms = {}
for proband in combined.index:
	dads[proband] = [combined.loc[proband, 'Father_age'], combined.loc[proband, 'paternal_dnm']]
	moms[proband] = [combined.loc[proband, 'Mother_age'], combined.loc[proband, 'maternal_dnm']]


# dadx = dads.values()
# for x in dadx:
# 	plt.scatter(x[0], x[1], c='b')
# plt.xlabel("Paternal Age")
# plt.ylabel("number of DNMs")
# plt.show()

# momx = moms.values()
# for x in momx:
# 	plt.scatter(x[0], x[1], c='r')
# plt.xlabel("Maternal Age")
# plt.ylabel("number of DNMs")
# plt.show()

# model = smf.ols(formula = "maternal_dnm ~ Mother_age", data = combined).fit()
# print(model.summary())

model2 = smf.ols(formula = "paternal_dnm ~ Father_age", data = combined).fit()

# new_observation = pd.DataFrame({"Father_age" : [50.5]})
# print(model2.predict(new_observation))

fig, ax = plt.subplots()
ax.hist(combined.loc[:, 'paternal_dnm'], label = "Paternal", bins = 30, alpha = 0.5)
ax.hist(combined.loc[:, 'maternal_dnm'], label = "Maternal", bins = 30, alpha = 0.5)
plt.legend()
plt.show()

ttestresult = sm.stats.ttest_ind(combined.loc[:, 'paternal_dnm'], combined.loc[:, 'maternal_dnm'], alternative='two-sided', usevar='pooled', weights=(None, None), value=0)
print(ttestresult)