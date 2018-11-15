# SmartGrid

Veel huizen hebben tegenwoordig zonnepanelen om zelf energie mee te produceren. Deze productie is echter vaak groter dan de consumptie, waardoor de stroom die overblijft in batterijen opgeslagen moet worden. In SmartGrid worden drie wijken gevisualiseerd met elk drie batterijen, waarbij de opslag geregeld dient te worden: in deze code hebben wij oplossingen gevonden voor dit probleem, dat vier fases kent. 

![Plaatje van wijk 1](http://heuristieken.nl/wiki/index.php?title=File:Wijk1.png)
Bron: http://heuristieken.nl/wiki/index.php?title=SmartGrid

## Aan de slag (Getting Started)

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in [Python3.7.1](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
pip install matplotlib
pip install pandas
```

### Structuur (Structure)

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

## Auteurs (Authors)

* Jeffrey Chong
* Wim van Dijk

## Dankwoord (Acknowledgments)

* StackOverflow
* minor programmeren van de UvA
