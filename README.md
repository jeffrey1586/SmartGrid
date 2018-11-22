# SmartGrid

Veel huizen hebben tegenwoordig zonnepanelen om zelf energie mee te produceren. Deze productie is echter vaak groter dan de consumptie, waardoor de stroom die overblijft in batterijen opgeslagen moet worden. In SmartGrid worden drie wijken gevisualiseerd met elk vijf batterijen, waarbij de opslag geregeld dient te worden: in deze code hebben wij oplossingen gevonden voor dit probleem, dat vier fases kent. 

![Plaatje van wijk 1]  
Bron: http://heuristieken.nl/wiki/index.php?title=SmartGrid

In fase a) dienen alle huizen aan de batterijen te worden aangesloten, zonder dat er batterijen overladen worden. In fase b) wordt die configuratie geoptimaliseerd. Dat wil zeggen, dat de aansluiting met zo min mogelijk kabel plaats vindt. In fase c) kunnen de batterijen worden verplaatst, met als doel de SmartGrids verder te optimaliseren. In fase d) worden tot slot de batterijen vervangen door andersoortige batterijen, die in capaciteit en prijs verschillen.

**De toestandsruimte**, ofwel het aantal mogelijke oplossingen voor een probleem, verschilt per fase, hoewel deze gelijk is voor fase a en b. Het aantal mogelijke smartgrids voor deze stages kan in de volgende **complexiteitsfunctie** worden gedefinieerd: 

    aantal batterijen ^ n
  
waarbij n het aantal huizen in de smartgrid is. Deze functie kan voor a en b alsvolgt worden ingevuld: 5^150. Het aantal configuraties is dan 7.00649232e104, wat de grootte van het probleem weergeeft. Hierbij zitten dus ook configuraties die onbruikbaar zijn: bijvoorbeeld waarbij alle huizen op 1 batterij aangesloten zijn. De configuraties die wel bruikbaar zijn, voldoen aan de constraint dat elk huis aangesloten is én aan de constraint dat geen enkele batterij overladen is. Om een begin te maken met het uitfilteren van foute configuraties, proberen we door onderstaande aanpassing op de complexiteitsfunctie de configuraties waarbij een, twee, drie of vier batterijen niét gebruikt worden weg te halen. Bij deze configuraties vindt een overlading altijd plaats.

    aantal batterijen ^ n / 4 ^ n
  
Dit uitfilteren werkt echter alleen bij algoritmes die deze configuraties ook daadwerkelijk links laten liggen.

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

Om de code te draaien met de standaardconfiguratie (bv. brute-force en data/wijk1_batterijen.csv, data/wijk1_huizen.csv) gebruik de instructie:

```
python smartgrid.py
```

## Auteurs (Authors)

* Jeffrey Chong
* Wim van Dijk

## Dankwoord (Acknowledgments)

* StackOverflow
* minor programmeren van de UvA
