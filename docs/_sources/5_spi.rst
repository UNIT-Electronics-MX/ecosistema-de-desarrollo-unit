SPI (Interfaz Periférica Serial)
=================================

.. warning::

  El soporte para la tarjeta de desarrollo Cocket Nova  (CH552) se encuentra en desarrollo. Por favor, mantente atento a futuras actualizaciones.



Visión General del SPI
----------------------

SPI (Interfaz Periférica Serial) es un bus de comunicación síncrono, full-duplex y maestro-esclavo. Se utiliza comúnmente para conectar microcontroladores a periféricos como sensores, pantallas y dispositivos de memoria. La placa de desarrollo DualMCU ONE ofrece capacidades de comunicación SPI, lo que te permite interconectar una amplia gama de dispositivos SPI.


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

DualMCU ONE RP2040 y ESP32
~~~~~~~~~~~~~~~~~~~~~~~~~~

La placa de desarrollo DualMCU ONE está equipada con dos microcontroladores, el ESP32 y el RP2040. Ambos microcontroladores ofrecen soporte para la comunicación SPI, lo que te permite conectar dispositivos SPI a la placa de desarrollo.


.. list-table:: Configuración SPI cruzado entre ESP32 y RP2040
  :widths: 20 20 20 20
  :header-rows: 1
  :align: center

  * - ESP32
    - RP2040
    - GPIO
    - GPIO
  * - SCK
    - SCK
    - 18
    - 14
  * - MISO
    - MOSI
    - 23
    - 15
  * - MOSI
    - MISO
    - 19
    - 12
  * - SS
    - SS
    - 5
    - 13

.. tabs:: 

  .. tab:: MicroPython RP2040

    .. code-block:: python

      from machine import Pin, SPI
      import time

      # RP2040 pin configuration
      rp2040_cs = Pin(13, Pin.OUT)   # Chip Select (CS)
      spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(15), miso=Pin(12))

      # rp2040_cs = Pin(21, Pin.OUT)   # Chip Select (CS)
      # spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(20))


      def spi_send_command(command, response_length=3):
          # Seleccionar el dispositivo SPI (bajar CS)
          rp2040_cs.value(0)
          time.sleep_us(10)  # Breve pausa para estabilizar CS
          
          # Asegurarte de que ambos buffers (envío y respuesta) sean del mismo tamaño
          send_buffer = bytearray(response_length)
          response = bytearray(response_length)  # Buffer de respuesta de 2 bytes, igual que send_buffer

          # Copiar el comando en el buffer de envío (solo el primer byte)
          send_buffer[0] = command[0]

          # Enviar el comando y recibir la respuesta
          spi.write_readinto(send_buffer, response)
          
          # Deseleccionar el dispositivo SPI (subir CS)
          time.sleep_us(1)
          rp2040_cs.value(1)
          
          return response

      def main():
          # Lista de comandos para enviar al ESP32 (cada comando es de 1 byte)
          commands = [
              b'\x01',  # Comando 0x01: Solicitar estado general de memoria
              b'\x02',  # Comando 0x02: Solicitar memoria libre
              b'\x03',  # Comando 0x03: Solicitar estado de los registros
              b'\x21'   # Comando 0x04: Solicitar temperatura
          ]
          
          while True:
              for command_to_send in commands:
                  # Enviar el comando y recibir la respuesta
                  response = spi_send_command(command_to_send, response_length=3)  # Ajustado para 2 bytes
                  
                  # Imprimir el comando enviado y la respuesta recibida
                  print(f"Sent command: {command_to_send.hex()} | Received response:", response)
                  
                  time.sleep(1)  # Tiempo de espera entre comandos

      main()


  .. tab:: ESP-IDF ESP32

    .. code-block:: c

      #include <stdio.h>
      #include <string.h>
      #include "driver/spi_slave.h"
      #include "driver/gpio.h"
      #include "esp_log.h"
      #include "esp_system.h"  // Para funciones del sistema como esp_get_free_heap_size
      #include "esp_heap_caps.h"  // Para asignación de memoria compatible con DMA

      // ESP32 WROOM 32E

      #define PIN_NUM_MISO 23
      #define PIN_NUM_MOSI 14
      #define PIN_NUM_CLK  18
      #define PIN_NUM_CS   5
      #define SPIHOST    HSPI_HOST
      #define ESP32_state  0



      #define CMD_START_RX 0XE0
      #define CMD_END_RX 0XEE

      static const char *TAG = "SPI_SLAVE";

      // Buffer de 2 bytes para la transmisión SPI
      uint8_t PK_BUFF[2];

      // Función para procesar el comando recibido por SPI
      void process_command(uint8_t *command) {

          // delete start and end command choose the command 
          // command length is 1 byte
          
          ESP_LOGI(TAG, "Received command: %02X", command[0]);

          // Simular una respuesta según el comando recibido
          switch (command[0]) {
              case 0x01:  // Comando 0x01: Retornar estado de la memoria
                  PK_BUFF[0] = 0x53;  // Ejemplo de estado de memoria
                  PK_BUFF[1] = 0x4f;
                  break;
              case 0x02:  // Comando 0x02: Retornar memoria disponible
                  PK_BUFF[0] = 0x59;  // Simular datos
                  PK_BUFF[1] = 0x2D;
                  break;
              case 0x03:  // Comando 0x03: Retornar estado de registros
                  PK_BUFF[0] = 0x28;
                  PK_BUFF[1] = 0x29;
                  break;
              case 0x21:  // Comando 0x04: Name ascii 32, S3, C6
                  PK_BUFF[0] = 0x4f;  
                  PK_BUFF[1] = 0x4b;
    
                  break;
              default:
                  PK_BUFF[0] = 0x00;  // Comando desconocido
                  PK_BUFF[1] = 0x00;
                  break;
          }
      }

      void app_main(void) {
          // Configuración del bus SPI
          spi_bus_config_t buscfg = {
              .mosi_io_num = PIN_NUM_MOSI,
              .miso_io_num = PIN_NUM_MISO,
              .sclk_io_num = PIN_NUM_CLK,
              .quadwp_io_num = -1,
              .quadhd_io_num = -1,
          };

          // Configuración de la interfaz SPI como esclavo
          spi_slave_interface_config_t slvcfg = {
              .spics_io_num = PIN_NUM_CS,
              .flags = 0,
              .queue_size = 6,  // Aumentar el tamaño de la cola para mejorar el rendimiento
              .mode = 0,
          };

          // Inicializar el bus SPI como esclavo
          esp_err_t ret = spi_slave_initialize(SPIHOST, &buscfg, &slvcfg, SPI_DMA_CH_AUTO);
          ESP_ERROR_CHECK(ret);

          // Asignar buffers de 4 bytes para enviar y recibir datos
          uint8_t *sendbuf = (uint8_t *)heap_caps_malloc(4, MALLOC_CAP_DMA);
          uint8_t *recvbuf = (uint8_t *)heap_caps_malloc(4, MALLOC_CAP_DMA);

          if (sendbuf == NULL || recvbuf == NULL) {
              ESP_LOGE(TAG, "Failed to allocate DMA-capable memory");
              return;
          }

          memset(sendbuf, 0, 4);  // Inicializar el buffer de envío

          spi_slave_transaction_t t;
          memset(&t, 0, sizeof(t));  // Inicializar la estructura de transacción SPI

          while (1) {
              // Esperar un comando desde el maestro
              t.length = 8 * 2;  // Recibir 1 byte de comando y enviar 2 bytes de respuesta
              t.tx_buffer = sendbuf;
              t.rx_buffer = recvbuf;

              // Realizar la transacción SPI
              ret = spi_slave_transmit(SPIHOST, &t, portMAX_DELAY);
              ESP_ERROR_CHECK(ret);

              // Procesar el comando recibido
              process_command(recvbuf);

              // Copiar el resultado de PK_BUFF al buffer de envío
              sendbuf[0] = PK_BUFF[0];
              sendbuf[1] = PK_BUFF[1];
          }
      }
          


SDCard SPI
---------------------

.. warning::

   Asegúrate de que la Micro SD contenga datos. Se recomienda guardar múltiples archivos de antemano para facilitar su uso.


Biblioteca (MicroPython)
~~~~~~~~~~~~~~~~~~~~~~~~~~

La biblioteca `dualmcu.py` para MicroPython en ESP32 y RP2040 es compatible con la lectura y escritura en la Micro SD. La biblioteca proporciona una interfaz sencilla para leer y escribir archivos en la tarjeta SD. La biblioteca está disponible en PyPi y se puede instalar mediante el IDE Thonny.

.. raw:: html

      <table style="width: 100%; border-collapse: collapse; border: 1px solid #ccc;">
        <tr>
          <th style="border: 1px solid #ccc; padding: 8px;">Biblioteca</th>
          <th style="border: 1px solid #ccc; padding: 8px;">Enlace</th>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">ocks</td>
          <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://pypi.org/project/ocks/" target="_blank">Ejemplo de instalación</a></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">dualmcu</td>
          <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://pypi.org/project/dualmcu/" target="_blank">Biblioteca DualMCU</a></td>
        </tr>
      </table>


VSPI y HSPI
~~~~~~~~~~~~

La diferencia entre VSPI y HSPI radica en la velocidad de transferencia de datos. VSPI es más lento que HSPI, pero es más fácil de configurar. HSPI, por otro lado, es más rápido pero requiere una configuración más detallada.

Interfaz VSPI
^^^^^^^^^^^^^^

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


Interfaz HSPI
^^^^^^^^^^^^^^

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
    - 
  * - D3
    - SS (Selección del Esclavo)
    - 15
  * - CMD
    - MOSI
    - 13
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
    - 12
  * - D1
    - 
    - 

Para la prueba, utilizaremos un ESP32 WROM-32E y una tarjeta SanDisk Micros Ultra con una capacidad de 32 GB.

.. code-block:: python

  import machine
  import os
  from dualmcu import *

  # Inicializa la interfaz SPI para la tarjeta SD
  spi = machine.SPI(2, baudrate=1000000, polarity=0, phase=0, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12))

  # Inicializa la tarjeta SD
  sd = SDCard(spi, machine.Pin(15))

  # Monta el sistema de archivos
  vfs = os.VfsFat(sd)
  os.mount(vfs, "/sd")

  # Lista los archivos en la raíz de la tarjeta SD
  print("Archivos en la raíz de la tarjeta SD:")
  print(os.listdir("/sd"))

  os.umount("/sd") 

SDIO (Interfaz de Entrada/Salida Segura Digital)
------------------------------------------------

SDIO (Secure Digital Input/Output) es una interfaz de comunicación de alta velocidad que permite la transferencia de datos entre un microcontrolador y una tarjeta SD. La placa de desarrollo DualMCU ONE ofrece soporte para la interfaz SDIO, lo que te permite leer y escribir datos en una tarjeta SD de forma rápida y eficiente. 

La interfaz SDIO es una interfaz de comunicación de alta velocidad que permite la transferencia de datos entre un microcontrolador y una tarjeta SD. La placa de desarrollo DualMCU ONE ofrece soporte para la interfaz SDIO, lo que te permite leer y escribir datos en una tarjeta SD de forma rápida y eficiente. 



.. _figura-micro-sd-card:

.. figure:: /_static/Micro-SD-Card-Pinout.png
  :align: center
  :alt: Pinout de la Micro SD
  :width: 40%

  Pinout de la Micro SD


Esta tabla detalla las conexiones entre la tarjeta SD y el microcontrolador ESP32.

.. list-table:: Conexiones SDIO
  :header-rows: 1
  :widths: 25 25 25 25
  :align: center

  * - Nombre del Pin
    - Pines Correspondientes en Modo SPI
    - Número GPIO (Slot 1)
    - Número GPIO (Slot 2)
  * - CLK
    - SCLK
    - 6
    - 14
  * - CMD
    - MOSI
    - 11
    - 15
  * - DAT0
    - MISO
    - 7
    - 2
  * - DAT1
    - Interrupción
    - 8
    - 4
  * - DAT2
    - Sin Conexión (pullup)
    - 9
    - 12
  * - DAT3
    - CS
    - 10
    - 13

Ejemplo de aplicación
~~~~~~~~~~~~~~~~~~~~~~


.. _figura-micro-sd-card-reader:

.. figure:: /_static/dualmcu/output_serial.png
  :align: center
  :alt: Lector de Micro SD
  :width: 90%

  Lector de Micro SD

.. code-block:: cpp

  /* Sketch for testing the ESP32 HSPI interface on the DualMCU ONE.
   * Connect the SD card to the following pins:
   *
   * SD Card | ESP32
   *    D2       12
   *    D3       13
   *    CMD      15
   *    VSS      GND
   *    VDD      3.3V
   *    CLK      14
   *    VSS      GND
   *    D0       2  (add 1K pull up after flashing)
   *    D1       4
   */

  #include "FS.h"
  #include "SD_MMC.h"

  void listDir(fs::FS &fs, const char * dirname, uint8_t levels){
      Serial.printf("Listing directory: %s\n", dirname);

      File root = fs.open(dirname);
      if(!root){
          Serial.println("Failed to open directory");
          return;
      }
      if(!root.isDirectory()){
          Serial.println("Not a directory");
          return;
      }

      File file = root.openNextFile();
      while(file){
          if(file.isDirectory()){
              Serial.print("  DIR : ");
              Serial.println(file.name());
              if(levels){
                  listDir(fs, file.path(), levels -1);
              }
          } else {
              Serial.print("  FILE: ");
              Serial.print(file.name());
              Serial.print("  SIZE: ");
              Serial.println(file.size());
          }
          file = root.openNextFile();
      }
  }

  void createDir(fs::FS &fs, const char * path){
      Serial.printf("Creating Dir: %s\n", path);
      if(fs.mkdir(path)){
          Serial.println("Dir created");
      } else {
          Serial.println("mkdir failed");
      }
  }

  void removeDir(fs::FS &fs, const char * path){
      Serial.printf("Removing Dir: %s\n", path);
      if(fs.rmdir(path)){
          Serial.println("Dir removed");
      } else {
          Serial.println("rmdir failed");
      }
  }

  void readFile(fs::FS &fs, const char * path){
      Serial.printf("Reading file: %s\n", path);

      File file = fs.open(path);
      if(!file){
          Serial.println("Failed to open file for reading");
          return;
      }

      Serial.print("Read from file: ");
      while(file.available()){
          Serial.write(file.read());
      }
  }

  void writeFile(fs::FS &fs, const char * path, const char * message){
      Serial.printf("Writing file: %s\n", path);

      File file = fs.open(path, FILE_WRITE);
      if(!file){
          Serial.println("Failed to open file for writing");
          return;
      }
      if(file.print(message)){
          Serial.println("File written");
      } else {
          Serial.println("Write failed");
      }
  }

  void appendFile(fs::FS &fs, const char * path, const char * message){
      Serial.printf("Appending to file: %s\n", path);

      File file = fs.open(path, FILE_APPEND);
      if(!file){
          Serial.println("Failed to open file for appending");
          return;
      }
      if(file.print(message)){
          Serial.println("Message appended");
      } else {
          Serial.println("Append failed");
      }
  }

  void renameFile(fs::FS &fs, const char * path1, const char * path2){
      Serial.printf("Renaming file %s to %s\n", path1, path2);
      if (fs.rename(path1, path2)) {
          Serial.println("File renamed");
      } else {
          Serial.println("Rename failed");
      }
  }

  void deleteFile(fs::FS &fs, const char * path){
      Serial.printf("Deleting file: %s\n", path);
      if(fs.remove(path)){
          Serial.println("File deleted");
      } else {
          Serial.println("Delete failed");
      }
  }

  void testFileIO(fs::FS &fs, const char * path){
      File file = fs.open(path);
      static uint8_t buf[512];
      size_t len = 0;
      uint32_t start = millis();
      uint32_t end = start;
      if(file){
          len = file.size();
          size_t flen = len;
          start = millis();
          while(len){
              size_t toRead = len;
              if(toRead > 512){
                  toRead = 512;
              }
              file.read(buf, toRead);
              len -= toRead;
          }
          end = millis() - start;
          Serial.printf("%u bytes read for %u ms\n", flen, end);
          file.close();
      } else {
          Serial.println("Failed to open file for reading");
      }


      file = fs.open(path, FILE_WRITE);
      if(!file){
          Serial.println("Failed to open file for writing");
          return;
      }

      size_t i;
      start = millis();
      for(i=0; i<2048; i++){
          file.write(buf, 512);
      }
      end = millis() - start;
      Serial.printf("%u bytes written for %u ms\n", 2048 * 512, end);
      file.close();
  }

  void setup(){
      Serial.begin(115200);
      if(!SD_MMC.begin()){
          Serial.println("Card Mount Failed");
          return;
      }
      uint8_t cardType = SD_MMC.cardType();

      if(cardType == CARD_NONE){
          Serial.println("No SD_MMC card attached");
          return;
      }

      Serial.print("SD_MMC Card Type: ");
      if(cardType == CARD_MMC){
          Serial.println("MMC");
      } else if(cardType == CARD_SD){
          Serial.println("SDSC");
      } else if(cardType == CARD_SDHC){
          Serial.println("SDHC");
      } else {
          Serial.println("UNKNOWN");
      }

      uint64_t cardSize = SD_MMC.cardSize() / (1024 * 1024);
      Serial.printf("SD_MMC Card Size: %lluMB\n", cardSize);

      listDir(SD_MMC, "/", 0);
      createDir(SD_MMC, "/mydir");
      listDir(SD_MMC, "/", 0);
      removeDir(SD_MMC, "/mydir");
      listDir(SD_MMC, "/", 2);
      writeFile(SD_MMC, "/hello.txt", "Hello ");
      appendFile(SD_MMC, "/hello.txt", "World!\n");
      readFile(SD_MMC, "/hello.txt");
      deleteFile(SD_MMC, "/foo.txt");
      renameFile(SD_MMC, "/hello.txt", "/foo.txt");
      readFile(SD_MMC, "/foo.txt");
      testFileIO(SD_MMC, "/test.txt");
      Serial.printf("Total space: %lluMB\n", SD_MMC.totalBytes() / (1024 * 1024));
      Serial.printf("Used space: %lluMB\n", SD_MMC.usedBytes() / (1024 * 1024));
  }

  void loop(){

}


