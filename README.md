# Mini-Project IV: Supervised Learning  | Josh Ho

### [Assignment](assignment.md)

## Project Objectives
1. Use a supervised machine learning model to predict the eligibility of applicants for a loan.
2. Implement machine learning methods like creating pipelines, model optimization, and model deployment

## Hypothesis
Eligibility May Be Impacted By:
1. Applicants who have or do not have dependents. Do they have no children? Do they have 1-2? They have 3? Do they have 4+? Applicants with dependents mean they require higher incomes to provide sustainable and comfortable lives for those whom rely on them and themselves. They can be seen as the "breadwinner" and main financial supporter.
2. The size of the loan the applicant is applying for. Are they asking for a few thousand, hundreds of thousands, or even millions? Depending on the size of the loan, the institution providing the money may be parting with a larger sum, which could reflect higher risk.
3. The reason for why the applicant is taking out a loan. Is it for a large purchase like a home, or new vehicle? Is it to start a business, or pay for post-secondary tuition? Is it to go on a lavish vacation, or pay off a higher interest loan? The reason for the loan, and the intent of how the money will be used, are all things that may impact the applicant's eligibility.

However, overall I believe that applicants who have credit history, have a higher income, higher education, and live in a developed area will be more likely to be granted a loan. 

This is because a credit history likely provides a proven track record of financial acumen, a higher income likely means a greater ability to repay the loan, a higher education likely means an access to better resources, and living in a developed area likely means having an established and safe community to reside in. All these things when combined together point to an applicant who likely has a more financially stable and privileged background.

## EDA 
1. Distribution of Applicant Incomes
* Applicant income data was heavily right skewed, with the vast majority (500+) of applicants making $18000 or less dollars.

2. Mean Income by Education
* Applicants who graduated from post-secondary education tend to make almost $2000 more on than applicants who do not.

3. Applicant Income by Property Area, Marital Status, and Self Employment
* Sorts applicant incomes by the property they reside in, and whether they are married (yes or no) and self employed (yes or no).

4. Income by Gender and Education
* Male applicants who graduated make more than males who have not graduated, and females in general. Whereas females in general make more than males who did not graduate.

5. Loan Amount by Marital Status and Number of Dependents
* Applicants who were married and had 3+ dependents applied for much higher loans than those who were married or unmarried with less than 3 children.

## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
1. Hypothesis Generation
2. Data Exploration (EDA, Statistics, Pivot Tables)
3. Data Cleaning (Imputing missing values, handling outliers/extreme values, renaming columns)
4. Data Preprocessing (Feature engineering, data transformation, merging DataFrames)
5. Model Building (Setting up train and test sets, dimensionality reduction, model predictions, model optimization and tuning)
6. Pipeline Implementation (Building a pipeline to consolidate many of the steps of the ML process, optimize pipeline)
7. Model Deployment (Model persistence, version control with git, and cloud deployment with flask)

## Results/Demo
After the entire modeling process mentioned above, I was able to achieve a prediction accuracy of 71.54% on both my train and test sets - not bad!

However, after consolidating my data cleaning, feature engineering, feature selection, and model building into a pipeline, I was able to achieve an 84.55% accuracy on my test set and an 80.65% accuracy on my train set. An over 10% improvement versus my initial model! However, there is a slightly lesser performance on my train set versus my test set, which could suggest some underlying fitting optimization issues.

## Challenges 
The largest challenge I had was trying to figure out which combination of hyperparameters with which models to use. There are so many interesting and different options that have either small or large impact on the models performance, and is so enticing to pick which combinations to use and when. This is especially so, as there are so many parameters and options just for a single model (ex. SVM's parameters include: kernels whether it be linear or rbf, gamma options, max iterations, and regularization, just to name a few). This becomes exponentially more when adding on another model like logistic regression to a grid search parameter. However, though this is a challenge for me, it proves to be a technique with a great deal of positive impact! As overall, this process saves significant amounts of time and computing power, versus if I were to code each pipeline, and grid parameter dictionary model by model.

## Future Goals
Given more time, I would like to have tried tuning different hyperparameters for each kind of model in my pipeline. Additionally, I would have liked to try using Grid Search optimize a pipeline with several models as parameters. This would have been very interesting to see which model and its hyperparameters, as well as the other steps of the pipeline (preprocessing, feature selection) and their hyperparameters would have been the best combination. Seeing the optimization of a model compute in seconds and provide an accuracy score is thrilling, especially when you can see tge significant increases in said scores. Overall, the practice of implementing pipelines and grid search has made the machine learning process so much more efficient and effective, and it has been an exciting experience. The streamlining and optimization provided by these modules and techniques has made a firm impression on me, and going forward I am excited to see how else I can implement and work with them!