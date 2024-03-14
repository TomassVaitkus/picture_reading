nuotraukos nuskaitymo aprašas:

* [X] visai neblogai nuskaito ir sukrauna i txt faila (Done)
* [X] dabar nusiskaicius tekstini faila visai sveika butu kazkaip su regex biblioteka (Done)
  isskaidyti, kur skaiciai, kur tekstas. Bėda ta, kad  kartais tarp skaiciu yra tarpai, kurie trukdys teisingai suformuoti teisingus skaicius.

  antras variantas yra skaityti kiekviena eilute esancia txt faile ir tikrinti ar toje eiluteje yra atitinkami zodziai is ieskomu zodziu saraso pvz ['imones kodas','atlyginimu mediana'] ir kiti. Ir jei randama, tokiu atveju apdirbam ji su regex ir issitraukiam norima vieta, kuria dedam i dataframe atitinkama stulpeli. Panasu, kad sitas visai padeda... susitvarkiau, kad nuskaitytu lietuviskas raides ir dabar galima ieskoti sarase norimu fraziu :) (Done)

Tai nuskaitymas kaip ir padarytas is nuotraukos, dabar reikia kazkaip pritaikyti tai norimoms papkutems keiciant url daryt vis naujas nuotraukas

Taip pat reikia pasidaryti, kad eitu per imoniu sarasa. Tai greiciausiai bus koks nors listas imoniu pavadinimu ir per fora tures eiti ir gaminti vis nauja url, kuri reiks paduot nuotraukos darymui.
