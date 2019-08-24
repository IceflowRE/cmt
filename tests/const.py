from pathlib import Path

from cmt.a_map import MapType

test_data = Path("./tests/data/")


def map_file(type_: MapType, version: int) -> Path:
    return test_data.joinpath(f"v{version}.{type_.name}")
