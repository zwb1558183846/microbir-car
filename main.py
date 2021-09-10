cbit_小车类.car_ctrl_speed(cbit_小车类.CarState.CAR_STOP, 0)

def on_forever():
    if cbit_传感器类.IR_Sensor(DigitalPin.P4, cbit_传感器类.enIR.NO_GET) and cbit_传感器类.IR_Sensor(DigitalPin.P5, cbit_传感器类.enIR.NO_GET):
        cbit_小车类.car_ctrl_speed(cbit_小车类.CarState.CAR_STOP, 0)
    if cbit_传感器类.IR_Sensor(DigitalPin.P4, cbit_传感器类.enIR.GET) and cbit_传感器类.IR_Sensor(DigitalPin.P5, cbit_传感器类.enIR.GET):
        cbit_小车类.car_ctrl_speed(cbit_小车类.CarState.CAR_RUN, 150)
basic.forever(on_forever)
