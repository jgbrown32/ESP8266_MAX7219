# MAX7219 8x8 LED Matrix Library
This library provides support for the MAX7219 8x8 LED matrix on ESP8266 with MicroPython. It uses framebuf internally to provide drawing primitives and text support (including scrolling marquee). You can chain several matrices any way you like: if you use two 4x 8x8 matrices, you can have one of the left, and the other on the right giving you a 64x8 pixel area, or have one on top of the other to have a 32x16 pixel display!

This library is a mashup of several others in an attempt to compile a single MAX7219 driver with comprehensive functionality.   See Credits below.

## Syntax

#### Methods
* show() : Writes bytearray buffer to display.
* brightness(*value*) : Set brightness level for display. Value is an integer from 0 to 15.
* marquee(*msg*) : Scroll *msg* string across the display, from right to left.
* *framebuf* methods: https://docs.micropython.org/en/latest/library/framebuf.html

#### Example
```
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
# display = max7219.Max7219(width, height, spi, cs, rotate)
  # width = total width of display in pixels
  # height = total height of display in pixels
  # spi = SPI bus
  # cs = cs (Chip Select) pin on ESP8266
  # rotate = rotate display 180 degrees (Optional; default = True) 
display = max7219.Max7219(8, 8, spi, Pin(15))
display.text('A', 0, 0)
display.show()

# display.marquee(msg_to_display)
display.marquee("This is my message")
```

#### Use Notes
* The ESP8266 SPI bus seems to work best with a baud rate of 10000000.
* Some 8x8 matrix displays (specifically the chained 4x displays) are rotated 180 degrees when connected.  Use the rotate parameter (True or False) to address your specific display. 
* See MicroPython documentation of *framebuf* for additional supported methods (https://docs.micropython.org/en/latest/library/framebuf.html).
* This library has only been tested on an ESP8266 but may work on other systems.

## Connecting to ESP8266

 ESP8266 | MAX7219
 --- | ---
 5V | VCC
 GND | GND
 D7 (GPIO13) | DIN
 D8 (GPIO15) | CS
 D5 (GPIO14) | CLK

## Examples

#### Single 8x8 matrix
```
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(8, 8, spi, Pin(15))
screen.text('A', 0, 0, 1)
screen.show()
```

#### Single 4x 8x8 matrix
```
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(32, 8, spi, Pin(15))
screen.text('ABCD', 0, 0, 1)
screen.show()
```

#### Two 4x 8x8 matrices (left/right)
```
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(64, 8, spi, Pin(15))
screen.text('ABCDEFGH', 0, 0, 1)
screen.show()
```

#### Two 4x 8x8 matrices (top/bottom)
```
from machine import Pin, SPI
import max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(32, 16, spi, Pin(15))
screen.text('ABCD', 0, 0, 1)
screen.text('EFGH', 0, 8, 1)
screen.show()
```
## Credits
This library is based on:
* Vincent Rialland : https://github.com/vrialland/micropython-max7219
* Mike Causer : https://github.com/mcauser/micropython-max7219
* joewez : https://github.com/joewez/WifiMarquee

Thank you for sharing your code!
