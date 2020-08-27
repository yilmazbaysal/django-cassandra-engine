from cassandra.cqlengine import columns
from cassandra.cqlengine.columns import *


class Text(columns.Text):

    choices = None

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices', None)

        super().__init__(*args, **kwargs)


class Ascii(columns.Ascii):

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices', None)

        super().__init__(*args, **kwargs)


class Integer(columns.Integer):

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices', None)

        super().__init__(*args, **kwargs)


class TinyInt(columns.TinyInt):

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices', None)

        super().__init__(*args, **kwargs)


class SmallInt(columns.SmallInt):

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices', None)

        super().__init__(*args, **kwargs)
