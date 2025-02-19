MicroPython
===========

MicroPython es una implementación ligera y eficiente del lenguaje de programación Python 3 que está optimizada para ejecutarse en microcontroladores. Está diseñado para ser utilizado en entornos restringidos, lo que lo hace adecuado para el desarrollo de sistemas embebidos. MicroPython proporciona un conjunto rico de bibliotecas y módulos que permiten a los desarrolladores interactuar con componentes de hardware y periféricos, lo que lo convierte en una opción ideal para proyectos de IoT y prototipos.


La siguiente tabla enumera las placas que son compatibles con MicroPython.


.. note::

   Para descargar MicroPython y obtener más información sobre cómo instalarlo en una placa de microcontrolador específica, visite el `sitio web oficial de MicroPython <https://www.micropython.org/download/>`__.
.. TABLA DE PLACAS COMPATIBLES CON MICROPYTHON

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - Placa
    - Descripción y Recursos
  * - ESP32
    - ESP32 es una serie de microcontroladores de bajo costo con Wi-Fi y Bluetooth integrados, ideal para aplicaciones IoT. Dispone de un robusto soporte en MicroPython y documentación oficial amplia.
  * - RP2040
    - El chip RP2040, utilizado en la Raspberry Pi Pico, es eficiente y compatible con MicroPython para proyectos educativos, prototipos y sistemas embebidos.
  * - STM32
    - STM32 ofrece microcontroladores de alto rendimiento para aplicaciones en tiempo real, con soporte en MicroPython en varias series (por ejemplo, STM32F4 y STM32F7).
  * - nRF52
    - La serie nRF52 de Nordic Semiconductor se destaca por su bajo consumo y alta eficiencia, ideal para aplicaciones BLE; su compatibilidad con MicroPython está respaldada por documentación y ejemplos prácticos.
  * - Pyboard
    - La Pyboard es la placa oficial de MicroPython, diseñada específicamente para aprovechar al máximo las capacidades de este lenguaje en entornos embebidos.

Características Avanzadas de MicroPython
----------------------------------------

MicroPython es una solución ligera y poderosa para el desarrollo de sistemas embebidos, diseñada para maximizar el rendimiento en dispositivos con recursos limitados sin renunciar a la versatilidad del lenguaje Python. A continuación se detallan sus características principales:

- **REPL Interactivo**: Permite ejecutar y probar fragmentos de código en tiempo real, facilitando la depuración y la experimentación directa en el dispositivo.
- **Interfaz de Hardware Optimizada**: Incorpora bibliotecas para el manejo eficiente de pines GPIO, I2C, SPI, UART y otros periféricos, lo que simplifica la integración con sensores, actuadores y módulos de comunicación.
- **Eficiencia de Recursos**: Sus optimizaciones específicas hacen que MicroPython consuma mínimos recursos, convirtiéndolo en la opción ideal para microcontroladores y dispositivos embebidos con memoria y poder de cómputo limitados.
- **Compatibilidad con Python 3**: Ofrece la facilidad y familiaridad de Python, permitiendo la migración de proyectos y la utilización de una amplia gama de bibliotecas existentes.
- **Facilidad de Integración y Extensión**: Su ecosistema permite la incorporación de módulos externos y soporte para aplicaciones IoT, facilitando la implementación de soluciones complejas.

Sintaxis y Tipado en MicroPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MicroPython mantiene la sintaxis clara y legible de Python 3, combinada con un tipado dinámico que agiliza el proceso de desarrollo. Las principales características incluyen:

.. list-table:: Comparativa de Características de Sintaxis y Tipado
  :widths: 30 70
  :header-rows: 1

  * - Característica
    - Descripción
  * - Sintaxis Simplificada
    - Conserva la legibilidad y estructura de Python 3, facilitando la escritura y el mantenimiento.
  * - Tipado Dinámico
    - Permite la creación de variables sin necesidad de declarar tipos explícitos, acelerando el desarrollo.
  * - Optimización para Hardware Limitado
    - Funciones adaptadas para minimizar el consumo de memoria y maximizar el rendimiento en microcontroladores.
  * - Amplia Compatibilidad
    - Gran parte del ecosistema de Python es utilizable, lo que acelera la integración de herramientas y librerías adicionales.

Más Información y Recursos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para profundizar en el uso de MicroPython y aprovechar al máximo sus capacidades, se recomienda explorar:

- La documentación oficial en el `sitio de MicroPython <https://www.micropython.org/>`__, que ofrece tutoriales, guías y ejemplos de aplicaciones reales.
- Comunidades y foros especializados donde desarrolladores comparten proyectos, soluciones y mejoras.
- Recursos interactivos y cursos en línea que facilitan una adopción rápida y eficiente del entorno MicroPython.

Comenzando con MicroPython
---------------------------

Para iniciar tus proyectos con MicroPython sigue estos pasos:

1. Descarga el firmware adecuado para tu placa desde el `sitio oficial <https://micropython.org/download/>`__.
2. Conecta tu dispositivo mediante un terminal serial (UART) para acceder al REPL, donde podrás interactuar directamente con el microcontrolador.
3. Revisa la documentación y ejemplos disponibles para crear aplicaciones embebidas, desde prototipos simples hasta complejas implementaciones IoT.

Esta versión mejorada reúne información esencial y actualizada, destacando la eficiencia, versatilidad y facilidad de uso de MicroPython para el desarrollo de sistemas embebidos.

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



----------------------------------------


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
