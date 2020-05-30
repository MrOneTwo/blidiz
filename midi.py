import rtmidi
from pynput.keyboard import Key
from pynput.mouse import Button
import pynput
import time
from pathlib import Path
import config


ATOM_NAME = "ATOM"
EXPORT_PATH = Path(config.CFG_EXPORT_PATH)

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

knob_position = 0
knob_previous = knob_position

BUTTON_TO_BUTTON_ID = {
    "A1_1": 36, "A1_2": 52,
    "A2_1": 37, "A2_2": 53,
    "A3_1": 38, "A3_2": 54,
    "A4_1": 39, "A4_2": 55,
    "B1_1": 40, "B1_2": 56,
    "B2_1": 41, "B2_2": 57,
    "B3_1": 42, "B3_2": 58,
    "B4_1": 43, "B4_2": 59,
    "C1_1": 44, "C1_2": 60,
    "C2_1": 45, "C2_2": 61,
    "C3_1": 46, "C3_2": 62,
    "C4_1": 47, "C4_2": 63,
    "D1_1": 48, "D1_2": 64,
    "D2_1": 49, "D2_2": 65,
    "D3_1": 50, "D3_2": 66,
    "D4_1": 51, "D4_2": 67
}

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

def setBrushZbrush(keys: list):
    for k in keys:
        keyboard.press(k)
        keyboard.release(k)
        time.sleep(0.02)


while True:
    m = midiin.getMessage(250)
    if m:
        if m.isNoteOn():
            print("ON", m.getNoteNumber(), m.getMidiNoteName(m.getNoteNumber()), m.getVelocity())
            # Layer 2.
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A1_2"]:
                exportMeshZbrush("export_1")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A2_2"]:
                exportMeshZbrush("export_2")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A3_2"]:
                exportMeshZbrush("export_3")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A4_2"]:
                exportMeshZbrush("export_4")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B1_2"]:
                exportMeshZbrush("export_5")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B2_2"]:
                exportMeshZbrush("export_6")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B3_2"]:
                exportMeshZbrush("export_7")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B4_2"]:
                exportMeshZbrush("export_8")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["C1_2"]:
                exportMeshZbrush("export_9")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["C2_2"]:
                exportMeshZbrush("export_10")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["C3_2"]:
                exportMeshZbrush("export_11")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["C4_2"]:
                exportMeshZbrush("export_12")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["D1_2"]:
                exportMeshZbrush("export_13")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["D2_2"]:
                exportMeshZbrush("export_14")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["D3_2"]:
                exportMeshZbrush("export_15")
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["D4_2"]:
                exportMeshZbrush("export_16")
            # Layer 1.
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["B1_1"]:
                keyboard.press("s")
                keyboard.release("s")
                time.sleep(0.02)
                mouse.press(Button.left)
                time.sleep(0.05)
                mouse.move(2, 0)
                time.sleep(0.05)
                mouse.release(Button.left)
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A1_1"]:
                setBrushZbrush(("b", "c", "b"))
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A2_1"]:
                setBrushZbrush(("b", "s", "m"))
            if m.getNoteNumber() == BUTTON_TO_BUTTON_ID["A3_1"]:
                setBrushZbrush(("b", "d"))
        elif m.isNoteOff():
            print("OFF", m.getNoteNumber(), m.getMidiNoteName(m.getNoteNumber()))
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
