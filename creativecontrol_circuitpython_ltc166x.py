# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: MIT
"""
`creativecontrol_circuitpython_ltc166x`
================================================================================

CircuitPython library for control of LTC166X 8-bit and 10-bit DACs.


* Author(s): Thadeus Frazier-Reed

Implementation Notes
--------------------

*
http://www.kerrywong.com/2010/05/02/a-library-for-ltc1665ltc1660/

**Hardware:**

* Linear Technologies LTC166X datasheet:
  https://www.analog.com/media/en/technical-documentation/data-sheets/166560fa.pdf

Multiple LTC1665/LTC1660’s can be controlled from a
single 3-wire serial port (i.e., SCK, DIN and CS/LD) by
using the included “daisy-chain” facility. A series of m
chips is configured by connecting each DOUT (except the
last) to DIN of the next chip, forming a single 16m-bit
shift register. The SCK and CS/LD signals are common
to all chips in the chain. In use, CS/LD is held low while m
16-bit words are clocked to DIN of the first chip; CS/LD
is then pulled high, updating all of them simultaneously.
.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

import microcontroller
from busio import SPI
import digitalio
from adafruit_bus_device.spi_device import SPIDevice

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/creativecontrol/creativecontrol_CircuitPython_LTC166X.git"

class LTC166X():
    """
    LTC166X 8 or 10-bit digital to analog converter.  This class has a similar
    interface as the CircuitPython AnalogOut class and can be used in place
    of that module.
    :param ~busio.SPI spi: The SPI bus.
    :param int address: The address of the device if set differently from the default.
    """

    def __init__(
            self,
            sck: microcontroller.Pin,
            mosi: microcontroller.Pin,
            cs: microcontroller.Pin,
            bits: int = None,
            debug: bool = False) -> None:
        """
        """
        self._num_channels = 8
        self._data_bits = 12
        self._cs = digitalio.DigitalInOut(cs)
        self._spi = SPI(clock=sck, MOSI=mosi)
        self._bit_depth = bits or self.get_bit_depth()
        self._range = pow(2, self._bit_depth)
        self._device = SPIDevice(self._spi, self._cs, baudrate=5000000, polarity=0, phase=0)
        self._debug = debug

    def get_bit_depth(self):
        """
        Placeholder. If not using a subclass to define bit depth, must define on initialization.
        """
        return None

    def get_device_range(self):
        """
        Return device range based on device used.
        """
        return self._range

    def write_dac_values(self, values):
        """
        Write to DAC using adafruit_bus_device.

        :param values: list of values from 0 to device range.
        """
        with self._device as spi:
            for idx, value in enumerate(values):
                assert 0 <= value <= self._range
                out = 0x0000
                # Set the top 4 bits to the address based on array position.
                out |= (idx%self._num_channels)+1 << self._data_bits
                # Set the next n bits based on bit depth.
                out |= value << (self._data_bits - self._bit_depth)
                out_bytes = out.to_bytes(2, 'big')
                if self._debug:
                    print(f'{idx} {hex(out)} {out_bytes} {len(out_bytes)}')
                spi.write(out_bytes)


class LTC1660(LTC166X):
    """
    Extended class for 10bit Octal DAC
    """
    def get_bit_depth(self):
        return 10


class LTC1665(LTC166X):
    """
    Extended class for 8bit Octal DAC
    """
    def get_bit_depth(self):
        return 8
