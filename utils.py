import pandas as pd
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt

def evaluate(y_true, y_pred):
   acc = metrics.accuracy_score(y_true, y_pred)
   pre = metrics.precision_score(y_true, y_pred, average='weighted')
   re = metrics.recall_score(y_true, y_pred, average='weighted')
   f1 = metrics.f1_score(y_true, y_pred, average='weighted')


   return {
       'Accuracy': acc,
       'Precision': pre,
       'Recall': re,
       "F1-score": f1,
   }


def plot_confusion_matrix(y_true, y_pred, label):
   print()
   print("Classification report")
   print(metrics.classification_report(y_true, y_pred, labels=label))
   print()
   conf = metrics.confusion_matrix(y_true=y_true, y_pred=y_pred, normalize='pred', labels=label)
   plt.figure(figsize=(20,20))
   sns.set(font_scale=1.4)
   sns.heatmap(conf,annot=True,annot_kws={"size": 16}, fmt='.3f', xticklabels=label,yticklabels=label)
   plt.xlabel('Predicted')
   plt.ylabel('True')
   plt.show()


def train_test(model, X_train, X_test, y_train, y_test):
   model.fit(X_train, y_train)
   pred = model.predict(X_test)
   result = evaluate(y_test, pred)
   result = pd.DataFrame([result], index=['value'])
   print(result)
   plot_confusion_matrix(y_test, pred, label=model.classes_)