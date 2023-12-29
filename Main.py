import autopy

def findduck(startArea):
    screen = autopy.bitmap.capture_screen()
    position = screen.find_color((255,119,99),0.03,((startArea[0],startArea[1]),(800,400)))
    if position:
        #print("Found duck at %s" % str(pos))
        autopy.mouse.move(position[0]+20, position[1])
        autopy.mouse.click()

def findGameArea():
    for i in range(1000):
        screen = autopy.bitmap.capture_screen()
        position = screen.find_color((255,119,99),0.03)
        if position:
            print("Game Area: " + str(position))
            return position
        exit()

startArea = findGameArea()
 for i in range(1000):
    findduck(startArea)