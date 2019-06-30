import pyautogui as gui
import keyboard
import time
import math

# Helper function to get value of pixel in image
def getPixel(Image,x, y):
    px = Image.load()
    return px[x, y]


# Screen Dimensions
top, left, width, height = 293, 0, 1920, 465
screenDimensions = {
    "top": top,
    "left": left,
    "width": width,
    "height": height
}

# helper variables to calculate time
last = 0
total_time = 0

# the intervals where the bot will search for obstacles
y_search, x_start, x_end = 350, 435, 450
y_search2 = 275 # for the birds


time.sleep(1)
while True:
    t1 = time.time()
    if keyboard.is_pressed('q'): # Emergency Button
        break

    # increase the search width every second to simulate the dino acceleration
    if math.floor(total_time) != last:
        x_end += 4
        if x_end >= width:
            x_end = width
        last = math.floor(total_time)

    # a way to get a screen shot but it was too slow
    # sct_img = sct.grab(screenDimensions)
    # mss.tools.to_png(sct_img.rgb, sct_img.size, output="test.png")

    # Get a screen shot
    sct_img = gui.screenshot(region=(left,top, width, height))

    # Get the color of the world background
    bgColor = getPixel(sct_img, 440, 30)

    for i in reversed(range(x_start, x_end)):
        # if i found a pixel in the search interval with a colour other than the bg colour, then it is an obstacle
        if getPixel(sct_img,i,y_search) != bgColor\
                or getPixel(sct_img,i,y_search2) != bgColor:
            keyboard.press(' ') # jump
            break

    t2 = time.time()-t1
    total_time += t2

    # DEBUG
    print(x_end)

