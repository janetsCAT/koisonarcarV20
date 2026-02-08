def on_button_pressed_a():
    koi2.classify_image_add_tag_id("left")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    koi2.classify_image_save(koi2.Location.FLASH, "model.json")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    koi2.classify_image_add_tag_id("right")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global detect, _class
    koi2.classify_image_load(koi2.Location.FLASH, "model.json")
    detect = not (detect)
    _class = koi2.classify_image_get_class()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

direction = 0
_class = ""
detect = False
koi2.koi2_init(SerialPin.P2, SerialPin.P12)
koi2.switch_function(koi2.FullFunction.CLASSIFY_IMAGE, koi2.IOTSwitch.OFF)
detect = False
turnleft = False
turnright = False

def on_forever():
    global turnright, turnleft
    while detect:
        if _class == "right":
            robotbit.servo(robotbit.Servos.S1, 250)
            turnright = not (turnright)
            break
        elif koi2.classify_image_get_class() == "left":
            robotbit.servo(robotbit.Servos.S1, 0)
            turnleft = not (turnleft)
            break
        else:
            # if the koi did not find the signal, it will turn back. Better to turn left/right again to find the signal.
            robotbit.motor_run(robotbit.Motors.M1A, 0)
basic.forever(on_forever)

def on_forever2():
    global direction
    direction = sonar.ping(DigitalPin.P15, DigitalPin.P14, PingUnit.CENTIMETERS)
    while turnleft:
        robotbit.motor_run(robotbit.Motors.M1A, 0)
        if direction < 15:
            robotbit.motor_run(robotbit.Motors.M1A, 0)
        if direction < 10:
            robotbit.servo(robotbit.Servos.S1, 250)
basic.forever(on_forever2)

def on_forever3():
    pass
basic.forever(on_forever3)
