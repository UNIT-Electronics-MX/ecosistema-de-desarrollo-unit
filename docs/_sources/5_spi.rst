SPI (Interfaz Periférica Serial)
=================================

Explora el protocolo de comunicación SPI y aprende cómo interconectar dispositivos SPI utilizando la placa DualMCU ONE. Te guiaremos en la configuración de la comunicación SPI y en la comunicación con dispositivos SPI.

Visión General del SPI
----------------------

SPI (Interfaz Periférica Serial) es un bus de comunicación síncrono, full-duplex y maestro-esclavo. Se utiliza comúnmente para conectar microcontroladores a periféricos como sensores, pantallas y dispositivos de memoria. La placa de desarrollo DualMCU ONE ofrece capacidades de comunicación SPI, lo que te permite interconectar una amplia gama de dispositivos SPI.

Detalles del Pinout
-------------------

En la siguiente figura, puedes ver los pines SPI en la placa DualMCU ONE y los pines GPIO correspondientes en los microcontroladores ESP32 y RP2040.

.. _figura-spi:

.. figure:: /_static/product/spi_uart.png
  :align: center
  :alt: SPI
  :width: 90%

  Pines SPI

A continuación, se muestra la tabla de asignación de pines para las conexiones SPI en la DualMCU ONE, detallando las conexiones GPIO correspondientes para los microcontroladores ESP32 y RP2040.

.. list-table:: Asignación de Pines SPI
  :widths: 20 20 20
  :header-rows: 1
  :align: center

  * - PIN
    - GPIO ESP32
    - GPIO RP2040
  * - SCK
    - 18
    - 18
  * - MISO
    - 19
    - 16
  * - MOSI
    - 23
    - 19
  * - SS
    - 5
    - 17

.. caution::
  ESP32 y RP2040 tienen conexiones que comparten los mismos pines, por lo que se recomienda utilizar solo un microcontrolador a la vez.
  
  .. list-table:: Pines compartidos
    :widths: 20 20 
    :header-rows: 1
    :align: center

    * - GPIO ESP32
      - GPIO RP2040
    * - 5
      - 13
    * - 18
      - 14
    * - 23
      - 12

SPI entre ESP32 y RP2040
------------------------

La placa DualMCU ONE fue diseñada para ser compatible con los microcontroladores ESP32 y RP2040. Por ello, es posible compartir información entre ambos microcontroladores utilizando el protocolo SPI. Para ello, utilizaremos los siguientes pines:

.. list-table:: Conexiones SPI
  :widths: 25 25 25 25
  :header-rows: 1
  :align: center

  * - Pin 
    - SPI RP2040
    - Pin 
    - SPI ESP32
  * - SCK
    - 14
    - SCK
    - 18
  * - MISO 
    - 12
    - MOSI
    - 23
  * - MOSI 
    - 15
    - MISO
    - 14
  * - SS
    - 13
    - SS
    - 5
  * - READY
    - 7
    - READY
    - 33
  * - RESET
    - 16
    - RESET
    - RST 

.. caution::
  La conexión RST no existe físicamente; por lo tanto, es necesario establecer una conexión externa.
 

SDCard SPI
----------

.. warning::

   Asegúrate de que la Micro SD contenga datos. Se recomienda guardar múltiples archivos de antemano para facilitar su uso.


.. _figura-micro-sd-card:

.. figure:: /_static/Micro-SD-Card-Pinout.png
  :align: center
  :alt: Pinout de la Micro SD
  :width: 40%

  Pinout de la Micro SD

Biblioteca (MicroPython)
~~~~~~~~~~~~~~~~~~~~~~~~~~

La biblioteca `dualmcu.py` para MicroPython en ESP32 y RP2040 es compatible con la lectura y escritura en la Micro SD. La biblioteca proporciona una interfaz sencilla para leer y escribir archivos en la tarjeta SD. La biblioteca está disponible en PyPi y se puede instalar mediante el IDE Thonny.

**Instalación**

1. Abre `Thonny <https://thonny.org/>`_.
2. Navega a **Tools** -> **Manage Packages**.
3. Busca ``dualmcu`` y haz clic en **Install**.

Para más información, revisa la sección 

  - Biblioteca DualMCU ONE

Alternativamente, descarga la biblioteca desde `dualmcu.py <https://pypi.org/project/dualmcu/>`_.


VSPI y HSPI
**Interfaz VSPI**
.. _figura-micro-sd-card-reader:

.. figure:: /_static/Lector-Micro-SD.jpg
  :align: center
  :alt: Lector externo de Micro SD
  :width: 40%

  Lector externo de Micro SD

Las conexiones son las siguientes:

Esta tabla ilustra las conexiones entre la tarjeta SD y los pines GPIO en los microcontroladores ESP32 y RP2040.

.. list-table:: Conexiones VSPI
  :widths: 10 20 20 20
  :header-rows: 1
  :align: center

  * - Tarjeta SD
    - Nombre del Pin
    - ESP32
    - RP2040
  * - D3
    - SS
    - 5
    - 17
  * - CMD
    - MOSI
    - 23
    - 19
  * - VSS
    - GND
    - 
    - 
  * - VDD
    - 3.3V
    - 
    - 
  * - CLK
    - SCK
    - 18
    - 18
  * - D0
    - MISO
    - 19
    - 16

Descripciones
"""""""""""""
   - SCK (Reloj Serial)
   - SS (Selección del Esclavo)


.. code-block:: python

  import machine, os
  from dualmcu import *

  SCK_PIN = 18
  MOSI_PIN = 23
  MISO_PIN = 19
  CS_PIN = 5

  spi = machine.SPI(1, baudrate=100000, polarity=0, phase=0, sck=machine.Pin(SCK_PIN), mosi=machine.Pin(MOSI_PIN), miso=machine.Pin(MISO_PIN))
  spi.init()
  sd = SDCard(spi, machine.Pin(CS_PIN))
  os.mount(sd, '/sd')
  os.listdir('/')

  print("archivos ...")
  print(os.listdir("/sd"))


**Interfaz HSPI**
  
Esta tabla detalla las conexiones entre la tarjeta SD y el microcontrolador ESP32.

.. list-table:: Conexiones HSPI
  :widths: 10 20 20
  :header-rows: 1
  :align: center

  * - Tarjeta SD
    - ESP32
    - PIN
  * - D2
    - 
    - 12
  * - D3
    - SS (Selección del Esclavo)
    - 13
  * - CMD
    - MOSI
    - 15
  * - VSS
    - GND
    -
  * - VDD
    - 3.3V
    - 
  * - CLK
    - SCK (Reloj Serial)
    - 14
  * - VSS
    - GND
    - 
  * - D0
    - MISO
    - 2
  * - D1
    - 
    - 4

Para la prueba, utilizaremos un ESP32 WROM-32E y una tarjeta SanDisk Micros Ultra con una capacidad de 32 GB.

.. code-block:: python

  import machine
  import os
  from dualmcu import *

  # Inicializa la interfaz SPI para la tarjeta SD
  spi = machine.SPI(2, baudrate=1000000, polarity=0, phase=0, sck=machine.Pin(14), mosi=machine.Pin(15), miso=machine.Pin(2))

  # Inicializa la tarjeta SD
  sd = SDCard(spi, machine.Pin(13))

  # Monta el sistema de archivos
  vfs = os.VfsFat(sd)
  os.mount(vfs, "/sd")

  # Lista los archivos en la raíz de la tarjeta SD
  print("Archivos en la raíz de la tarjeta SD:")
  print(os.listdir("/sd"))

  os.umount("/sd") 


SPI (Arduino IDE)
~~~~~~~~~~~~~~~~~~

Arduino IDE es compatible tanto con la lectura como con la escritura en la tarjeta Micro SD. La biblioteca proporciona una interfaz sencilla para leer y escribir archivos en la tarjeta SD.


.. tabs::

  .. tab:: VSPI 

   .. code-block::

