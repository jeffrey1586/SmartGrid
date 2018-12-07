# SmartGrid

Veel huizen hebben tegenwoordig zonnepanelen om zelf energie mee te produceren. Deze productie is echter vaak groter dan de consumptie, waardoor de stroom die overblijft in batterijen opgeslagen moet worden. In SmartGrid worden drie wijken gevisualiseerd met elk vijf batterijen, waarbij de opslag geregeld dient te worden: in deze code hebben wij oplossingen gevonden voor dit probleem, dat vier fases kent.

![Wijk 1 met kabellengte 3772](https://github.com/jeffrey1586/SmartGrid/blob/master/doc/better%20visualization%20standard%20wijk1.png)  

In fase a) dienen alle huizen aan de batterijen te worden aangesloten, zonder dat er batterijen overladen worden. In fase b) wordt die configuratie geoptimaliseerd. Dat wil zeggen, dat de aansluiting met zo min mogelijk kabel plaats vindt. In fase c) kunnen de batterijen worden verplaatst, met als doel de SmartGrids verder te optimaliseren. In fase d) worden tot slot de batterijen vervangen door andersoortige batterijen, die in capaciteit en prijs verschillen.

**De toestandsruimte**, ofwel het aantal mogelijke oplossingen voor een probleem, verschilt per fase, hoewel deze gelijk is voor fase a en b. Het aantal mogelijke smartgrids voor deze stages kan in de volgende **complexiteitsfunctie** worden gedefinieerd:

    aantal batterijen ^ n

waarbij n het aantal huizen in de smartgrid is. Deze functie kan voor a en b alsvolgt worden ingevuld: 5^150. Het aantal configuraties is dan 7.00649232e104, wat de grootte van het probleem weergeeft. Hierbij zitten dus ook configuraties die onbruikbaar zijn: bijvoorbeeld waarbij alle huizen op 1 batterij aangesloten zijn. De configuraties die wel bruikbaar zijn, voldoen aan de constraint dat elk huis aangesloten is én aan de constraint dat geen enkele batterij overladen is. Om een begin te maken met het uitfilteren van foute configuraties, proberen we door onderstaande aanpassing op de complexiteitsfunctie de configuraties waarbij een, twee, drie of vier batterijen niét gebruikt worden weg te halen. Bij deze configuraties vindt een overlading altijd plaats.

    aantal batterijen ^ n / 4 ^ n

Dit uitfilteren werkt echter alleen bij algoritmes die deze configuraties ook daadwerkelijk links laten liggen.

**De scorefunctie** voor fase a) en b) kan zo gedefinieerd worden:

    kabellengte * 9 + 25 000

In deze is de kabellengte het aantal grids dat alle kabels beslaan. Per gridsegment kost een kabel €9. In de wijken voor a en b zijn altijd 5 batterijen aanwezig, die per stuk €5000 kosten: 5 * €5000 = €25 000.

De upperbound van deze scorefunctie, ofwel de hoogst mogelijke kosten die een configuratie zou kunnen halen (en daarmee de slechtste score), is in de onderstaande formule weergegeven. Hierbij is x de kabellengte tussen het huis en de batterij in een wijk die het verst van elkaar af liggen. n is het aantal huizen in de wijk.

    (n * x) * 9 + 25 000

De lowerbound, ofwel de laagst mogelijke kosten die een configuratie zou kunnen halen (en dus de beste score), is in onderstaande formule weergegeven. De kortste afstand die een huis af zou kunnen leggen is 1; n is het aantal huizen in de wijk.

    (n * 1) * 9 + 25 000

## Algoritmes
**Greedy algoritme**
In onze code passen we een greedy algorithm toe om een Smartgrid te configureren. Eerst laden we in de method ´load_batteries’ alle batterijen in, waarin elke batterij een object wordt die een x-, y- en capaciteitswaarde toegekend krijgt (zie het bestand battery.py in code/classes). Dit doen we ook voor de huizen in de method ‘load_houses’: deze krijgen echter in plaats van een capaciteit een output.

Dan vindt het verbinden van huizen met batterijen plaats in de method ‘connecting’. Voor elk huis wordt:
de afstand naar elke batterij berekend;
de kleinste afstand uitgekozen (kenmerkend voor een greedy algorithm);
de bij de kleinste afstand horende batterij aan het huis verbonden, tenzij de capaciteit overschreden wordt: het huis krijgt dan de batterij die daarna het dichtstbijzijnd is (en capaciteit over heeft).

Dit algoritme levert een configuratie met een totale kabellengte van 3876 op en is bovenaan de README gevisualiseerd.
(smartgridHouse.py: op regel 86 kan shuffle uit worden gezet).

**Shuffle methode**
Eveneens kan er in deze code gekozen worden voor een algoritme dat bovenstaande configuratie ‘shufflelt’. Dat wil zeggen, de volgorde waarin de huizen elk op zoek gaan naar batterijen, wordt willekeurig aangepast. Het kan namelijk zo zijn dat er een huis verbonden wordt aan een batterij die ver weg staat, terwijl er voor dit huis een andere batterij veel dichter in de buurt staat. Aan deze laatste batterij wordt dit huis echter dan niet verbonden, omdat de capaciteit al vol zou kunnen zitten.

De verbindingsvolgorde is dus relevant. Het shufflen (zie functie ‘Shuffle’) verandert op willekeurige wijze deze volgorde. De methode is roekeloos, maar levert wel verbetering ten opzichte van niet-shufflen. Zie voor preciezere resultaten de README in het mapje 'resultaten'.
(smartgridHouse.py).

**Hillclimber algoritmes**
In deze code is onder andere een hillclimber algorithm geschreven om te testen of een simpele swap functie verbetering oplevert.

De swap houdt hier in dat de batterijen van twee huizen, die onder elkaar staan in het list van huizen, verwisseld worden (mits het verschillende batterijen zijn), waarna gekeken wordt of de totale lengte verkleind is. Als dat het geval is, dan wordt de capaciteit van de batterijen gecontroleerd: als deze niet overschreden is, wordt de swap definitief toegepast en behouden. De hillclimber begint dan met de volgende swap. (smartgridHillclimber.py).

De verbetering die dit algoritme in de scorefunctie oplevert is minimaal. Zie voor preciezere resultaten de README in het mapje 'resultaten'.

Een tweede hillcimber die is geïmplementeerd is de stochastic hillcimber. Deze neemt twee willekeurige huizen, verwisselt de batterijen en kijkt of er een kortere kabellengte ontstaat. Als dat het geval is, wordt de swap behouden en begint het algoritme opnieuw. De batterijen worden uiteraard niet overladen: eveneens vindt er geen batterijwissel plaats tussen twee huizen die dezelfde batterij gebruiken. Zie voor de resultaten de README in het mapje 'resultaten' (smartgridStochastic.py).

Ten slotte is er een derde hillcimber, de steepest ascend. Deze pakt eerst een random huis uit de lijst met huisobjecten en genereert vervolgens elke mogelijke swap voor dit huis. De beste swap wordt toegepast, waarna het algoritme opnieuw start met het volgende huis uit de lijst. Zie voor de resultaten de README in het mapje 'resultaten' (smartgridSteepest.py).

## Aanvullende exploratie
**vanuit batterij**
Zoals eerder vermeld is de volgorde waarin huizen verbonden worden relevant. Eveneens is het object van waaruit verbonden wordt relevant: dat kan vanuit een huis zijn, of vanuit een batterij (smartgridBattery.py).

In de code zoals deze nu is, is het echter onmogelijk om het laatste huis nog te verbinden. Geen enkele batterij heeft nog genoeg capacteit over om de laatste output op te vangen. Het resultaat zonder deze laatste verbinding is een kabellengte van  3817: verbetering van de code zal moeten laten blijken of deze verbindingswijze beter is.

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
