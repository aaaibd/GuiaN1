txtorg = ("La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica.")
print(txtorg)
txtorg.lower()
texto = 'la universidad de los lagos es una institución estatal fundada en 1993. esta universidad regional entrega una contribución significativa al desarrollo sostenible del territorio. como universidad sus pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática.'

print(texto)
texto2 = texto.split()
uni = 'universidad'
prepetida = tuple([uni] * texto2.count(uni))
print(texto2.count(uni), "veces se repiten las palabras:", prepetida)