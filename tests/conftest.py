from pathlib import Path

import pytest

from cmt.a_map import MapType

map_versions = [0, 1]
map_types = [MapType.CMAP, MapType.ECMAP]


@pytest.fixture
def map_files():
    return {
        (0, MapType.CMAP): Path("./tests/data/v0.cmap"),
        (1, MapType.CMAP): Path("./tests/data/v1.cmap"),
        (0, MapType.ECMAP): Path("./tests/data/v0.ecmap"),
        (1, MapType.ECMAP): Path("./tests/data/v1.ecmap"),
    }
