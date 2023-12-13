import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col=0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col=0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)


#---------------PLOT ONE--------------------
#For subject GTEX-113JC, plot the distribution of expression (logged normalized counts) across all genes, excluding any genes with 0 counts.

# subject = counts_df_logged.loc["GTEX-113JC", :]
# subject = subject.astype(float)

# subject_filtered = subject[subject > 0.0]

# print(subject_filtered)


# plt.hist(subject_filtered, bins=50)
# plt.xlabel("Expression Level (logged normalized counts)")
# plt.ylabel("Number of Genes")
# plt.show()

#----------------PLOT TWO----------------
#For the gene MXD4, plot the distribution of expression 
#(logged normalized counts) in males versus females.

# gene = full_design_df.loc[:, ["MXD4", "SEX"]]

# males = gene.loc[gene.loc[:, "SEX"]==1, "MXD4"]
# females = gene.loc[gene.loc[:, "SEX"]==2, "MXD4"]

# plt.hist(males, bins=50, color='blue', alpha=0.5, label="male")
# plt.hist(females, bins=50, color='red', alpha=0.5, label="female")
# plt.xlabel("Expression Level (logged normalized counts)")
# plt.ylabel("Number of Genes")
# plt.legend()
# plt.show()

#----------------PLOT THREE-------------
#Plot the number of subjects in each age category.

# sixty_sixtynine = full_design_df.loc[full_design_df.loc[:, "AGE"]=="60-69", "AGE"]
# fifty_fiftynine = full_design_df.loc[full_design_df.loc[:, "AGE"]=="50-59", "AGE"]
# twenty_twentynine = full_design_df.loc[full_design_df.loc[:, "AGE"]=="20-29", "AGE"]
# thirty_thirtynine = full_design_df.loc[full_design_df.loc[:, "AGE"]=="30-39", "AGE"]
# seventy_seventynine = full_design_df.loc[full_design_df.loc[:, "AGE"]=="70-79", "AGE"]
# forty_fortynine = full_design_df.loc[full_design_df.loc[:, "AGE"]=="40-49", "AGE"]


# data = {'20-29':len(twenty_twentynine), '30-39':len(thirty_thirtynine), '40-49':len(forty_fortynine), '50-59':len(fifty_fiftynine), '60-69':len(sixty_sixtynine), '70-79':len(seventy_seventynine)}
# print(data)

# names = list(data.keys())
# values = list(data.values())
# plt.bar(range(len(data)), values, tick_label=names)
# plt.xlabel("Age Group")
# plt.ylabel("Number of Subjects")
# plt.show()

#---------------PLOT FOUR--------------- 
#For the gene LPXN, plot the median expression (logged normalized counts) 
#over time (i.e. in each age category), stratified by sex.

gene = full_design_df.loc[:, ["LPXN", "SEX", "AGE"]]


males = gene.loc[gene.loc[:, 'SEX'] == 1, :]
females = gene.loc[gene.loc[:, 'SEX'] == 2, :]

sixty_sixtynine = males.loc[males.loc[:, "AGE"]=="60-69", "LPXN"]
fifty_fiftynine = males.loc[males.loc[:, "AGE"]=="50-59", "LPXN"]
twenty_twentynine = males.loc[males.loc[:, "AGE"]=="20-29", "LPXN"]
thirty_thirtynine = males.loc[males.loc[:, "AGE"]=="30-39", "LPXN"]
seventy_seventynine = males.loc[males.loc[:, "AGE"]=="70-79", "LPXN"]
forty_fortynine = males.loc[males.loc[:, "AGE"]=="40-49", "LPXN"]

f_sixty_sixtynine = females.loc[females.loc[:, "AGE"]=="60-69", "LPXN"]
f_fifty_fiftynine = females.loc[females.loc[:, "AGE"]=="50-59", "LPXN"]
f_twenty_twentynine = females.loc[females.loc[:, "AGE"]=="20-29", "LPXN"]
f_thirty_thirtynine = females.loc[females.loc[:, "AGE"]=="30-39", "LPXN"]
f_seventy_seventynine = females.loc[females.loc[:, "AGE"]=="70-79", "LPXN"]
f_forty_fortynine = females.loc[females.loc[:, "AGE"]=="40-49", "LPXN"]


data = {'20-29': twenty_twentynine.median(), '30-39': thirty_thirtynine.median(),
        '40-49': forty_fortynine.median(), '50-59': fifty_fiftynine.median(),
        '60-69': sixty_sixtynine.median(), '70-79': seventy_seventynine.median()}

f_data = {'20-29': f_twenty_twentynine.median(), '30-39': f_thirty_thirtynine.median(),
          '40-49': f_forty_fortynine.median(), '50-59': f_fifty_fiftynine.median(),
          '60-69': f_sixty_sixtynine.median(), '70-79': f_seventy_seventynine.median()}


log_values = {key: np.log(value) for key, value in data.items()}
log_f_values = {key: np.log(value) for key, value in f_data.items()}


log_values_array = np.array(list(log_values.values())).reshape(-1, 1)
log_f_values_array = np.array(list(log_f_values.values())).reshape(-1, 1)

scaler = MinMaxScaler()
norm_values = scaler.fit_transform(log_values_array).flatten()
norm_f_values = scaler.fit_transform(log_f_values_array).flatten()


names = list(log_values.keys())

bar_width = 0.35
bar_positions1 = np.arange(len(log_values))
bar_positions2 = [pos + bar_width for pos in bar_positions1]


plt.bar(bar_positions1, norm_values, bar_width, label='Males')
plt.bar(bar_positions2, norm_f_values, bar_width, label='Females')


plt.xlabel('Age Group')
plt.ylabel('Normalized Log-Transformed Median Values')
plt.title('Normalized Log-Transformed Median Expression Values of LPXN')
plt.xticks([pos + bar_width / 2 for pos in bar_positions1], names)


plt.legend()


plt.show()
