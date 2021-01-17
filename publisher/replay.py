from .publisher_interface import *

from rx.subject.replaysubject import ReplaySubject


class ReplayPublisher(ReplaySubject, PublisherInterface): 

    def __init__(self, buffer_size: int = None, window=None, scheduler=None): 
        ReplaySubject.__init__(self, buffer_size=buffer_size, window=window, scheduler=scheduler)
        PublisherInterface.__init__(self)


class FilteredReplayPublisher(ReplayPublisher): 

    def __init__(self, buffer_size: int = None, window=None, scheduler=None): 
        ReplayPublisher.__init__(self, buffer_size=buffer_size, window=window, scheduler=scheduler)

    def on_next(self, value) -> None:
        if value is None:
            return

        super().on_next(value)


class CachedReplayPublisher(ReplaySubject, CachedPublisherInterface): 

    def __init__(self, value=None, buffer_size: int = None, window=None, scheduler=None): 
        ReplaySubject.__init__(self, buffer_size=buffer_size, window=window, scheduler=scheduler)
        CachedPublisherInterface.__init__(self, value)

    def on_next(self, value) -> None:
        self._value = value
        super().on_next(value)


class FilteredCachedReplayPublisher(CachedReplayPublisher): 

    def __init__(self, value=None, buffer_size: int = None, window=None, scheduler=None): 
        CachedReplayPublisher.__init__(self, value=value, buffer_size=buffer_size, window=window, scheduler=scheduler)

    def on_next(self, value) -> None:
        if value is None:
            return

        super().on_next(value)