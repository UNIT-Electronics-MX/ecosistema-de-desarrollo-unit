Salidas digitales (GPIO)
========================

Las salidas digitales son una forma de interactuar con el mundo exterior. En la mayoría de los microcontroladores, las salidas digitales se utilizan para encender o apagar LEDs, activar relés, controlar motores y más.

Open-drain y Open-collector

Algunos microcontroladores tienen salidas de drenaje abierto (open-drain) o colector abierto (open-collector). Estas salidas son útiles para la conexión de dispositivos de alta corriente o para la comunicación bidireccional.

- **Open-drain**: La salida puede conectarse a tierra (GND) pero no a VCC.
- **Open-collector**: La salida puede conectarse a VCC pero no a tierra (GND).


.. warning:: 
   MicroPython no se encuentra disponible para la placa de desarrollo Cocket Nova su ejemplo es solo para SDCC.


Parpadeo (blink)
----------------

Un parpadeo de LED es un proyecto común para comenzar con microcontroladores. Lo que no te dicen es la equivalencia de un parpadeo en diferentes plataformas. Para Arduino IDE, MicroPython o SDCC puede difererir en la cantidad de líneas de código, pero el resultado es el mismo: un LED que parpadea.

.. tip:: 
   Con frecuencia, las tarjetas de desarrollo tienen un LED integrado en un pin específico, como el pin 13 en Arduino Uno o el pin 25 en Raspberry Pi Pico.


.. _figura-LED:

.. figure::  /_static/RGB_LED.jpg
   :align: center
   :alt: LEDs
   :width: 60%

    LEDs
    
.. tabs::

    .. tab:: MicroPython

        .. code-block:: python

                from machine import Pin
                import time
                led = Pin(25, Pin.OUT)
                while True:
                        led.value(1)
                        time.sleep(0.5)
                        led.value(0)
                        time.sleep(0.5)

    .. tab:: C++

        .. code-block:: cpp

                void setup() {
                        pinMode(LED_BUILTIN, OUTPUT);
                }

                void loop() {
                        digitalWrite(LED_BUILTIN, HIGH);
                        delay(500);
                        digitalWrite(LED_BUILTIN, LOW);
                        delay(500);
                }



.. _figura-LED:

.. figure::  /_static/ouput_led.png
   :align: center
   :alt: LEDs
   :width: 60%

    LEDs

.. tabs::
    
    .. tab:: SDCC

        .. code-block:: c

            #include "src/system.h" 
            #include "src/gpio.h"  
            #include "src/delay.h"  

            #define PIN_LED P34

            void main(void)
            {
                    CLK_config();
                    DLY_ms(5);

                    PIN_output(PIN_LED);
                    while (1)
                    {
                            PIN_toggle(PIN_LED);
                            DLY_ms(500);
                    }
            }


    .. tab:: C++

        .. code-block:: cpp

            #define LED_BUILTIN 34 // 34 to 33

            void setup() {
            pinMode(LED_BUILTIN, OUTPUT);
            }

            void loop() {
            digitalWrite(LED_BUILTIN, HIGH); 
            delay(500);
            digitalWrite(LED_BUILTIN, LOW);    
            delay(500);
            }



PWM (Modulación por ancho de pulso)
===================================

La modulación por ancho de pulso (PWM) es una técnica utilizada para controlar la cantidad de energía entregada a un dispositivo. En los microcontroladores, el PWM se utiliza para controlar la velocidad de los motores, el brillo de los LEDs y más.


.. tabs::

    .. tab:: C++

        .. code-block:: cpp

                void setup() {
                    pinMode(9, OUTPUT);
                    analogWrite(9, 128);
                }

                void loop() {
                    for (int i = 0; i <= 255; i++) {
                            analogWrite(9, i);
                            delay(10);
                    }
                }

    .. tab:: MicroPython

        .. code-block:: python

                from machine import Pin, PWM
                import time
                pwm = PWM(Pin(25))
                pwm.freq(1000)
                while True:
                    for duty_cycle in range(1024):
                            pwm.duty(duty_cycle)
                            time.sleep(0.01)

    .. tab:: SDCC

        .. code-block:: c

            #include <stdio.h>
            #include "src/config.h"
            #include "src/system.h"
            #include "src/gpio.h"
            #include "src/delay.h"
            #include "src/pwm.h"

            #define MIN_COUNTER 10
            #define MAX_COUNTER 254
            #define STEP_SIZE   10

            void change_pwm(int hex_value)
            {
                PWM_write(PIN_PWM, hex_value);
            }
            void main(void) 
            {

                CLK_config();                          
                DLY_ms(5);                            
                PWM_set_freq(1);                    
                PIN_output(PIN_PWM);       
                PWM_start(PIN_PWM);      
                PWM_write(PIN_PWM, 0);
            while (1) 
            {
                for (int i = MIN_COUNTER; i < MAX_COUNTER; i+=STEP_SIZE) 
                {
                    change_pwm(i);
                    DLY_ms(20);
                }
                for (int i = MAX_COUNTER; i > MIN_COUNTER; i-=STEP_SIZE)
                {
                    change_pwm(i);
                    DLY_ms(20);
                }
                
            }
            }
