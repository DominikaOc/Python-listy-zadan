
def najludniejszy_region():
    # 1. Wczytanie populacji państw do słownika
    populacje_panstw = {}
    with open("populations.txt", "r", encoding="utf-8") as f:
        for linia in f:
            linia = linia.strip()
            if linia:  # pomijamy ewentualne puste linie
                kraj, pop_str = linia.split(",")
                populacje_panstw[kraj.strip()] = int(pop_str.strip())

    # 2. Grupowanie populacji według regionów
    populacje_regionow = {}
    with open("regions.txt", "r", encoding="utf-8") as f:
        for linia in f:
            linia = linia.strip()
            if linia:
                kraj, region = linia.split(":")
                kraj = kraj.strip()
                region = region.strip()

                # Pobieramy populację kraju (zakładamy, że zawsze tam jest)
                populacja_kraju = populacje_panstw[kraj]

                # Dodajemy populację do odpowiedniego regionu
                if region in populacje_regionow:
                    populacje_regionow[region] += populacja_kraju
                else:
                    populacje_regionow[region] = populacja_kraju

    # 3. Znalezienie regionu o maksymalnej łącznej populacji.
    # Funkcja max z argumentem key=populacje_regionow.get zwraca klucz (nazwę regionu),
    # dla którego wartość (populacja) jest największa.
    najludniejszy = max(populacje_regionow, key=populacje_regionow.get)

    return najludniejszy

print(najludniejszy_region())