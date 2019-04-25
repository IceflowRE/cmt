from abc import ABC


class Entity(ABC):
    """
    :ivar type: entity type
    :ivar byte_size: size in bytes the entity uses
    """

    def __init__(self, type_: int, byte_size: int):
        self.type = type_
        self.byte_size = byte_size

    def encode(self) -> bytearray:
        """
        Includes the entity type.
        :return:
        """
        raise NotImplementedError
