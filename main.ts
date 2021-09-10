// 前进
function go_ahead () {
    cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Run, 150)
}
input.onButtonPressed(Button.A, function () {
    while (true) {
        距离 = cbit_传感器类.Ultrasonic(DigitalPin.P1, DigitalPin.P2)
        if (距离 < 15) {
            turn_left()
        } else {
            go_ahead()
        }
    }
})
// 左转
function turn_left () {
    cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_SpinLeft, 150)
}
let 距离 = 0
cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Stop, 0)
距离 = 0
