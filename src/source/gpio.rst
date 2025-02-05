General Purpose Input/Output (GPIO) Peripheral
==============================================

The way to connect your board to the external world and control other components is through the GPIO pins. Not all pins are available for use; in most cases, only pins 0, 2, 4, 5, 12, 13, 14, 15, and 16 can be used.

The pins are available in the `machine` module, so make sure you import that first. Then you can create a pin using:

.. code-block:: python

    pin = machine.Pin(0)

Here, the "0" is the pin that you want to access. Usually, you want to configure the pin to be input or output, and you do this when constructing it. To make an input pin, use:

.. code-block:: python

    pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

You can either use `PULL_UP` or `None` for the input pull-mode. If it’s not specified, then it defaults to `None`, which is no pull resistor. GPIO16 has no pull-up mode. You can read the value on the pin using:

.. code-block:: python

    pin.value()

The pin on your board may return 0 or 1 here, depending on what it’s connected to. To make an output pin, use:

.. code-block:: python

    pin = machine.Pin(0, machine.Pin.OUT)

Then set its value using:

.. code-block:: python

    pin.value(0)
    pin.value(1)

Or:

.. code-block:: python

    pin.off()
    pin.on()


Example blink 
------------

Here is an example of blinking an LED connected to pin 0:

.. code-block:: python

    import machine
    import time

    pin = machine.Pin(0, machine.Pin.OUT)

    while True:
        pin.on()
        time.sleep(1)
        pin.off()
        time.sleep(1)

Example button
-------------

Here is an example of reading a button connected to pin 0:

.. code-block:: python

    import machine

    pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if pin.value() == 0:
            print("Button pressed")
        else:
            print("Button released")