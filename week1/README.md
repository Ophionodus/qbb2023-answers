Step 2.2

 0.3776 is the coefficient for the relationship between Mother Age and number of de novo mutations, which represents the 'size' of this relationship. It is the slope of the relationship between the independent variable (age) and the dependent variable (number of DNMs). This does match up with the plot from step 2.1, which does seem to show a positive slope of about that magnitude.
 
 
 This relationship does seem to be significant; the p value is shown as 0.000, and is therefore much smaller than 0.05, indicating a statistically significant difference.
 
 
 Step 2.3
 
 The coefficient for the relationship between father age and number of DNMs is 1.3538, indicating that fathers contribute more DNMs with greater age as compared to mothers. This matches up with the plot, which shows a steeper relationship and seems to follow a pattern of roughly 1.3 more DNMs for each year of age.
 
 This relationship is also significant, as the p value is shown as 0.000.
 
 
 Step 2.4 
 
 I got a prediction of 78.695457 DNMs. I got this answer by using the predict function of statsmodels, using this code: 
new_observation = pd.DataFrame({"Father_age" : [50.5]})
print(model2.predict(new_observation))


Step 2.6

I chose an independent t-test, because we are dealing with two independent distributions in separate groups and trying to determine if they are statistically different.

 I got a p-value of 2.1986031793078793e-264, indicating that there is an infinitesimally small probability that the difference between groups is due to chance. Therefore, the test result was statistically significant. This indicates that this data suggests that fathers contribute significantly more DNMs to their probands than mothers.