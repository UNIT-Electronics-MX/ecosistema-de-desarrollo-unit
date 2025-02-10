Interfaz USB
============

La interfaz USB es un protocolo de comunicación que permite la conexión de dispositivos electrónicos a una computadora. En el caso de los microcontroladores, la interfaz USB permite la comunicación con una computadora para la transferencia de datos, actualización de firmware, depuración, etc.

HID (Dispositivo de Interfaz Humano)
------------------------------------

HID (Human Interface Device) es un protocolo de comunicación USB que permite a los dispositivos electrónicos interactuar con un usuario. Los dispositivos HID incluyen teclados, ratones, joysticks, gamepads, etc.

.. figure:: /_static/cocket/hid_example.png
   :align: center
   :alt: HID
   :width: 60%

   Ejemplo de Dispositivo HID

.. raw:: html

    <table style="width: 100%; border-collapse: collapse; border: 1px solid #ccc;">
    <tr>
        <th style="border: 1px solid #ccc; padding: 8px;">Biblioteca</th>
        <th style="border: 1px solid #ccc; padding: 8px;">Enlace</th>
    </tr>
    <tr>
        <td style="border: 1px solid #ccc; padding: 8px;">HID Teclado y Ratón </td>
        <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/UNIT-Electronics/CH55x_SDCC_Examples/tree/main/Software/examples/USB/USB-HID" target="_blank">HID device</a></td>
    </tr>
   </table>
   

CDC (Clase de Dispositivo de Comunicación)
------------------------------------------

CDC (Communication Device Class) es una clase de dispositivos USB que permite la comunicación entre un dispositivo y una computadora. Los dispositivos CDC incluyen módems, adaptadores de red, etc.


.. raw:: html

    <table style="width: 100%; border-collapse: collapse; border: 1px solid #ccc;">
    <tr>
        <th style="border: 1px solid #ccc; padding: 8px;">Biblioteca</th>
        <th style="border: 1px solid #ccc; padding: 8px;">Enlace</th>
    </tr>

    <tr>
        <td style="border: 1px solid #ccc; padding: 8px;">Comunicacion serial virtual </td>
        <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/UNIT-Electronics/CH55x_SDCC_Examples/blob/main/Software/examples/USB/README.md" target="_blank">USB CDC Serial for CH55x</a></td>
    </tr>
    </table>


MIDI (Interfaz Digital de Instrumentos Musicales)
------------------------------------------------

MIDI (Musical Instrument Digital Interface) es un protocolo de comunicación que permite a los dispositivos electrónicos comunicarse entre sí para la creación, edición y reproducción de música. Los dispositivos MIDI incluyen teclados, sintetizadores, controladores, etc.

Micrófono USB
-------------


.. raw:: html

    <table style="width: 100%; border-collapse: collapse; border: 1px solid #ccc;">
    <tr>
        <th style="border: 1px solid #ccc; padding: 8px;">Biblioteca</th>
        <th style="border: 1px solid #ccc; padding: 8px;">Enlace</th>
    </tr>

    <tr>
        <td style="border: 1px solid #ccc; padding: 8px;">Micrófono</td>
        <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/UNIT-Electronics/UNIT-PDM-MEMS-Microphone-Breakout-Guide-UF2" target="_blank">USB MIDI</a></td>

    </tr>
    <tr>
        <td style="border: 1px solid #ccc; padding: 8px;"> Descarga archivo UF2 </td>
        <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/UNIT-Electronics/DualMCU/blob/main/Software/UF2_Files/usb_microphone.uf2" target="_blank">Descargar UF2</a></td>
    </table>


.. figure:: /_static/dualmcu/AR3631-UNIT-MP34DT05TR-A-Modulo-Microfono-PDM-V2.jpg
   :align: center
   :alt: micrófono usb
   :width: 50%

   Micrófono USB DualMCU

Este archivo transforma el DualMCU en un micrófono USB de alto rendimiento utilizando el microcontrolador RP2040. Para utilizar esta funcionalidad, conecta un micrófono MEMS PDM (Pulse Density Modulation), como:

- **MP34DT06J**
- **UNIT PDM MEMS Microphone MP34DT05**

Esta funcionalidad es ideal para videoconferencias o aplicaciones de audio en general, proporcionando un rendimiento de sonido de alta calidad.




Conexión de un micrófono PDM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para conectar un **micrófono PDM UNIT MP34DT05TR-A** o un **módulo de micrófono PDM de Adafruit** al RP2040 en la placa DualMCU, sigue estos pasos:

1. Asegúrate de tener el hardware necesario: un módulo de micrófono PDM y la placa DualMCU.
2. Ubica los pines GPIO12 y GPIO13 en la placa DualMCU [(Diagrama de pines)](https://github.com/UNIT-Electronics/DualMCU/blob/main/Hardware/Resources/EU0002-DUALMCU%20V3.1.2.jpg) y conecta el micrófono de la siguiente manera:

.. list-table:: Conexión entre DualMCU y PDM-MIC
    :widths: 25 75
    :header-rows: 1

    * - DualMCU
      - PDM-MIC
    * - 3.3V
      - 3.3V
    * - GND
      - GND
    * - GPIO12
      - Señal SCL
    * - GPIO13
      - Señal DAT

.. figure:: /_static/dualmcu/MicConectionsJST1.jpg
   :align: center
   :alt: micrófono usb
   :width: 50%

   Micrófono USB DualMCU

3. Enciende la placa DualMCU y el módulo de micrófono.
4. Entra en modo BOOT en el RP2040 y arrastra y suelta el archivo `usb_microphone.uf2` en la placa DualMCU.


Ejemplo Completo en `UNIT-PDM-MEMS-Microphone-Breakout-Guide-UF2 <https://github.com/UNIT-Electronics/UNIT-PDM-MEMS-Microphone-Breakout-Guide-UF2#readme>`_

