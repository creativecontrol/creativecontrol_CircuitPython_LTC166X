Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/creativecontrol/CircuitPython_creativecontrol_CircuitPython_LTC166X/workflows/Build%20CI/badge.svg
    :target: https://github.com/creativecontrol/CircuitPython_creativecontrol_CircuitPython_LTC166X/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython library for control of LTC1665 8-bit and LTC1660 10-bit DACs from Linear Technologies.

`LTC166X datasheet <https://www.analog.com/media/en/technical-documentation/data-sheets/166560fa.pdf>`_

Multiple LTC1665/LTC1660’s can be controlled from a single 3-wire serial port (i.e., SCK, DIN and CS/LD) by
using the included “daisy-chain” facility. A series of *n* chips is configured by connecting each DOUT (except the
last) to DIN of the next chip, forming a single 16n-bit shift register. The SCK and CS/LD signals are common
to all chips in the chain. In use, CS/LD is held low while *n* 16-bit words are clocked to DIN of the first chip; CS/LD
is then pulled high, updating all of them simultaneously.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/creativecontrol-circuitpython-ltc166x/>`_.
To install for current user:

.. code-block:: shell

    pip3 install creativecontrol-circuitpython-ltc166x

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install creativecontrol-circuitpython-ltc166x

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install creativecontrol-circuitpython-ltc166x

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install creativecontrol_circuitpython_ltc166x

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: shell

   import time
   import board
   import creativecontrol_circuitpython_ltc166x

   ltc1665 = creativecontrol_circuitpython_ltc166x.LTC1665(cs=board.GP1, sck=board.GP2, mosi=board.GP3, debug=True)

   dac_values = [1, 3, 7, 15, 31, 63, 127, 255]

   while True:
        print('writing dac values ', time.monotonic())
        ltc1665.write_dac_values(dac_values)
        time.sleep(4)
        print('off')
        ltc1665.write_dac_values([0]*8)
        time.sleep(4)

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/creativecontrol/CircuitPython_creativecontrol_CircuitPython_LTC166X/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
