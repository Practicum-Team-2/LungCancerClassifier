


import pandas as pd
import numpy as np
from imblearn.pipeline import Pipeline as imbpipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from imblearn.over_sampling import SMOTE
import explainerdashboard


pd.options.display.max_seq_items = None

url="https://raw.githubusercontent.com/Practicum-Team-2/LungCancerClassifier/main/data/full_data.csv"
df = pd.read_csv(url, index_col=0)

#df = pd.read_csv('full_data.csv')
#df.drop(df.columns[0], axis=1, inplace=True)
df=df[df["Cancer Type Detailed"]!="Small Cell Lung Cancer"]
df["Cancer Type Detailed"].value_counts()

df['Cancer Type Detailed'] = np.where(df['Cancer Type Detailed'] == "Lung Squamous Cell Carcinoma", 1, 0)
df = df.loc[:, df.columns != 'Somatic Status']

# Split the dataset into train and test sets
X = df.loc[:, df.columns != 'Cancer Type Detailed']
y = df['Cancer Type Detailed']
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size = 0.2, random_state = 11)


"""start preprocessing the data, very inefficient approach just because I want to preserve the variable names."""

X_train_cat=X_train.iloc[:,[3,4]]#the categorical columns
impute=SimpleImputer(strategy='most_frequent', fill_value='missing')
X_train_cat=pd.DataFrame(impute.fit_transform(X_train_cat), columns = X_train_cat.columns)
X_train_cat=pd.get_dummies(X_train_cat)


X_train_num=X_train.iloc[:,[0,1,2,5,6]]#the numeric columns
impute=SimpleImputer(strategy='median')
#X_train_num=impute.fit_transform(X_train_num)

X_train_num=pd.DataFrame(impute.fit_transform(X_train_num),columns = X_train.iloc[:,[0,1,2,5,6]].columns)
#X_train_num=pd.DataFrame(StandardScaler().fit_transform(X_train_num), columns = X_train.iloc[:,[0,1,2,6,7]].columns)

X_train_good =pd.concat([X_train_cat,X_train_num],axis=1)


#address imbalanced data
oversample = SMOTE()
X_train_good, y_train = oversample.fit_resample(X_train_good, y_train)


X_test_cat=X_test.iloc[:,[3,4]]
impute=SimpleImputer(strategy='most_frequent', fill_value='missing')
X_test_cat=pd.DataFrame(impute.fit_transform(X_test_cat), columns = X_test_cat.columns)
X_test_cat=pd.get_dummies(X_test_cat)
X_test_num=X_test.iloc[:,[0,1,2,5,6]]
impute=SimpleImputer(strategy='median')
#X_test_num=impute.fit_transform(X_test_num)
X_test_num=pd.DataFrame(impute.fit_transform(X_test_num), columns = X_test.iloc[:,[0,1,2,5,6]].columns)

#X_test_num=pd.DataFrame(StandardScaler().fit_transform(X_test_num), columns = X_test.iloc[:,[0,1,2,6,7]].columns)
X_test_good =pd.concat([X_test_cat,X_test_num],axis=1)
X_test_good, y_test = oversample.fit_resample(X_test_good, y_test)




from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from sklearn.ensemble import RandomForestClassifier
feature_descriptions = {
    "Sex": "Gender of Patient",
    "Mutation Count": "Mutation Count",
    "Fraction Genome Altered": "Fraction Genome Altered",
    "Diagnosis Age": "Age at which a condition or disease was first diagnosed.", 
    "Person Cigarette Smoking History Pack Year Value": "Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20.",
    "TMB Nonsynonymous": "Tumor Mutational Burden Nonsynonymous",
    "Smoking History" : "Smoking History",
}
#X_train, y_train, X_test, y_test = titanic_survive()
#train_names, test_names = titanic_names()
model = RandomForestClassifier(n_estimators=100, max_depth=9,criterion="gini",max_features=2)#the best parameters
model.fit(X_train_good, y_train)
explainer = ClassifierExplainer(model, X_test_good, y_test, 
                                cats=[{"Smoking History":['Smoking History_Current Smoker',"Smoking History_Former Smoker","Smoking History_Non Smoker","Smoking History_Reformed Smoker"]},
                                    {'Sex': ['Sex_Female', 'Sex_Male']}],
                                descriptions=feature_descriptions,
                                labels=['Lung Adenocarcinoma', 'Lung Squamous Cell Carcinoma'],
                                index_name = "Sample", 
                                target = "Cancer Type Detailed"
                                )
db = ExplainerDashboard(explainer, 
                        title="Lung Cancer Classifier", 
                        shap_interaction=False,
                        decision_trees=False
                        )
db.run(port=8030)

