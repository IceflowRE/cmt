import filecmp

import pytest

import cmt
from tests.conftest import map_types, map_versions


@pytest.mark.parametrize("map_type", map_types)
@pytest.mark.parametrize("version", map_versions)
def test_decode_encode(version, map_type, map_files, tmp_path):
    trg = tmp_path.joinpath("encoded" + map_type.name)
    origin = map_files[version, map_type]
    cmap = cmt.decode(origin, debug=False)
    cmt.encode(cmap, trg)
    assert filecmp.cmp(origin, trg, shallow=False)
