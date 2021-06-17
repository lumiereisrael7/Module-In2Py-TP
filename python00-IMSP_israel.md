 <center style= "color: green">Doing calculation</center>

 <li> Considerons les expressions suivantes</li>


```python
width = 17
height = 12.0
delimiter = '.'
```


```python
width/2

type(width/2) is float

#Le type est un float. la valeur vaut 8.5
```




    True




```python
width/2.0

type(width/2.0) is float

#la valeur vaut 8.5 et le type est un float
```




    8.5




```python
height/3

type(height/3) is float
#La valeur vaut 4.0 et le type est un float
```




    4.0




```python
1 + 2 * 5

type(1 + 2 * 5) is int

#La valeur vaut 11 et le type est un int
```




    True




```python
delimiter * 5

type(delimiter * 5) is str
# Je voulais dire que nous aurons une erreur puisque delimiter contient une chaine de caractere et on voudrait le multiplier par 5
# Mais le résultat obtenue montre qu'on souhaite repeter 5 fois la chaine à l'intérieur de la variable delimiter.
# Donc la valeur est: .....
# Le type est un str
```




    True



<li>Utilisation de l'interpreter Python comme calculatrice</li>


```python
PI = 3.1415926535897931

r = 5

V = (3/4) * PI * (r**3)

print(V)
```

    294.5243112740431


 <center style= "color: green">Data type and operations</center>

<li>Type des variables</li>


```python
x = 1

y = float(5)

z = "ten"

type(x) is int

type(y) is float

type(z) is str
```




    True



<li>L'operation "+"</li>


```python
print(x + x)

print(x + y)

print(y + y)

print(y + z)

print(z + z)
```

    2
    6.0
    10.0
    tenten


Nous aurons une erreur au niveau de l'operation : <b>float-str</b> <br> Aucune autre surprise

<li>L'operation "*"</li>


```python
print(x * x) 

print(x * y)

print(y * y)

#print(y * z)

#print(z * z)
```

    1
    5.0
    25.0


Les lignes commentées génèrent d'erreurs
Nous aurons d'erreurs au niveau de l'operation : <b>float-str et str-str</b> <br> Aucune autre surprise

<li>L'operation "-"</li>


```python
print(x - x)

print(x - y)

print(y - y)

#print(y - z)

#print(z - z)
```

    0
    -4.0
    0.0


Les lignes commentées génèrent d'erreurs
Nous aurons d'erreurs au niveau de l'operation : <b>float-str et str-str</b> <br> Aucune autre surprise

<li>L'operation "/"</li>


```python
print(x / x)

print(x / y)

print(y / y)

#print(y / z)

#print(z / z)
```

    1.0
    0.2
    1.0


Les lignes commentées génèrent d'erreurs
Nous aurons d'erreurs au niveau de l'operation : <b>float-str et str-str</b> <br> Aucune autre surprise

<li>L'operation "%"</li>


```python
print(x % x)

print(x % y)

print(y % y)

#print(y % z)

#print(z % z)
```

    0
    1.0
    0.0


Les lignes commentées génèrent d'erreurs
Nous aurons d'erreurs au niveau de l'operation : <b>float-str et str-str</b> <br> Aucune autre surprise

<li>Les operations <pre> "<", ">", "<=", ">=" "=="</pre></li>


```python
print(x <= x)

print(x < y)

print(y > y)

print(y == z)

print(z > z)
```

    True
    True
    False
    False
    False


Ce sont des operateurs logiques. Donc renvoies un <b>booleen</b>.

La surprise est qu'aucune des lignes ne présentent d'erreur pour les operations. Pour toutes les operations il n'y a pas d'erreurs sur les lignes.


```python
help(int)

help(float)
```
