input.onButtonPressed(Button.A, function () {
    koi2.classifyImageAddTagID("left")
})
input.onButtonPressed(Button.AB, function () {
    koi2.classifyImageSave(koi2.Location.Flash, "model.json")
})
input.onButtonPressed(Button.B, function () {
    koi2.classifyImageAddTagID("right")
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    koi2.classifyImageLoad(koi2.Location.Flash, "model.json")
    if (koi2.classifyImageGetClass() == "right") {
        robotbit.Servo(robotbit.Servos.S1, 0)
        turnleft = true
    } else if (koi2.classifyImageGetClass() == "left") {
        robotbit.Servo(robotbit.Servos.S1, 175)
        turnright = true
    }
})
let direction = 0
let turnright = false
let turnleft = false
koi2.koi2Init(SerialPin.P2, SerialPin.P12)
koi2.switchFunction(koi2.FullFunction.ClassifyImage, koi2.IOTSwitch.OFF)
turnleft = false
turnright = false
basic.forever(function () {
    direction = sonar.ping(
    DigitalPin.P15,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    while (turnright) {
        basic.showNumber(direction)
        robotbit.MotorRun(robotbit.Motors.M1A, 0)
        if (direction < 15) {
            robotbit.MotorRun(robotbit.Motors.M1A, 0)
        } else if (direction < 10) {
            robotbit.Servo(robotbit.Servos.S1, 0)
        } else {
            robotbit.Servo(robotbit.Servos.S1, 160)
        }
    }
    while (turnleft) {
        robotbit.MotorRun(robotbit.Motors.M1A, 0)
        if (direction < 15) {
            robotbit.MotorRun(robotbit.Motors.M1A, 0)
        } else if (direction < 10) {
            robotbit.Servo(robotbit.Servos.S1, 175)
        } else {
            robotbit.Servo(robotbit.Servos.S1, 160)
        }
    }
})
