# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import atexit
from rpi_ws281x import Color, PixelStrip, ws

# LED strip configuration:
LED_BRIGHTNESS = 2
LED_STRIP = ws.SK6812_STRIP
LED_FREQUENCY_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_MONITOR_DIRECT_MEMORY_ACCESS = 10
LED_INVERT_SIGNAL = False

LED_MONITOR_COUNT = 212        # Number of LED pixels.
LED_MONITOR_PIN = 12           # GPIO pin connected to the pixels (must support PWM!).
LED_MONITOR_CHANNEL = 0

LED_COASTER_COUNT = 182        # Number of LED pixels.
LED_COASTER_PIN = 13           # GPIO pin connected to the pixels (must support PWM!).
LED_COASTER_CHANNEL = 1

SLEEP_TIME = 10

PURPLE = Color(147,112,219)
RED = Color(255, 0, 0)
CLEAR = Color(0, 0, 0, 255)
WHITE = Color(255, 255, 255)

TRANS_BLUE = Color(91, 206, 250)
TRANS_PINK = Color(245, 169, 184)

def transFlagChase(strip, wait_ms=10):
    for i in range(strip.numPixels()):
        blue = [0,1,8,9]
        pink = [2,3,6,7]
        transFlagLooped(strip, blue, pink, 0)
        blue = [4,5,6,7]
        pink = [2,3,8,9]
        transFlagLooped(strip, blue, pink, strip.numPixels()/2)
    strip.show()
    time.sleep(wait_ms / 100.0)

def transFlagLooped(strip, blue, pink, led_offset):
    for i in range(int(strip.numPixels()/2)):
        led_to_change = int(i+led_offset)
        last_digit = int(repr(led_to_change)[-1])
        if(last_digit in blue):
            strip.setPixelColor(led_to_change, TRANS_BLUE)
        elif(last_digit in pink):
            strip.setPixelColor(led_to_change, TRANS_PINK)
        else:
            strip.setPixelColor(led_to_change, WHITE)

def colourSet(strip, color, wait_ms=100):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
    time.sleep(wait_ms / 1000.0)

def colourSetStrips(strips, color, wait_ms=100):
    for strip in strips:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()
    time.sleep(wait_ms / 1000.0)

def onExit(strips):
    for strip in strips:
        colourSet(strip, CLEAR)  # White wipe

def initLeds(strips):
    for strip in strips:
        # colourSet(strip, RED)
        print("set!")
        transFlagChase(strip)
    time.sleep(SLEEP_TIME)
    colourSetStrips(strips, TRANS_BLUE)
    time.sleep(SLEEP_TIME)
    colourSetStrips(strips, TRANS_PINK)
    time.sleep(SLEEP_TIME)
    colourSetStrips(strips, WHITE)
    time.sleep(SLEEP_TIME)

# Main program logic follows:
if __name__ == '__main__':
    monitorStrip = PixelStrip(LED_MONITOR_COUNT, LED_MONITOR_PIN, LED_FREQUENCY_HZ, LED_MONITOR_DIRECT_MEMORY_ACCESS, LED_INVERT_SIGNAL, LED_BRIGHTNESS, LED_MONITOR_CHANNEL, LED_STRIP)
    coasterStrip = PixelStrip(LED_COASTER_COUNT, LED_COASTER_PIN, LED_FREQUENCY_HZ, LED_MONITOR_DIRECT_MEMORY_ACCESS, LED_INVERT_SIGNAL, LED_BRIGHTNESS, LED_COASTER_CHANNEL, LED_STRIP)
    monitorStrip.begin()
    coasterStrip.begin()
    strips = [monitorStrip, coasterStrip]
    atexit.register(onExit, strips)

    print('Press Ctrl-C to quit.')
    while True:
        initLeds(strips)
