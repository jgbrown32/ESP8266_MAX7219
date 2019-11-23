from machine import Pin, SPI
import max7219, utime

spi = SPI(1, 10000000)
d = max7219.Max7219(32, 8, spi, Pin(15), False)
d.text("12:12", 0, 0)

d.show()
utime.sleep(10)

max7219.scroll_message(d, "Now is the time for all good men...")
