"""Grænsefladen mellem chatbotten og vagthunden.

Chatbotten kalder vagthunden tre steder:

    tjek_besked()    før chatbotten læser kundens besked      (lag 1: stop snyd)
    tjek_svar()      før kunden ser chatbottens svar          (lag 2: stop læk)
    tjek_handling()  før et værktøj bliver udført             (lag 3: stop forbudte handlinger)

Hver metode returnerer en Vurdering med en farve:

    grøn  = ok, fortsæt
    gul   = et menneske skal kigge på det først
    rød   = blokeret

DENNE FIL ER KUN ET SKELET. Alle tre lag svarer "grøn" hele tiden, så
chatbotten kører helt uden beskyttelse. Det er sådan, testrunde 1 skal køres.
Person B bygger de rigtige tjek ind i de tre metoder.
"""

from dataclasses import dataclass

GROEN, GUL, ROED = "grøn", "gul", "rød"


@dataclass
class Vurdering:
    farve: str          # "grøn", "gul" eller "rød"
    begrundelse: str    # kort forklaring, vises i loggen og på dashboardet
    lag: int            # 1, 2 eller 3


class Vagthund:
    def __init__(self, lag1=False, lag2=False, lag3=False):
        # Hvert lag kan slås til og fra, så de tre testrunder kan køres.
        self.lag1 = lag1
        self.lag2 = lag2
        self.lag3 = lag3

    def tjek_besked(self, besked, kunde):
        """Lag 1: Er kundens besked et forsøg på prompt injection?"""
        if not self.lag1:
            return Vurdering(GROEN, "Lag 1 er slået fra.", 1)
        # TODO (B): mønstertjek + AI-tjek af beskeden.
        return Vurdering(GROEN, "Lag 1 er ikke bygget endnu.", 1)

    def tjek_svar(self, svar, kunde):
        """Lag 2: Indeholder chatbottens svar data, kunden ikke må se?"""
        if not self.lag2:
            return Vurdering(GROEN, "Lag 2 er slået fra.", 2)
        # TODO (B): tjek for andre kunders data og for indhold fra systemprompten.
        return Vurdering(GROEN, "Lag 2 er ikke bygget endnu.", 2)

    def tjek_handling(self, kundens_besked, vaerktoej, input_data, kunde):
        """Lag 3: Må chatbotten udføre denne handling?

        Bemærk, hvad metoden får at se: kundens oprindelige besked, værktøjets
        navn og input samt kunden. Den får IKKE resten af samtalen eller de
        data, chatbotten har læst. Så kan skjult tekst i data ikke nå herind.
        """
        if not self.lag3:
            return Vurdering(GROEN, "Lag 3 er slået fra.", 3)
        # TODO (B): rettighedskort først, derefter AI-formålstjek.
        return Vurdering(GROEN, "Lag 3 er ikke bygget endnu.", 3)
