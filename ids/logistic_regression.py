from ids.abstract_model import AbstractModel
from sklearn import linear_model

class LogisticRegression(AbstractModel):

    def __init__(self, max_iter=1000):
        self.classifier = linear_model.LogisticRegression(
        multi_class='multinomial',
        solver='lbfgs',
        max_iter=max_iter
    )