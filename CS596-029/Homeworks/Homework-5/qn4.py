import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


X_train = 
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
X_train = vectorizer.fit_transform(data_train.data)
