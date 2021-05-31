from titanic.models.dataset import DataSet
import pandas as pd

class Service(object):

    dataset = DataSet()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this)-> object:
        return this.train.drop('Survived', axix = 1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this