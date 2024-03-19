# Step Counter

## Introduction @unplugged

![A @boardname@ attached on a foot](/static/mb/projects/step-counter.png)

Du willst wissen wie viele Schritte du am Tag zurücklegst?

Dann ist dieses Tutorial genau richtig für dich!
Hier lernst du wie du einen Schrittzähler, auch Pedometer genannt, programmieren kannst.

## A counter
Um deine Schritte zu zählen, musst du dir irgendwo merken wie viele Schritte du schon zurückgelegt hast. Das kannst du mit Hilfe von einer Variable ``||variables:Anzahl_Schritte||`` speichern. Achtung: beim Start soll ``||variables:Anzahl_Schritte||`` bei 0 Schritte starten. 

```blocks
let Anzahl_Schritte = 0
```

## Schritt zählen
Immer wenn du einen Schritt machst, wird dein Micro:bit geschüttelt. Verwende ``||input:geschüttelt||`` um deine Variable ``||variables:Anzahl_Schritte||`` um 1 zu erhöhen.

```blocks
let Anzahl_Schritte = 0
input.onGesture(Gesture.Shake, function () {
    Anzahl_Schritte += 1
})
```

## Wie viele Schritte hast du gemacht
Du möchtest dauerhaft deine Anzahl an Schritte am Bildschirm sehen. Deshalb brauchst du den Baustein ``||basic:dauerhaft||``, um die Variable ``||variables:Anzahl_Schritte||`` mit Hilfe von ``||basic:zeige Zahl||`` anzuzeigen.

```blocks
basic.forever(function() {
    basic.showNumber(Anzahl_Schritte)
})
```



## Lösche deine Schritte
Du möchtest wieder anfangen deine Schritte neu zu zählen. Setze den Wert deiner gespeicherten Variable ``||variables:Anzahl_Schritte||`` ``||input:wenn Knopf A gedrückt||`` zurück. Achtung: Auf welchen Wert musst du die Variable ``||variables:Anzahl_Schritte||`` setzen?

```blocks
input.onButtonPressed(Button.B, function () {
    Anzahl_Schritte = 0
})
```

## Zeige die Anzahl deiner Schritte beim Druck auf Knopf B
Um Strom zu sparen möchtest du den Bildschirm für 5 Sekunden ausschalten. Das bedeutet ``||input:wenn Knopf B gedrückt||``, wird ``||basic:Bildschirminhalt löschen||`` aufgerufen und für 5 Sekunden ``||basic:pausieren (ms)||``.

```blocks
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.pause(5000)
})
```



## überprüfen ob du mehr wie 20 Schritte zurückgelegt hast
### Für die Profis:
Du möchtest überprüfen, ob du mehr wie 20 Schritte zurückgelegt hast, ``||input:wenn Knopf A+B gedrückt||`` wurde.
``||logic:Wenn __________ dann||`` deine Variable ``||variables:Anzahl_Schritte||`` größer oder gleich (>=) 20 ist, soll ein glücklicher Smiley mit Hilfe von ``||basic:zeige LEDs||`` am Display ausgegeben werden. Male dir deinen Smiley in dem du die LEDs die leuchten sollen markierst. Ansonsten (weniger wie 20 Schritte), soll ein trauriger Smiley mit Hilfe von ``||basic:zeige LEDs||`` angezeigt werden.

```blocks
input.onButtonPressed(Button.AB, function () {
    if (Anzahl_Schritte >= 20) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    }
})
```


## Run!
### Auf die Plätze - fertig - los!
Dein Schrittzähler ist nun fertig. Probiere ihn gleich aus.

<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
