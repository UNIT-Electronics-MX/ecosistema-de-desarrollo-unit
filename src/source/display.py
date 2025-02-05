import machine
from ocks import SSD1306_I2C

def setup_i2c(sda_pin, scl_pin):
    """
    Set up the I2C communication.

    Parameters:
        sda_pin (int): GPIO pin number for I2C SDA.
        scl_pin (int): GPIO pin number for I2C SCL.

    Returns:
        I2C object: Configured I2C instance.

    Raises:
        ValueError: If the pin numbers are out of allowable range.

    Note:
        Ensure that the pin numbers provided are valid digital pins that support I2C functions.
    """
    if not (0 <= sda_pin <= 40 and 0 <= scl_pin <= 40):  # Adjust pin range as necessary
        raise ValueError("Pin numbers out of allowable range.")
    return machine.SoftI2C(freq=400000, timeout=50000, sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin))

def initialize_display(i2c):
    """
    Initialize the SSD1306 OLED display.

    Parameters:
        i2c (I2C object): The I2C instance to communicate with the display.

    Returns:
        SSD1306_I2C object: The OLED display instance.

    Raises:
        ConnectionError: If the display cannot be initialized due to I2C communication issues.

    Example:
        >>> i2c = setup_i2c(21, 22)
        >>> initialize_display(i2c)
    """
    try:
        return SSD1306_I2C(128, 64, i2c)
    except Exception as e:
        raise ConnectionError("Failed to initialize the OLED display due to I2C communication error: " + str(e))

def clear_display(oled):
    """
    Clear the display (fill with black).

    Parameters:
        oled (SSD1306_I2C): The OLED display instance.

    Returns:
        None

    Example:
        >>> i2c = setup_i2c(21, 22)
        >>> oled = initialize_display(i2c)
        >>> clear_display(oled)
    """
    oled.fill(0)
    oled.show()

def show_text(oled, text, x, y):
    """
    Display text on the OLED screen.

    Parameters:
        oled (SSD1306_I2C): The OLED display instance.
        text (str): The text to display.
        x (int): X position for the text.
        y (int): Y position for the text.

    Returns:
        None

    Raises:
        ValueError: If x or y positions are out of the display's boundaries.

    Example:
        >>> i2c = setup_i2c(21, 22)
        >>> oled = initialize_display(i2c)
        >>> show_text(oled, 'Hello, World!', 0, 0)
    """
    if not (0 <= x <= 128 and 0 <= y <= 64):  # Assume display dimensions are 128x64
        raise ValueError("Text position out of display's boundaries.")
    oled.text(text, x, y)
    oled.show()
