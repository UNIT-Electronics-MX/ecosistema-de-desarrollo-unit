Conversión de Analógico a Digital
=================================

Definición de ADC
-----------------

La conversión de analógico a digital (ADC) es un proceso que convierte señales analógicas en valores digitales.
Los microcontroladores utilizan ADC para leer señales analógicas de sensores y otros dispositivos.


.. warning::
   El voltaje de referencia del ADC varía según el microcontrolador. Consulta la hoja de datos del microcontrolador para obtener información específica.

Cuantificación y Codificación de Señales Analógicas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las señales analógicas son continuas y pueden tomar cualquier valor dentro de un rango dado. En cambio, las señales digitales son discretas y solo pueden adoptar valores específicos. La conversión de una señal analógica a digital implica dos pasos: cuantificación y codificación.



.. _figura-ADC:

.. figure::  /_static/adc.png
   :align: center
   :alt: Conversión de Analógico a Digital
   :width: 60%

   Conversión de Analógico a Digital



.. list-table:: Ejemplos de Codificación y Cuantificación
   :widths: 20 20 20
   :align: center
   :header-rows: 1

   * - Resolución
     - Niveles de Cuantificación
     - Código Digital
   * - 8 bits
     - 256
     - ``0x00`` a ``0xFF``
   * - 12 bits
     - 4,096
     - ``0x000`` a ``0xFFF``
   * - 16 bits
     - 65,536
     - ``0x0000`` a ``0xFFFF``


Cuantificación
^^^^^^^^^^^^^^

Divide la señal analógica en niveles discretos. El número de niveles determina la resolución del ADC.

.. note:: 
   La resolución de un ADC se mide en bits y se calcula como 2^n, donde n es el número de bits.


.. list-table:: Resoluciones de ADC
   :widths: 20 20 40
   :align: center
   :header-rows: 1

   * - Resolución
     - Niveles de Cuantificación
     - Descripción
   * - 8 bits
     - 256
     - Un ADC de 8 bits tiene 256 niveles de cuantificación, lo que significa que puede representar la señal analógica con 256 valores diferentes.
   * - 12 bits
     - 4,096
     - Un ADC de 12 bits tiene 4,096 niveles de cuantificación, lo que permite representar la señal analógica con 4,096 valores distintos.
   * - 16 bits
     - 65,536
     - Un ADC de 16 bits tiene 65,536 niveles de cuantificación, permitiendo representar la señal analógica con 65,536 valores distintos.


Codificación 
^^^^^^^^^^^^

Asigna un código digital a cada nivel de cuantificación. Este código digital representa el valor de la señal analógica en dicho nivel.




Código de Ejemplo
-----------------

.. warning:: 
   MicroPython no se encuentra disponible para la placa de desarrollo Cocket Nova su ejemplo es solo para SDCC.

A continuación, se muestra un ejemplo de código para leer continuamente un valor ADC e imprimirlo:

.. note:: 
   El siguiente código está diseñado para funcionar con el microcontrolador RP2040 en la placa de desarrollo DualMCU.

.. tabs::

   .. tab:: MicroPython

      .. code-block:: python

         import machine
         import time

         # Configuración del ADC
         A0 = machine.Pin(26, machine.Pin.IN)  # Inicializar pin A0 para entrada
         adc = machine.ADC(A0)                 # Crear objeto ADC

         # Lectura continua
         while True:
             adc_value = adc.read_u16()        # Leer el valor del ADC
             print(f"Lectura ADC: {adc_value:.2f}")  # Imprimir el valor
             time.sleep(1)                     # Retraso de 1 segundo   

   .. tab:: C++

      .. code-block:: cpp

         // El potenciómetro está conectado al GPIO 26 (ADC0 analógico)
         const int potPin = 26;

         // Variable para almacenar el valor del potenciómetro
         int potValue = 0;

         void setup() {
             Serial.begin(115200);
             analogReadResolution(12);
             delay(1000);
         }

         void loop() {
             // Leer el valor del potenciómetro
             potValue = analogRead(potPin);
             Serial.println(potValue);
             delay(500);
         }

   .. tab:: SDCC

      .. code-block:: c

         #include "src/system.h" 
         #include "src/gpio.h"   
         #include "src/delay.h"  

         #define PIN_ADC P11

         void main(void)
         {
             CLK_config();
             DLY_ms(5);

             ADC_input(PIN_ADC);
             ADC_enable();

             while (1)
             {
                 int data = ADC_read(); // Leer valor ADC (0 - 255, 8 bits)
             }
         }

Clase ADC
---------

La clase ``machine.ADC`` se utiliza para crear objetos ADC que pueden interactuar con los pines analógicos.

.. class:: machine.ADC(pin)

   El constructor de la clase ADC toma un solo argumento: el número de pin.

Ejemplo de Definición
---------------------

Para definir y usar un objeto ADC, sigue este ejemplo:

.. tabs::

   .. tab:: MicroPython

      .. code-block:: python

         import machine
         adc = machine.ADC(0)  # Inicializar ADC en el pin A0

   .. tab:: C++

      .. code-block:: cpp

         #define ADC0 26

Lectura de Valores
------------------

Para leer el valor analógico convertido a formato digital:

.. tabs:: 

   .. tab:: MicroPython

      .. code-block:: python

         adc_value = adc.read() # Leer el valor del ADC
         print(adc_value)  # Imprimir el valor del ADC

   .. tab:: C++

      .. code-block:: cpp

         voltage_write = analogRead(ADC0);

   .. tab:: SDCC

      .. code-block:: c

         int data = ADC_read(); // Leer ADC (0 - 255, 8 bits)
