from titanic.models.dataset import DataSet
from titanic.models.service import Service

class Test(object):

    dataset: object = DataSet()
    service: object = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)

    def plot(self):
        this = self.entity
        print(f'The data type of Train is {type(this.train)}.')
        print(f'Columns of Train is {this.train.columns}.')
        print(f'The top 5 superior data are {this.train.head}.')
        print(f'The top 5 inferior data are {this.train.tail}.')