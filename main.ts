let Anzahl_Schritte = 0
input.onGesture(Gesture.Shake, function () {
    Anzahl_Schritte += 1
})
basic.forever(function () {
    Anzahl_Schritte = 0
})
