import struct
from enum import Enum

from cmt import utils
from cmt.cmap.a_entity import AEntity


class BlockType(Enum):
    Nothing = 0  # white
    Finish = 1  # red
    Jump = 2  # green
    Speed = 3  # yellow
    Ice = 4  # blue
    Checkpoint = 5  # purple


class Block(AEntity):
    def __init__(self):
        super().__init__(0, struct.calcsize('<BiiIIIIf'))
        self.block_type = None
        self.position = (0.0, 0.0, 0)
        self.scale = (0, 0, 0)
        self.rotation_z = 0.0
        self.checkpoint_nr = None

    def __str__(self):
        return f"type: 0 [Block]\n" \
            f"block type: {self.block_type.value} [{self.block_type.name}]\n" \
            f"position: {self.position}\n" \
            f"scale: {self.scale}\n" \
            f"rotation z: {self.rotation_z}" \
            f"\ncheckpoint nr: {self.checkpoint_nr}" if self.block_type == 5 else ""

    @classmethod
    def decode(cls, data: bytes, offset: int, debug: bool = False) -> 'Block':
        ent = Block()

        ent.block_type = BlockType(utils.unpack_from('<B', data, offset, ("block type",), debug)[0])
        offset += 1
        ent.position = utils.unpack_from('<iiI', data, offset, ("position x", "position y", "position z"), debug)
        offset += 3 * 4
        ent.scale = utils.unpack_from('<III', data, offset, ("scale x", "scale y", "scale z"), debug)
        offset += 3 * 4
        ent.rotation_z = utils.unpack_from('<f', data, offset, ("rotation z",), debug)[0]
        offset += 4
        ent.checkpoint_nr = None
        if ent.block_type == BlockType.Checkpoint:
            ent.checkpoint_nr = utils.unpack_from('<B', data, offset, ("checkpoint nr",), debug)[0]
            ent.byte_size += 1
        return ent

    def encode(self) -> bytearray:
        data = bytearray()
        # entity type
        data.extend(struct.pack('<B', self.type))
        # block type
        data.extend(struct.pack('<B', self.block_type.value))
        # position
        data.extend(struct.pack('<iiI', *self.position))
        # scale
        data.extend(struct.pack('<III', *self.scale))
        # rotation z
        data.extend(struct.pack('<f', self.rotation_z))
        if self.block_type == BlockType.Checkpoint:
            data.extend(struct.pack('<B', self.checkpoint_nr))
        return data


class Sphere(AEntity):
    def __init__(self):
        super().__init__(1, struct.calcsize('<iiI'))
        self.position = (0.0, 0.0, 0)

    def __str__(self):
        return f"type: 1 [Sphere]\n" \
            f"position: {self.position}"

    @classmethod
    def decode(cls, data: bytes, offset: int, debug: bool = False):
        ent = Sphere()

        ent.position = utils.unpack_from('<iiI', data, offset, ("position x", "position y", "position z"), debug)
        return ent

    def encode(self) -> bytearray:
        data = bytearray()
        # entity type
        data.extend(struct.pack('<B', self.type))
        # position
        data.extend(struct.pack('<iiI', *self.position))
        return data


class PlayerStart(AEntity):
    def __init__(self):
        super().__init__(2, struct.calcsize('<BiiIf'))
        self.position = (0.0, 0.0, 0)
        self.rotation_z = 0.0

    def __str__(self):
        return f"type: 2 [PlayerStart]\n" \
            f"position: {self.position}\n" \
            f"rotation z: {self.rotation_z}"

    @classmethod
    def decode(cls, data: bytes, offset: int, debug: bool = False) -> 'PlayerStart':
        ent = PlayerStart()

        utils.unpack_from('<B', data, offset, ("unused",), debug)
        offset += 1
        ent.position = utils.unpack_from('<iiI', data, offset, ("position x", "position y", "position z"), debug)
        offset += 3 * 4
        ent.rotation_z = utils.unpack_from('<f', data, offset, ("rotation z",), debug)[0]
        offset += 4
        return ent

    def encode(self) -> bytearray:
        data = bytearray()
        # entity type
        data.extend(struct.pack('<B', self.type))
        # unused, type identifier
        data.extend(b'\x00')
        # position
        data.extend(struct.pack('<iiI', *self.position))
        # rotation z
        data.extend(struct.pack('<f', self.rotation_z))
        return data


class Dummy(AEntity):
    def __init__(self):
        super().__init__(128, struct.calcsize('<BiiIIIIf'))
        self.id = None
        self.position = (0.0, 0.0, 0)
        self.scale = (0, 0, 0)
        self.rotation_z = 0.0

    def __str__(self):
        return f"type: 128 [Dummy]\n" \
            f"id: {self.id}\n" \
            f"position: {self.position}\n" \
            f"scale: {self.scale}\n" \
            f"rotation z: {self.rotation_z}"

    @classmethod
    def decode(cls, data: bytes, offset: int, debug: bool = False) -> 'Dummy':
        ent = Dummy()

        ent.id = utils.unpack_from('<B', data, offset, ("id",), debug)[0]
        offset += 1
        ent.position = utils.unpack_from('<iiI', data, offset, ("position x", "position y", "position z"), debug)
        offset += 3 * 4
        ent.scale = utils.unpack_from('<III', data, offset, ("scale x", "scale y", "scale z"), debug)
        offset += 3 * 4
        ent.rotation_z = utils.unpack_from('<f', data, offset, ("rotation z",), debug)[0]
        return ent

    def encode(self) -> bytearray:
        data = bytearray()
        # entity type
        data.extend(struct.pack('<B', self.type))
        # id
        data.extend(struct.pack('<B', self.id))
        # position
        data.extend(struct.pack('<iiI', *self.position))
        # scale
        data.extend(struct.pack('<III', *self.scale))
        # rotation z
        data.extend(struct.pack('<f', self.rotation_z))
        return data