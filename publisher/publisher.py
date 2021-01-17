from .publisher_interface import *

from rx.subject import Subject


class PassThroughPublisher(Subject, PublisherInterface):

    def __init__(self): 
        Subject.__init__(self)
        PublisherInterface.__init__(self)