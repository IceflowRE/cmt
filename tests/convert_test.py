import pytest

import cmt
from tests.conftest import map_types, map_versions


@pytest.mark.parametrize("map_type", map_types)
@pytest.mark.parametrize("version", map_versions)
@pytest.mark.parametrize("trg_map_type", map_types)
@pytest.mark.parametrize("trg_version", map_versions)
def test_convert_without_exception(version, map_type, trg_map_type, trg_version, map_files):
    map_ = cmt.decode(map_files[version, map_type])
    cmt.convert(map_, trg_version, trg_map_type)
