# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import atexit
from rpi_ws281x import Color, PixelStrip, ws

# LED strip configuration:
LED_BRIGHTNESS = 5
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

def colorWipe(strip, color, wait_ms=5):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(((i * 256 // strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)

def onExit(strips):
    for strip in strips:
        colourSet(strip, CLEAR)  # White wipe

def initLeds(strips):
    for strip in strips:
        # colourSet(strip, RED)
        print("set!")
        transFlagChase(strip)
    time.sleep(2)
    colourSetStrips(strips, TRANS_BLUE)
    time.sleep(2)
    colourSetStrips(strips, TRANS_PINK)
    time.sleep(2)
    colourSetStrips(strips, WHITE)
    time.sleep(2)
    colourSetStrips(strips, RED)
    time.sleep(2)
    colourSetStrips(strips, RED)
    time.sleep(2)

    # Color wipe animations.
    # colorWipe(strip, Color(255, 0, 0))  # Red wipe
    # colorWipe(strip, Color(0, 255, 0))  # Blue wipe
    # colorWipe(strip, Color(0, 0, 255))  # Green wipe
    # colorWipe(strip, Color(0, 0, 0, 255))  # White wipe
    # colorWipe(strip, Color(255, 255, 255))  # Composite White wipe
    # colorWipe(strip, Color(255, 255, 255, 255))  # Composite White + White LED wipe
    # # Theater chase animations.
    # theaterChase(strip, Color(127, 0, 0))  # Red theater chase
    # theaterChase(strip, Color(0, 127, 0))  # Green theater chase
    # theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
    # theaterChase(strip, Color(0, 0, 0, 127))  # White theater chase
    # theaterChase(strip, Color(127, 127, 127, 0))  # Composite White theater chase
    # theaterChase(strip, Color(127, 127, 127, 127))  # Composite White + White theater chase
    # # Rainbow animations.
    # rainbow(strip)
    # rainbowCycle(strip)
    # theaterChaseRainbow(strip)

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
