from rx import operators as ops
from rx import Observable, of

from publisher import PassThroughPublisher
from publisher.cache import FilteredValuePublisher as FVPublisher
from publisher.replay import FilteredCachedReplayPublisher as FCRPublisher

class Node:

    def __init__(self, name: str = "Generic Node", description: str = ""):
        self.name = name
        self.description = description

        self.setup()

    def setup(self):
        raise NotImplementedError


class AddNode(Node):

    def __init__(self, value1: Observable, value2: Observable, name: str = "Add Node", description: str = ""):
        self.value1 = value1
        self.value2 = value2

        self.output = FVPublisher()

        super().__init__(name, description)

    def setup(self):
        self.value1.pipe(
            ops.zip(self.value2),
            ops.map(lambda vals: vals[0] + vals[1])
        ).subscribe(self.output)


value1 = of(1, 2, 3, 4, 5, 6, 6)
value2 = PassThroughPublisher()

add = AddNode(value1, value2)
add.output.subscribe(lambda val: print(val))

value2.publish(1, 2, 3)
value2()
print("Output: " + str(add.output()))
value2.publish(4, 5, 6)

print("Output: " + str(add.output()))
