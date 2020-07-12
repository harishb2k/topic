import tensorflow as tf
import pandas as pd
import numpy as np

tf.get_logger().setLevel('ERROR')

# Read data from CSV file
dftrain = pd.read_csv('./data/train.csv')
dfeval = pd.read_csv('./data/eval.csv')

# These are the output Or "Y"
y_train = dftrain.pop('survived').astype(float)
y_eval = dfeval.pop('survived').astype(float)

# LinearClassifier need get the type of columns e.g. "sex" is "male/female" i.e. it is a categorical column
# On the other hand age and fare is numeric
CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

# Make type using tf.feature_column
feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))
for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float64))


# Function to return a input function for train method
def train_input_fn():
    ds = tf.data.Dataset.from_tensor_slices((dict(dftrain), y_train))
    ds = ds.batch(32).repeat(10)
    return ds


# Function to return a eval function for train method
def eval_input_fn():
    ds = tf.data.Dataset.from_tensor_slices((dict(dfeval), y_eval))
    ds = ds.batch(32).repeat(1)
    return ds


# Let's build and train our model
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
linear_est.train(train_input_fn)

# Let's check its result - I don't think it is needed (it is just to evaluate how your model did)
result = linear_est.evaluate(eval_input_fn)

# ------------------------------ So, here we do the predictions over trained model -------------------------------------

# Here we are passing 2 samples to evaluate
expected = [0, 1]
predict_x = {
    'survived': np.array([0, 1]),
    'sex': np.array(['male', "female"]),
    'age': np.array([22, 58.0]),
    'n_siblings_spouses': np.array([1, 0]),
    'parch': np.array([0, 0]),
    'fare': np.array([7.25, 26.55]),
    'class': np.array(['Third', 'First']),
    'deck': np.array(['unknown', 'C']),
    'embark_town': np.array(['Southampton', 'Southampton']),
    'alone': np.array(['n', 'y']),
}


# This is a input method for predict function
def input_fn(features, batch_size=256):
    return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size)


# This the the real prediction which will give you the result
predictions = linear_est.predict(input_fn=lambda: input_fn(predict_x))
for pred_dict, expec in zip(predictions, expected):
    class_id = pred_dict['class_ids'][0]
    probability = pred_dict['probabilities'][class_id]
    print(pred_dict['class_ids'])
    print(pred_dict['probabilities'])

# Result
# [0]                       -> This means that we got class id "0"
# [0.9072583  0.09274171]   -> Prediction over [0, 1] class, it says that 0.90% 0 and 0.09%1
# [1]
# [0.38411838 0.6158816 ]
