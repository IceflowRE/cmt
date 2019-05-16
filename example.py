from pathlib import Path

import cmt

if __name__ == '__main__':
    cmap = cmt.decode(Path("./new.cmap"), True)
    print(cmap)
    print(cmap.entities[0])
    cmt.encode(cmap, Path("./new_encode.cmap"))
