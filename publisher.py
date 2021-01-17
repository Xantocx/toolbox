from rx.subject import Subject
from rx.subject.replaysubject import ReplaySubject
from rx.subject.behaviorsubject import BehaviorSubject


class Publisher(Subject):

    def __init__(self): 
        super().__init__()

    def publish(self, *values) -> None:
        for value in values:
            self.on_next(value)

    def __call__(self, *args):
        self.publish(args)

            
class ReplayPublisher(ReplaySubject): 

    def __init__(self, buffer_size: int = None, window=None, scheduler=None): 
        super().__init__(buffer_size=buffer_size, window=window, scheduler=scheduler)

    def publish(self, *values) -> None:
        for value in values:
            self.on_next(value)

    def __call__(self, *args):
        self.publish(args)


class BehaviorPublisher(BehaviorSubject):

    def __init__(self, value=None): 
        super().__init__(value)

    def publish(self, *values) -> None:
        for value in values:
            self.on_next(value)

    def __call__(self, *args):
        if len(args) == 0:
            return self.value
        else:
            self.publish(args)


class FilteredBehaviorPublisher(BehaviorPublisher): 

    def __init__(self, value=None): 
        super().__init__(value)

    def on_next(self, value) -> None:
        if value is None:
            return

        super().on_next(value)


class CachedPublisher(Subject): 

    def __init__(self, value=None): 
        super().__init__()

        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newValue) -> None:
        self.on_next(newValue)

    def on_next(self, value) -> None:
        self._value = value
        super().on_next(value)

    def republish(self) -> None:
        self.on_next(self.value)

    def publish(self, *values) -> None:
        for value in values:
            self.value = value

    def __call__(self, *args):
        if len(args) == 0:
            return self.value
        else:
            self.publish(args)


class FilteredCachedPublisher(CachedPublisher): 

    def __init__(self, value=None): 
        super().__init__(value)

    def on_next(self, value) -> None:
        if value is None:
            return

        super().on_next(value)