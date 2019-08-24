import filecmp

import pytest

import cmt
from cmt.a_map import MapType
from tests.const import map_file


@pytest.mark.parametrize("version", [0, 1])
def test_cmap(version, tmp_path):
    origin = map_file(MapType.CMAP, version)
    trg = tmp_path.joinpath("encoded.cmap")
    map_ = cmt.decode(origin, debug=False)
    cmt.encode(map_, trg)
    assert filecmp.cmp(origin, trg, shallow=False)


@pytest.mark.parametrize("version", [0, 1, 2])
def test_ecmap(version, tmp_path):
    origin = map_file(MapType.ECMAP, version)
    trg = tmp_path.joinpath("encoded.ecmap")
    map_ = cmt.decode(origin, debug=False)
    cmt.encode(map_, trg)
    assert filecmp.cmp(origin, trg, shallow=False)
