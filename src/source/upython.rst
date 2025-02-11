MicroPython
===========

MicroPython es una implementación ligera y eficiente del lenguaje de programación Python 3 que está optimizada para ejecutarse en microcontroladores. Está diseñado para ser utilizado en entornos restringidos, lo que lo hace adecuado para el desarrollo de sistemas embebidos. MicroPython proporciona un conjunto rico de bibliotecas y módulos que permiten a los desarrolladores interactuar con componentes de hardware y periféricos, lo que lo convierte en una opción ideal para proyectos de IoT y prototipos.


La siguiente tabla enumera las placas que son compatibles con MicroPython.

.. TABLA DE PLACAS COMPATIBLES CON MICROPYTHON

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - Placa
    - Descripción
  * - ESP32
    - ESP32 es una serie de microcontroladores de sistema en un chip de bajo costo y bajo consumo con Wi-Fi integrado y Bluetooth de doble modo. Es ampliamente utilizado en aplicaciones de IoT y es compatible con MicroPython.
  * - RP2040
    - RP2040 es un chip microcontrolador desarrollado por Raspberry Pi. Se utiliza en la placa de desarrollo Raspberry Pi Pico y es compatible con MicroPython.
  * - STM32
    - STM32 es una serie de chips microcontroladores desarrollados por STMicroelectronics. Es ampliamente utilizado en sistemas embebidos y es compatible con MicroPython.
  * - nRF52
    - nRF52 es una serie de chips microcontroladores desarrollados por Nordic Semiconductor. Se utiliza en aplicaciones de Bluetooth Low Energy (BLE) y es compatible con MicroPython.

Características de MicroPython
------------------------------

MicroPython ofrece varias características que lo hacen adecuado para el desarrollo de sistemas embebidos:

- **REPL Interactivo**: MicroPython proporciona un bucle de lectura-evaluación-impresión (REPL) interactivo que permite a los desarrolladores ejecutar comandos de Python directamente en el microcontrolador, lo que facilita la creación rápida de prototipos y pruebas.

- **Interfaz de Hardware**: MicroPython incluye bibliotecas y módulos que permiten a los desarrolladores interactuar con componentes de hardware como pines GPIO, I2C, SPI, UART y más, lo que facilita la interfaz con sensores, actuadores y otros periféricos.

Comenzando con MicroPython
--------------------------

Para comenzar con MicroPython, necesitarás una placa de microcontrolador que sea compatible con MicroPython, como el ESP32 o el RP2040. Aquí están los pasos generales para comenzar con MicroPython:

1. **Instalar el Firmware de MicroPython**: Descarga el firmware de MicroPython para tu placa de microcontrolador desde el sitio web oficial de MicroPython y flashealo en la placa usando una herramienta como esptool o rshell.

2. **Conectar a la Placa**: Usa un programa de terminal serial para conectarte a la placa a través de una conexión serial (UART) para acceder al REPL de MicroPython.

3. **Escribir y Ejecutar Código Python**: Escribe código Python usando el REPL interactivo o un editor de texto, y ejecútalo en la placa para interactuar con componentes de hardware y periféricos.

Bibliotecas y Módulos de MicroPython
------------------------------------

MicroPython proporciona un conjunto rico de bibliotecas y módulos que permiten a los desarrolladores trabajar con componentes de hardware y periféricos. Algunas de las bibliotecas y módulos clave disponibles en MicroPython incluyen:

- **machine**: Proporciona clases y funciones para interactuar con componentes de hardware como pines GPIO, I2C, SPI, UART y más.
- **network**: Incluye clases y funciones para trabajar con interfaces de red, como Wi-Fi y Ethernet, lo que permite aplicaciones de IoT.

IDEs y Herramientas de MicroPython
----------------------------------

Hay varios Entornos de Desarrollo Integrados (IDEs) y herramientas disponibles para trabajar con MicroPython, tales como:

- **Thonny**: Un IDE amigable para principiantes para Python que incluye soporte para MicroPython, proporcionando características como edición de código, REPL y transferencia de archivos.
- **uPyCraft**: Un IDE ligero para el desarrollo de MicroPython que incluye características como edición de código, transferencia de archivos y comunicación serial con la placa.
- **rshell**: Una herramienta de línea de comandos para acceder y gestionar archivos en una placa de MicroPython a través de una conexión serial, lo que permite la transferencia de archivos y el acceso al REPL.

Guía de Instalación Usando la Biblioteca MIP
============================================

.. note::
   El soporte directo para mip en RP2040 no está disponible. Se utiliza la biblioteca `mip` para instalar la biblioteca `max1704x.py`.

Requisitos
~~~~~~~~~~

- Dispositivo ESP32
- IDE Thonny
- Credenciales de Wi-Fi (SSID y Contraseña)

Instrucciones de Instalación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Siga los pasos a continuación para instalar la biblioteca `max1704x.py`:

Conectar a Wi-Fi
~~~~~~~~~~~~~~~~

Copie y ejecute el siguiente código en Thonny para conectar su ESP32 a una red Wi-Fi:


.. code-block:: python

   import mip
   import network
   import time

   def connect_wifi(ssid, password):
      wlan = network.WLAN(network.STA_IF)
      wlan.active(True)
      wlan.connect(ssid, password)

      for _ in range(10):
         if wlan.isconnected():
               print('Conectado a la red Wi-Fi')
               return wlan.ifconfig()[0]
         time.sleep(1)

      print('No se pudo conectar a la red Wi-Fi')
      return None


   ssid = "tu_ssid"
   password = "tu_contraseña"

   ip_address = connect_wifi(ssid, password)
   print(ip_address)
   mip.install('https://raw.githubusercontent.com/UNIT-Electronics/MAX1704X_lib/refs/heads/main/Software/MicroPython/example/max1704x.py')
   mip.install('https://raw.githubusercontent.com/Cesarbautista10/Libraries_compatibles_with_micropython/refs/heads/main/Libs/oled.py')
   mip.install('https://raw.githubusercontent.com/Cesarbautista10/Libraries_compatibles_with_micropython/refs/heads/main/Libs/sdcard.py')


Biblioteca DualMCU
------------------

En primer lugar, debe instalar el IDE Thonny. Puede descargarlo desde el `sitio web de Thonny <https://thonny.org/>`__.

1. Abra `Thonny <https://thonny.org/>`__.
2. Navegue a **Herramientas** -> **Administrar paquetes**.
3. Busque ``dualmcu`` y haga clic en **Instalar**.

.. _figure_dualmcu_libary:
.. figure:: /_static/dualmcu_library.png
   :align: center
   :alt: Biblioteca DualMCU
   :width: 60%
   
   Biblioteca DualMCU

4. Biblioteca instalada correctamente.

.. _figure_dualmcu_libary_success:
.. figure:: /_static/dualmcu_library_success.png
   :align: center
   :alt: Biblioteca DualMCU
   :width: 60%
   
   Biblioteca DualMCU instalada correctamente

Alternativamente, descargue la biblioteca desde `dualmcu.py <https://pypi.org/project/dualmcu/>`__.


Uso
^^^

La biblioteca proporciona un conjunto de herramientas para ayudar a los desarrolladores a trabajar con la placa DualMCU ONE. Las siguientes son las principales características de la biblioteca:

- **Soporte I2C**: La biblioteca ofrece soporte para el protocolo de comunicación I2C, facilitando la conexión con una amplia gama de sensores y dispositivos.

- **Compatibilidad con Shields de Arduino**: La biblioteca es compatible con Shields de Arduino, lo que permite utilizar una gran variedad de shields y accesorios con la placa DualMCU ONE.

- **Soporte para SDcard**: La biblioteca ofrece soporte para tarjetas SD, permitiendo a los desarrolladores leer y escribir datos en tarjetas SD de forma sencilla.


Ejemplos de uso de la biblioteca:

.. code-block:: python

    import machine
    from dualmcu import *

    i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

    oled = SSD1306_I2C(128, 64, i2c)

    oled.fill(1)
    oled.show()

    oled.fill(0)
    oled.show()
    oled.text('UNIT', 50, 10)
    oled.text('ELECTRONICS', 25, 20)

    oled.show()


Bibliotecas disponibles
^^^^^^^^^^^^^^^^^^^^^^^^^

- `Dualmcu <https://pypi.org/project/dualmcu/>`__ : Esta biblioteca ofrece un conjunto de herramientas para ayudar a los desarrolladores a trabajar con la placa DualMCU ONE. La biblioteca se mantiene y actualiza activamente para brindar la mejor experiencia a los desarrolladores que utilizan la placa DualMCU ONE. Para más información y actualizaciones, visite el `repositorio de GitHub dualmcu`__
- `Ocks <https://pypi.org/project/ocks/>`__ : Esta biblioteca proporciona soporte para el protocolo de comunicación I2C.
- `SDcard-lib <https://pypi.org/project/sdcard-lib/>`__ : Esta biblioteca ofrece soporte para tarjetas SD, permitiendo a los desarrolladores leer y escribir datos en tarjetas SD; todos los derechos pertenecen al autor original.


La biblioteca se mantiene y actualiza activamente para brindar la mejor experiencia a los desarrolladores que utilizan la placa DualMCU ONE. Para más información y actualizaciones, visite el `repositorio de GitHub dualmcu`__
