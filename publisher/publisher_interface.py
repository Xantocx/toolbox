class PublisherInterface:

    def __init__(self):
        pass

    def publish(self, *values) -> None:
        for value in values:
            self.on_next(value)

    def __call__(self, *args):
        if len(args) == 0:
            return

        self.publish(args)


class CachedPublisherInterface(PublisherInterface):

    def __init__(self, value=None):
        PublisherInterface.__init__(self)

        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newValue) -> None:
        self.on_next(newValue)

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