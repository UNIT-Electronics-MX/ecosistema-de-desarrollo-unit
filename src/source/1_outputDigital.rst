Salidas digitales 
==================

Las salidas digitales son una forma de interactuar con el mundo exterior. En la mayoría de los microcontroladores, las salidas digitales se utilizan para encender o apagar LEDs, activar relés, controlar motores y más.


.. tip::
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
    :width: 30%

    RGB_LED

MicroPython y Arduino IDE
~~~~~~~~~~~~~~~~~~~~~~~~~



.. note::
     En el siguiente ejemplo, se utiliza el pin 25 para el LED en la placa de desarrollo DualMCU RP2040. Modifica el pin según la placa de desarrollo que estés utilizando.
     
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

                     #define LED_BUILTIN 25

                     void setup() {
                                pinMode(LED_BUILTIN, OUTPUT);
                     }

                     void loop() {
                                digitalWrite(LED_BUILTIN, HIGH);
                                delay(500);
                                digitalWrite(LED_BUILTIN, LOW);
                                delay(500);
                     }

.. only:: html

    .. figure:: /_static/dualmcu/blink.gif
        :align: center
        :alt: figura-gif
        :width: 60%


Arduino IDE y SDCC 
~~~~~~~~~~~~~~~~~~

.. _figura_output_led:

.. figure::  /_static/cocket/ouput_led.png
    :align: center
    :alt: LEDs
    :width: 60%

    LEDs

.. tabs::

     .. tab:: C++

          .. code-block:: cpp

                #define LED_BUILTIN 34

                void setup() {
                pinMode(LED_BUILTIN, OUTPUT);
                }

                void loop() {
                digitalWrite(LED_BUILTIN, HIGH); 
                delay(500);
                digitalWrite(LED_BUILTIN, LOW);    
                delay(500);
                }

     
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

Modulación por ancho de pulso (PWM)
===================================

La modulación por ancho de pulso (PWM) es una técnica utilizada para controlar la cantidad de energía entregada a un dispositivo. En los microcontroladores, el PWM se utiliza para controlar la velocidad de los motores, el brillo de los LEDs y más.

.. warning:: 
    El soporte de ubicación para salidas PWM depende de la placa de desarrollo. Revisar la documentación de la placa para conocer los pines PWM disponibles.

.. only:: html

    .. figure:: /_static/cocket/pwm.gif
        :align: center
        :alt: figura-gif
        :width: 60%

Implementación
---------------

MicroPython y Arduino IDE
~~~~~~~~~~~~~~~~~~~~~~~~~


.. tabs::


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


Arduino IDE y SDCC
~~~~~~~~~~~~~~~~~~


.. only:: html

    .. figure:: /_static/cocket/led.gif
        :align: center
        :alt: figura-gif
        :width: 60%

.. tabs::

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


     .. tab:: C++

          .. code-block:: cpp

                     #define led 34

                     int brightness = 0;
                     int fadeAmount = 5;

                     void setup() {
                          pinMode(led, OUTPUT);
                     }

                     void loop() {
                          analogWrite(led, brightness);
                          brightness = brightness + fadeAmount;
                          if (brightness <= 0 || brightness >= 255) {
                                fadeAmount = -fadeAmount;
                          }
                          delay(30);
                     }

Aplicaciones
------------
 
Control de servomotores - MicroPython RP2040
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Los servomotores son dispositivos que se utilizan para controlar la posición de un objeto. Se utilizan en aplicaciones como robots, drones, juguetes y más.

Requieren de una señal PWM para controlar la posición del eje del motor. La mayoría de los servomotores aceptan una señal PWM con una frecuencia de 50 Hz y un ciclo de trabajo de 0.5 ms a 2.5 ms.

.. figure::  /_static/dualmcu/dualmcu_pwm.jpg
    :align: center
    :alt: Servomotor
    :width: 70%
    
    Diagrama de conexión del servomotor

.. tabs::
     
     .. tab:: MicroPython

          .. code-block:: python

               import machine
               import utime

               servo_pin = machine.Pin(0)
               pwm_servo = machine.PWM(servo_pin)
               pwm_servo.freq(50)

               def set_servo_angle(angle):
                    duty_cycle = int(1024 + (angle / 180) * 3072)
                    pwm_servo.duty_u16(duty_cycle)

               try:
                    while True:
                         for angle in range(0, 181, 10):
                              set_servo_angle(angle)
                              utime.sleep(0.1)
                         for angle in range(180, -1, -10):
                              set_servo_angle(angle)
                              utime.sleep(0.1)
               except KeyboardInterrupt:
                    pwm_servo.deinit()
                    print("\nPWM detenido. Recursos liberados.")

     .. tab:: C++

          .. code-block:: cpp

               #define SERVO_PIN 0

               void setup() {
                    pinMode(SERVO_PIN, OUTPUT);
               }

               void loop() {
                    for (int i = 40; i <= 115; i++) {
                              analogWrite(SERVO_PIN, i);
                              delay(500);
                    }
               }