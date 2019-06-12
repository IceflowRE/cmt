import struct

from cmt import utils
from cmt.cmap.v1 import *
from cmt.ecmap.a_ecmap import AECMap


class ECMap(AECMap):
    """
    Celaria .ecmap format (version 1)

    Datatypes:
    ===============================
    uByte > unsigned byte (1 byte)
    uShort > unsigned short (2 bytes)
    uInt > unsigned int (4 bytes)
    sShort > signed short (2 bytes)
    sInt > signed int (4 bytes)
    f32 > float (4 bytes)
    f64 > double (8 bytes)

    > <datatype> (<number of datatypes in sequence>) // <description>
    or
    > [<variable name>] : <datatype> (<number of datatypes in sequence>) // <description>

    Difference regarding to the .cmap begins with a '!!'.

    ===============================

    > uByte (11) // string identifier
    > uByte (1) // version

    > nameLen : uByte (1) // number of characters in map name
    > uByte (nameLen) // map name as String

    !! // checkpoint times are missing

    > f32 (1) // sun rotation on Z axis
    > f32 (1) // sun angle to xy plane (between 0 and 90 degrees)

    ... same as cmap v1 ...
    """

    def __init__(self):
        super().__init__(1)
        self.cmap = CMap_1()

    def __str__(self):
        return f"identifier: {self.identifier.name}\n" \
                   f"format version: {self.format_version}\n" \
                   f"::cmap::\n" + \
               str(self.cmap)

    @classmethod
    def decode(cls, data: bytes, offset: int, debug: bool = False) -> 'ECMAP':
        cmap = CMap_1()

        name_len = utils.unpack_from('<B', data, offset, ("name length",), debug)[0]
        offset += 1

        cmap.name = data[offset:offset + name_len].decode("utf-8")
        if debug:
            utils.debug_print(data[offset:offset + name_len], "name", cmap.name, offset)
        offset += name_len

        cmap.preview_cam_set = utils.unpack_from('<?', data, offset, ("preview cam set",), debug)[0]
        offset += 1

        cmap.sun_rotation = utils.unpack_from('<f', data, offset, ("sun rotation",), debug)[0]
        offset += 4

        cmap.sun_angle = utils.unpack_from('<f', data, offset, ("sun angle",), debug)[0]
        offset += 4

        cmap.camera_pos = utils.unpack_from('<ddd', data, offset, ("camera pos x", "camera pos y", "camera pos z"),
                                            debug)
        offset += 3 * 8

        cmap.camera_look = utils.unpack_from('<ddd', data, offset, ("camera look x", "camera look y", "camera look z"),
                                             debug)
        offset += 3 * 8

        # entities processing
        ent_count = utils.unpack_from('<I', data, offset, ("entity count",), debug)[0]
        offset += 4

        ent_done = 0
        while ent_done < ent_count:
            ent_type = utils.unpack_from('<B', data, offset, ("entity type",), debug)[0]
            offset += 1
            if ent_type == 0:
                cur_ent = Block_1.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 1:
                cur_ent = Sphere_1.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 2:
                cur_ent = PlayerStart_1.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 128:
                cur_ent = Dummy_1.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            else:
                raise ValueError(f"Unknown entity type: {ent_type} at {offset - 1}")
            ent_done += 1
        if debug:
            print(offset, " / ", len(data), " consumed")

        ecmap = ECMap()
        ecmap.cmap = cmap
        return ecmap

    def encode(self) -> bytearray:
        data = bytearray()
        # file identifier
        data.extend(self.identifier.value.encode("utf-8"))
        # format version
        data.extend(struct.pack('<B', self.format_version))
        # length of name
        data.extend(struct.pack('<B', len(self.cmap.name)))
        # name
        data.extend(self.cmap.name.encode("utf-8"))
        # preview cam set
        data.extend(struct.pack('<?', self.cmap.preview_cam_set))
        # sun rotation
        data.extend(struct.pack('<f', self.cmap.sun_rotation))
        # sun angle
        data.extend(struct.pack('<f', self.cmap.sun_angle))
        # camera position
        data.extend(struct.pack('<ddd', *self.cmap.camera_pos))
        # camera look
        data.extend(struct.pack('<ddd', *self.cmap.camera_look))
        # entity count
        data.extend(struct.pack('<I', len(self.cmap.entities)))
        # entities
        for ent in self.cmap.entities:
            data.extend(ent.encode())
        return data