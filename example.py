from pathlib import Path

from cmt.decode import decode
from cmt.encode import encode

if __name__ == '__main__':
    cmap = decode(Path("./trainingcourse_alpha.cmap"), True)
    print(cmap)
    print(cmap.entities[0])
    encode(Path("./trainingcourse_alpha_encode.cmap"), cmap)
