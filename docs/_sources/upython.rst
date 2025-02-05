MicroPython
===========

MicroPython es una implementación ligera y eficiente del lenguaje de programación Python 3 que está optimizada para ejecutarse en microcontroladores. Está diseñado para ser utilizado en entornos restringidos, lo que lo hace adecuado para el desarrollo de sistemas embebidos. MicroPython proporciona un conjunto rico de bibliotecas y módulos que permiten a los desarrolladores interactuar con componentes de hardware y periféricos, lo que lo convierte en una opción ideal para proyectos de IoT y prototipos.


Comenzando con MicroPython
--------------------------

Comenzar con MicroPython es fácil. La siguiente tabla enumera las placas que son compatibles con MicroPython.

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
