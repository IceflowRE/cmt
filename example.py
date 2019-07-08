from pathlib import Path

import cmt

if __name__ == '__main__':
    cmap = cmt.decode(Path("./tests/data/v1.cmap"), True)
    print(cmap)
    print(cmap.entities[0])

    #cmt.encode(cmap, Path("./new_encode.cmap"))
