from .publisher_interface import *

from rx.subject import Subject
from rx.subject.behaviorsubject import BehaviorSubject


class ValuePublisher(Subject, CachedPublisherInterface): 

    def __init__(self, value=None): 
        Subject.__init__(self)
        CachedPublisherInterface.__init__(self, value)

    def on_next(self, value) -> None:
        self._value = value
        super().on_next(value)


class FilteredValuePublisher(ValuePublisher): 

    def __init__(self, value=None): 
        ValuePublisher.__init__(self, value)

    def on_next(self, value) -> None:
        if value is None:
            return

        super().on_next(value)


class BehaviorPublisher(BehaviorSubject, PublisherInterface):

    def __init__(self, value=None): 
        BehaviorSubject.__init__(self, value)
        PublisherInterface.__init__(self)

    def __call__(self, *args):
        if len(args) == 0:
            return self.value
        else:
            self.publish(args)


class FilteredBehaviorPublisher(BehaviorPublisher): 

    def __init__(self, value=None): 
        BehaviorPublisher.__init__(self, value)

    def on_next(self, value) -> None:
        if value is None:
            return

        super().on_next(value)