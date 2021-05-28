from dataclasses import dataclass


@dataclass
class DataSet(object):
    context: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    #장고에서 프로퍼티를 등록하는 방법
    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) ->str: return self._label

    @label.setter
    def label(self, label): self._label = label
