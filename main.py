Anzahl_Schritte = 0

def on_gesture_shake():
    global Anzahl_Schritte
    Anzahl_Schritte += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global Anzahl_Schritte
    Anzahl_Schritte = 0
basic.forever(on_forever)
