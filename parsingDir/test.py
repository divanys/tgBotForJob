import bdForJogDir.parsing as ps
import bdForJogDir.function as fn


dataProduct = [
(ps.keysALl[0], ps.infoAll[ps.keysALl[0]]['Название'], fn.photoInsert(ps.infoAll[ps.keysALl[0]]['Фотография']), ps.infoAll[ps.keysALl[0]]['Цена'])
]

print(dataProduct)