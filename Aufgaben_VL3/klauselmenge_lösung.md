![Aufgabe](https://github.com/KingMus/ws-aufgaben/blob/master/Aufgaben_VL3/src-bilder/Aufgabe_Klauselmenge.png)

##### Lösung:

1)
> a v (b ^ c) <br>
> (a v b) ^ (a v c) <br>

2)
> a <-> (b ^ c) <br>
> (a ^ (b ^ c)) v (!a ^ !(b ^ c)) <br>
> (a ^ (b ^ c)) v (!a ^ (!b v !c)) <br>
> (a ^ b ^ c) v ((!a ^ !b) v (!a ^ !c)) <br>
> (a ^ b ^ c) v (!a v (!b ^ !c)) <br>

3)
> (!a ^ (!b -> c)) -> d <br>
> (!a ^ (b v c)) -> d <br>
> !(!a ^ (b v c)) v d <br>
> a v !(b v c)) v d <br>
> a v (!b ^ !c) v d <br>
