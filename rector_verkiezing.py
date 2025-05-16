from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"
    






    lijst_van_kandidaten = [
        RectorKandidaat("Jan Jansen", "Faculteit der Letteren"),
        RectorKandidaat("Piet Pieters", "Faculteit der Natuurwetenschappen"),
        RectorKandidaat("Klaas Klaassen", "Faculteit der Sociale Wetenschappen"),
        RectorKandidaat("Marie Marie", "Faculteit der Geneeskunde"),
        RectorKandidaat("Anna Anna", "Faculteit der Rechten"),
        RectorKandidaat("Elsa Elsa", "Faculteit der Economie"),
        RectorKandidaat("Hans Hans", "Faculteit der Techniek"),
        RectorKandidaat("Sophie Sophie", "Faculteit der Kunst"),
    ]