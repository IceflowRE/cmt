*************************
CMT - Celaria Map Toolkit
*************************
|status| |programming language| |license|

|github actions| |readthedocs| |codecov|

|pypi|

----

Celaria Map Toolkit can convert different map format from one into another.

Install via pip:

    pip install cmt

About the usage see:

    cmt --help

----

About
=====

.cmap support
-------------

+---------+--------+--------+---------+-----------+---------+
| Version | Encode | Decode | Convert | Downgrade | Upgrade |
+---------+--------+--------+---------+-----------+---------+
| 0       | ✔      | ✔      | v0      |           | ✔       |
+---------+--------+--------+---------+-----------+---------+
| 1       | ✔      | ✔      | v1      | ✔         | ✔       |
+---------+--------+--------+---------+-----------+---------+
| 2       | ✔      | ✔      | v4      | ✔         |         |
+---------+--------+--------+---------+-----------+---------+

.ecmap support
--------------

+---------+--------+--------+---------+-----------+---------+
| Version | Encode | Decode | Convert | Downgrade | Upgrade |
+---------+--------+--------+---------+-----------+---------+
| 0       | ✔      | ✔      | v0      |           | ✔       |
+---------+--------+--------+---------+-----------+---------+
| 1       | ✔      | ✔      | v1      | ✔         | ✔       |
+---------+--------+--------+---------+-----------+---------+
| 2       | ✔      | ✔      | v1      | ✔         | ✔       |
+---------+--------+--------+---------+-----------+---------+
| 4       | ✔      | ✔      | v2      | ✔         |         |
+---------+--------+--------+---------+-----------+---------+

----

Web
===

https://github.com/IceflowRE/cmt

Credits
=======

- Developer
    - `Iceflower S <https://github.com/IceflowRE>`__
        - iceflower@gmx.de
- Format Definition
    - http://www.celaria.com/

Disclaimer
----------

This software is not official supported by http://www.celaria.com/.

License
-------

Copyright 2019-present Iceflower S (iceflower@gmx.de)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. Badges.

.. |status| image:: https://img.shields.io/badge/status-archived-red.svg

.. |programming language| image:: https://img.shields.io/badge/language-Python_3.7-orange.svg
   :target: https://www.python.org/

.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT

.. |github actions| image:: https://img.shields.io/github/actions/workflow/status/IceflowRE/cmt/build.yml
   :target: https://github.com/IceflowRE/cmt/actions

.. |readthedocs| image:: https://readthedocs.org/projects/cmt/badge/?version=latest
   :target: https://cmt.readthedocs.io/en/latest/index.html

.. |pypi| image:: https://img.shields.io/pypi/v/cmt.svg
   :target: https://pypi.org/project/CMT/

.. |codecov| image:: https://img.shields.io/codecov/c/github/IceflowRE/cmt/main.svg?label=coverage
   :target: https://codecov.io/gh/IceflowRE/cmt
