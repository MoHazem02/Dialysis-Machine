from serial import *
from PyQt5 import QtCore

class ApplicationManager:
    def __init__(self,UI):
        self.ui = UI
        self.serial_port = Serial('COM4', 9600)
        self.desired_flow = 600
        self.start()
        
    def start(self):
        self.ui.DesiredBloodFlowRate.display(self.desired_flow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(500) 

    def read_data(self):
        arduino_data = self.serial_port.readline().decode('utf-8').strip()
        print(arduino_data)
        if len(arduino_data) > 9:
            return
        if arduino_data:
            cond, flow = arduino_data.split(',')
            if flow == '0.00':
                flow = 0
            else:
                flow *= 1000
            self.ui.BloodFlowRate.display(flow)
            self.ui.Conductivity.display(int(cond))
                
    
    def increment_flow(self):
        self.desired_flow += 50
        self.ui.DesiredBloodFlowRate.display(self.desired_flow)

    def decrement_flow(self):
        self.desired_flow -= 50
        self.ui.DesiredBloodFlowRate.display(self.desired_flow)