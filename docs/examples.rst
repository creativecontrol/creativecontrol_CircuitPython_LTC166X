Simple test
------------

Ensure your device works with this simple test. Write individual values to all DAC channels from a list.

.. literalinclude:: ../examples/ltc166x_dac_value_list.py
    :caption: examples/ltc166x_dac_value_list.py
    :linenos:

Single value
-------------

Write a value to a single DAC channel.

.. literalinclude:: ../examples/ltc166x_single_value.py
    :caption: examples/ltc166x_single_value.py
    :linenos:

Single value sweep
-------------------

Write a value to a single DAC channel ramping from min to max and back.

.. literalinclude:: ../examples/ltc166x_single_value_sweep.py
    :caption: examples/ltc166x_single_value_sweep.py
    :linenos:

DAC list selective
-------------------

Write random values to all DAC channels from a list. Only update value if it has changed.

.. literalinclude:: ../examples/ltc166x_dac_list_selective.py
    :caption: examples/ltc166x_dac_list_selective.py
    :linenos:

DAC Chain
----------

Example of using a DAC daisy-chain as described in the LTC166X datasheet
https://www.analog.com/media/en/technical-documentation/data-sheets/166560fa.pdf

.. literalinclude:: ../examples/ltc166x_dac_chain.py
    :caption: examples/ltc166x_dac_chain.py
    :linenos:
