import pandas as pd

from titanic.models.dataset import DataSet
from titanic.models.service import Service
from sklearn.ensemble import RandomForestClassifier

class Controller(object):

    dataset = DataSet()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        print(f'----------{type(this.label)}------')
        this.train = service.create_train(this)
        return this

    def learning(self, this):
        print(f'알고리즘 정확도 {self.service.accuracy_by_randomForestClassifier(this)}%')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId' : this.id, 'Survived' : prediction}).to_csv('./data/submission.csv', index=False)



    def preprocess(self, train, test)-> object:
        service = self.service
        this = self.dataset
        # 초기 모델(DF) 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']

        # nominal, ordinal 로 정형화
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        # 불필요한 feature (Name Cabin, Ticket) 제거
        this = service.drop_feature(this, 'Name', 'Sex', 'Cabin', 'Ticket', 'Age', 'Fare')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print('<Type Check>')
        print(f'1.Train 의 type 은 \n {type(this.train)} 이다.')
        print(f'2.Train 의 column 은 \n {this.train.columns} 이다.')
        print(f'3.Train 의 상위 5개 행 \n {this.train.head(5)} 이다.')
        print(f'4.Train 의 null의 갯수 \n {this.train.isnull().sum()}개')
        print(f'5.Train 의 type \n{type(this.test)} 이다.')
        print(f'6.Train 의 column \n {this.test.columns} 이다.')
        print(f'7.Train 의 상위 1개 행\n {this.test.head(1)} 이다.')
        print(f'8.Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*' * 100)