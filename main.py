from machine import Pin, SPI
import max7219, utime

spi = SPI(1, 10000000)
d = max7219.Max7219(32, 8, spi, Pin(15), False)
d.text("Jeff", 0, 0)

d.show()
utime.sleep(5)

d.marquee("Now is the time for all good men...")
