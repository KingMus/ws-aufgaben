## Aufgabe 1
Entscheiden Sie, um was es sich handelt?

###### Abduktion

Alle Kater sind schwarz. <br>
Felix ist schwarz. <br>
Felix ist ein Kater. <br>

<hr>

## Aufgabe 2

Folgende Sachverhalte sind bekannt:

* Jens wacht auf
* Jens holt einen Wischlappen
* Wenn Jens aufwacht und sein Zimmer säubert freut sich Jens' Mutter
* Wenn Jens einen Wischlappen holt dann säubert er das Zimmer

Formulieren Sie die Aussagen in der Struktur, die in dieser 
Vorlesung eingeführt wurde:

##### Beobachtungen (Regeln)
> aufwachen(a) <br>
> a wacht auf <br>

> lappenHolen(a) <br>
> a holt einen Lappen <br>

> zimmerSäubern(a) <br>
> a säubert sein Zimmer <br>

> freuen(a) <br>
> a freut sich <br>

##### Hintergrundwissen (Relationen)
> E € aufwachen(a) & zimmerSäubern(a) --> freuen(b). <br>
> lappenHolen(a) --> zimmerSäubern(a). <br>

##### Ergebnis (Beispiel)
> aufwachen(Jens). <br>
> lappenHolen(Jens) --> zimmerSäubern(Jens) --> freuen(Mutter). <br>
