# AI_Intrusion_Detection
This project propose a solution to the Intrusion Detection problem using Decision Trees.


## Prerequisites
- [Python 3.7](https://www.python.org/downloads/) installed (tested on v3.7).
- [pandas](https://pandas.pydata.org) library installed for reading the datas.
- [sklearn](http://scikit-learn.org/stable/install.html) library installed for DecisionTreeClassifier.

## How to use
Run `dt_predict.py` to start training and testing accuracies for datasets provided and to print the confusion matrix. 

## Code
`preprocessing.py` is used for mapping attacks to major five categories and one-hot encoding to remove the noise from datas.
Most of this code is from [here](https://github.com/404notf0und/Tree-ensemble-Intrusion-Detection-with-KDD99).

`data_names.py` is used for listing attribute names (taken from [here](https://github.com/404notf0und/Tree-ensemble-Intrusion-Detection-with-KDD99)) and features names (taken from [here](https://github.com/PENGZhaoqing/kdd99-scikit)).

## References
- [Artificial Intelligence - A Modern Approach](http://aima.cs.berkeley.edu) - Peter Norvig, Stuart J. Russell, 3rd edition. Pearson, 2010.
- [Scikit Learn](http://scikit-learn.org/stable/)
- [(Amor et al.)](https://www.semanticscholar.org/paper/Naive-Bayes-vs-decision-trees-in-intrusion-systems-Amor-Benferhat/16a778c5d83cce2f4c4af46efafb927e7d0d8e60)
- [KDD Cup 1999](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
- [Tree-ensemble-Intrusion-Detection-with-KDD99](https://github.com/404notf0und/Tree-ensemble-Intrusion-Detection-with-KDD99)
- [kdd99-scikit](https://github.com/PENGZhaoqing/kdd99-scikit)
- [Data Mining Techniques for Intrusion Detection](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.122.5800&rep=rep1&type=pdf)
- [Denial-of-Service, Probing & Remote to User (R2L) Attack Detection using Genetic Algorithm](https://pdfs.semanticscholar.org/060d/0c18c3f490720b62e40e7003aa7f75d50941.pdf) - Swati Paliwal, Ravindra Gupta.
- [Results of the KDD'99 Classifier Learning Contest](http://cseweb.ucsd.edu/~elkan/clresults.html)
- [Stack Overflow](https://stackoverflow.com/)
