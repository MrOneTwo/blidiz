import rtmidi
from pynput.keyboard import Key
from pynput.mouse import Button
import pynput
import time
from pathlib import Path

# 36 - 51

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

knob_position = 0
knob_previous = knob_position

BUTTON_TO_BUTTON_ID = {
    "A1": 36,
    "A2": 37,
    "A3": 38,
    "A4": 39,
    "B1": 40,
    "B2": 41,
    "B3": 42,
    "B4": 43,
    "C1": 44,
    "C2": 45,
    "C3": 46,
    "C4": 47,
    "D1": 48,
    "D2": 49,
    "D3": 50,
    "D4": 51,
}

cmd = "echo test"

ATOM_NAME = "ATOM"
EXPORT_PATH = Path(r"C:\Users\mc\Desktop\crouching_girl")

midiin = rtmidi.RtMidiIn()

ports = range(midiin.getPortCount())

if ports:
    for i in ports:
        port_name = midiin.getPortName(i)
        print(f"Port name {i}: {port_name}")
        if ATOM_NAME in midiin.getPortName(i):
            print(f"Opening port {i}: " + midiin.getPortName(i))
            m = midiin.openPort(i)
            break

def exportMeshZbrush(filename: str):
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.alt):
            keyboard.press("p")
            keyboard.release("p")
    time.sleep(0.02)
    with keyboard.pressed(Key.ctrl):
        keyboard.press("l")
        keyboard.release("l")
    time.sleep(0.02)
    keyboard.type(str(EXPORT_PATH))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(filename)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    with keyboard.pressed(Key.alt):
        keyboard.press("y")
        keyboard.release("y")


while True:
    m = midiin.getMessage(250)
    if m:
        if m.isNoteOn():
            # print('On', m.getMidiNoteName(m.getNoteNumber()), m.getVelocity())
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A1"]:
                exportMeshZbrush("export_1")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A2"]:
                exportMeshZbrush("export_2")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A3"]:
                exportMeshZbrush("export_3")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A4"]:
                exportMeshZbrush("export_4")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B1"]:
                keyboard.press("s")
                keyboard.release("s")
                time.sleep(0.02)
                mouse.press(Button.left)
                time.sleep(0.05)
                mouse.move(2, 0)
                time.sleep(0.05)
                mouse.release(Button.left)
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B3"]:
                keyboard.press("b")
                keyboard.release("b")
                time.sleep(0.02)
                keyboard.press("c")
                keyboard.release("c")
                time.sleep(0.02)
                keyboard.press("b")
                keyboard.release("b")
                time.sleep(0.02)
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B2"]:
                pass
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B4"]:
                pass
        elif m.isNoteOff():
            print("OFF", m.getMidiNoteName(m.getNoteNumber()))
        elif m.isController():
            print("CONTROLLER", m.getControllerNumber(), m.getControllerValue())
            if m.getNoteNumber() == 14:
                knob_position = m.getControllerValue()
                knob_rotation = knob_position - knob_previous

                cursor_movement = knob_rotation

                if cursor_movement == 0:
                    cursor_movement = 2

                keyboard.press("s")
                keyboard.release("s")
                time.sleep(0.02)
                mouse.press(Button.left)
                time.sleep(0.02)
                mouse.move(cursor_movement, 0)
                time.sleep(0.02)
                mouse.release(Button.left)

                knob_previous = knob_position
        else:
            print("?", m)