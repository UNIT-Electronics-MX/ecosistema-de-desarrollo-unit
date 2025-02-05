Arduino IDE
===========

Historia
--------

El **Arduino Integrated Development Environment (IDE)** fue desarrollado para proporcionar una plataforma accesible y fácil de usar para programar placas Arduino y otros microcontroladores compatibles. Su primera versión se lanzó en 2005 junto con la primera placa Arduino, con el objetivo de democratizar el acceso a la programación de hardware para estudiantes, artistas y desarrolladores de todas las áreas.

A lo largo de los años, el IDE ha evolucionado, incorporando soporte para una amplia gama de microcontroladores y arquitecturas, desde los clásicos **ATmega328P** hasta plataformas avanzadas como **ESP32** y **RP2040**. Actualmente, existen dos versiones principales:

- **Arduino IDE 1.x**: Una versión clásica basada en Java, con una interfaz sencilla y un sistema de compilación estable.
- **Arduino IDE 2.x**: Una versión moderna basada en Electron, con funciones avanzadas como autocompletado, depuración en vivo y una mejor experiencia de usuario.

El ecosistema de **Arduino IDE** ha sido clave para el desarrollo de proyectos de electrónica y robótica debido a su facilidad de uso y compatibilidad con múltiples plataformas.



Características Principales
---------------------------

Arduino IDE se distingue por las siguientes características:

- **Interfaz Intuitiva**: Diseñada para facilitar la programación con una curva de aprendizaje baja.
- **Compatibilidad Multiplataforma**: Funciona en Windows, macOS y Linux.
- **Bibliotecas Integradas**: Permite el uso de cientos de bibliotecas para sensores, motores, comunicación inalámbrica, etc.
- **Gestor de Placas**: Soporte para agregar tarjetas adicionales como ESP32, STM32 y RP2040 mediante el **Board Manager**.
- **Compilador Simplificado**: Usa un preprocesador que oculta detalles avanzados de C++, como la declaración de prototipos de funciones.
- **Monitor Serie**: Herramienta integrada para depuración de datos en serie.



Diferencias Clave entre Arduino y un Entorno Nativo
---------------------------------------------------

Capa de Abstracción
~~~~~~~~~~~~~~~~~~

Arduino proporciona una capa de abstracción que facilita la programación de microcontroladores mediante funciones de alto nivel:

.. code-block:: cpp

    pinMode(13, OUTPUT);
    digitalWrite(13, HIGH);
    delay(1000);

Los entornos nativos requieren configurar registros directamente, permitiendo un control más preciso sobre el hardware pero con mayor complejidad:

.. code-block:: c

    DDRB |= (1 << PB5);  // Configura PB5 como salida
    PORTB |= (1 << PB5); // Activa la salida

Compilador y Toolchain
~~~~~~~~~~~~~~~~~~~~~~

- **Arduino** utiliza un **preprocesador** especial que maneja automáticamente detalles como la declaración de funciones.
- **Entornos nativos** como **ESP-IDF** y **Pico-SDK** utilizan compiladores como **GCC** o **Clang**, que permiten una mayor optimización del código.

Portabilidad y Optimización
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Comparación de Portabilidad y Optimización
    :header-rows: 1

    * - **Característica**
      - **Arduino IDE**
      - **Entornos Nativos**
    * - Portabilidad
      - Alto: el mismo código funciona en varias plataformas
      - Baja: optimizado para hardware específico
    * - Rendimiento
      - Moderado
      - Alto: acceso directo al hardware
    * - Consumo de memoria
      - Mayor debido a capas de abstracción
      - Reducido: control total del código


Soporte para Multitarea y RTOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arduino no ofrece soporte nativo para **sistemas operativos en tiempo real (RTOS)**. Sin embargo, algunos fabricantes han extendido la funcionalidad de Arduino con soporte multitarea:

- **ESP-IDF** (ESP32): Utiliza **FreeRTOS** para manejar múltiples tareas simultáneamente.
- **Pico-SDK** (RP2040): Permite gestionar tareas en **núcleos separados**, logrando procesamiento paralelo.



Casos de Uso
------------

Arduino IDE es ampliamente utilizado en diversos ámbitos:

- **Educación**: Ideal para enseñanza de programación y electrónica.
- **Prototipado Rápido**: Desarrollo rápido de pruebas con sensores y actuadores.
- **IoT y Domótica**: Control de dispositivos conectados mediante Wi-Fi y Bluetooth.
- **Robótica**: Programación de robots autónomos y sistemas embebidos.

Gracias a su comunidad y ecosistema en crecimiento, **Arduino IDE** sigue siendo una herramienta fundamental para desarrolladores de hardware en todo el mundo.


Guía de Instalación de Paquetes de Unit Electronics
======================================================

Esta guía proporciona instrucciones paso a paso para instalar los paquetes de soporte de placas necesarios para programar las placas de desarrollo **DualMCU-ONE/DualMCU** (RP2040 + ESP32) y **Cocket Nova CH552** utilizando el entorno Arduino IDE. Estos paquetes permiten el desarrollo en el entorno de Arduino, asegurando una integración fluida con el hardware.


Prerequisitos
-------------

Antes de continuar, asegúrate de tener instaladas las siguientes herramientas:

- `Arduino IDE <https://www.arduino.cc/en/software>`_ – Requerido para programar las placas.
- `Controladores USB <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>`_ – Necesarios para la comunicación con las placas.
- **Paquetes de soporte de placas:**

  - `DualMCU-ONE (ESP32 + RP2040 <https://uelectronics.com/producto/unit-dualmcu-one-esp32-rp2040/>`_
  - `Cocket Nova CH552 <https://uelectronics.com/producto/unit-cocket-nova-ch552g-tarjeta-de-desarrollo/>`_


Instalación Rápida
-------------------

Copia y pega las siguientes URLs en el campo **URLs Adicionales del Gestor de Tarjetas** en las preferencias del Arduino IDE:

.. code-block:: bash

   https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-ESP32-Arduino-Package/main/package_Uelectronics_esp32_index.json
   https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-RP2040-Arduino-Package/main/package_Uelectronics_rp2040_index.json
   https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-CH552-Arduino-Package/refs/heads/develop/package_duino_mcs51_index.json

Luego, busca las placas **Unit Electronics** en el **Gestor de Tarjetas** e instala todos los paquetes necesarios.

Si prefieres una instalación manual, sigue los pasos detallados a continuación.


1. Instalación del Paquete de Placa DualMCU-ONE
-------------------------------------------------

**Paso 1: Instalar el Paquete ESP32**

1. Abre **Arduino IDE**.
2. Ve a **Archivo > Preferencias**.
3. En el campo **URLs Adicionales del Gestor de Tarjetas**, ingresa la siguiente URL:

   .. code-block::

      https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-ESP32-Arduino-Package/main/package_Uelectronics_esp32_index.json

4. Haz clic en **OK** para guardar las preferencias.
5. Ve a **Herramientas > Placa > Gestor de Tarjetas**.
6. Busca **DualMCU**.
7. Haz clic en **Instalar**.
8. Una vez instalado, selecciona **DualMCU** en el menú **Placas**.

**Paso 2: Instalar el Paquete RP2040**

1. Abre **Arduino IDE**.
2. Ve a **Archivo > Preferencias**.
3. En el campo **URLs Adicionales del Gestor de Tarjetas**, ingresa la siguiente URL:

   .. code-block::

      https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-RP2040-Arduino-Package/main/package_Uelectronics_rp2040_index.json

4. Haz clic en **OK** para guardar las preferencias.
5. Ve a **Herramientas > Placa > Gestor de Tarjetas**.
6. Busca **RP2040**.
7. Haz clic en **Instalar**.
8. Una vez instalado, selecciona **RP2040** en el menú **Placas**.

.. figure:: https://raw.githubusercontent.com/Rabadan-uelectronics/DualMCU-RP2040-Arduino-Package/refs/heads/main/releases/download/0.0.0/BoardsManager.png
   :align: center
   :width: 60%

   Ejemplo de instalación en el Gestor de Tarjetas.



2. Instalación del Paquete de Placa Cocket Nova CH552
-------------------------------------------------------

Para programar la placa **Cocket Nova CH552** utilizando Arduino IDE, sigue estos pasos:

1. Abre **Arduino IDE**.
2. Ve a **Archivo > Preferencias**.
3. En el campo **URLs Adicionales del Gestor de Tarjetas**, ingresa la siguiente URL:

   .. code-block::

      https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-CH552-Arduino-Package/refs/heads/develop/package_duino_mcs51_index.json

4. Haz clic en **OK** para guardar las preferencias.
5. Ve a **Herramientas > Placa > Gestor de Tarjetas**.
6. Busca **Cocket Nova**.
7. Haz clic en **Instalar**.
8. Una vez instalado, selecciona **Cocket Nova** en el menú **Placas**.

.. figure:: https://raw.githubusercontent.com/UNIT-Electronics/Uelectronics-CH552-Arduino-Package/refs/heads/main/images/board_json.png
   :align: center
   :width: 60%

   Ejemplo de instalación en el Gestor de Tarjetas.


.. tip::

   Has instalado correctamente los paquetes necesarios para programar las placas de desarrollo **DualMCU-ONE** (ESP32 + RP2040) y **Cocket Nova CH552** en el Arduino IDE. ¡Ahora estás listo para comenzar a desarrollar tus proyectos!

Para documentación adicional e ideas de proyectos, visita **[UNIT Electronics](https://uelectronics.com/)**.

