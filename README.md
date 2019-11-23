# MAX7219 8x8 LED Matrix Library
This library provides support for the MAX7219 8x8 LED matrix on ESP8266 with MicroPython. It uses framebuf internally to provide drawing primitives and text support (including scrolling marquee). You can chain several matrices any way you like: if you use two 4x 8x8 matrices, you can have one of the left, and the other on the right giving you a 64x8 area, or have one on top of the other to have a 32x16 display!

The library has only been tested on an ESP8266 but may work on other systems.

This library is a mashup of several others in an attempt to compile a single MAX7219 driver with comprehensive functionality.   See Credits below.

###Connecting on ESP8266

ESP8266 | MAX7219
--- | ---
5V | VCC
GND | GND
D7 (GPIO13) | DIN
D8 (GPIO15) | CS
D5 (GPIO14) | CLK

##Examples
Using 10000000 as baudrate is recommended as greater values don't seem to work well...

####Single 8x8 matrix

from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(8, 8, spi, Pin(15))
screen.text('A', 0, 0, 1)
screen.show()

####Single 4x 8x8 matrix
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(32, 8, spi, Pin(15))
screen.text('ABCD', 0, 0, 1)
screen.show()

###Two 4x 8x8 matrices (left/right)
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(64, 8, spi, Pin(15))
screen.text('ABCDEFGH', 0, 0, 1)
screen.show()

###Two 4x 8x8 matrices (top/bottom)
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(32, 16, spi, Pin(15))
screen.text('ABCD', 0, 0, 1)
screen.text('EFGH', 0, 8, 1)
screen.show()

##Credits
This library is based on:
* (Vincent Rialland) https://github.com/vrialland/micropython-max7219
* (Mike Causer) https://github.com/mcauser/micropython-max7219
* (joewez) https://github.com/joewez/WifiMarquee

Thank you for sharing your code!