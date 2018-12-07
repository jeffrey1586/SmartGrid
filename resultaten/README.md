# Resultaten

Hieronder zijn de resultaten per algoritme in een tabel terug te vinden. De resultaten gelden voor wijk 1. Hierin zijn de totale kabel lengtes van de smartgrid uitgedrukt, met voor elk algoritme de beste score, gemiddelde score en standaardafwijking.

| **Algoritme**           | **Beste score** | **Gemiddelde** | **Standaardafwijking** | **Aantal runs** |  
| ------------------------| ---------------:| --------------:| ----------------------:| ---------------:|
| Greedy                  | 3876            | 3876           | 0                      | 1               |
| Shuffle                 | 3698            | 3964.59        | 79.20                  | 10 000          |
| Simple hillclimber      | 3682            | 3965.18        | 78.34                  | 10 000          |
| Stochastic hillclimber  | 3587            | 3863.94        | 99.22                  | 10 000          |
| Steepest ascend         | 3686            | 3944.22        | 80.37                  | 10 000          |       


Ter verduidelijking: het greedy-algoritme levert maar een score op en heeft dus geen gemiddelde en standaardafwijking. Dit komt omdat de volgorde waarin het algoritme te werk gaat niet verandert - en in resultaat dus ook geen veranderingen laat zien.

Per run wordt er een configuratie gecreëerd.

Bij alle hillclimbers wordt de aangeleverde oplossing gehaald uit het shiffle algoritme, tenzij anders vermeld.

Bij de hillclimber simple worden er per configuratie 149 swaps getest. De stochastic probeert per configuratie 1000 keer een verbetering te vinden. De steepest ascend hillclimber probeert per congiruatie 100 keer een verbetering te vinden. Het verschil in aantal keer verbetering zoeken komt door de tijd (de steepest ascend is langzamer).
