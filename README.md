# PS3 Revival Hub

Strona pobiera dane z publicznego eksportu CSV arkusza Google Sheets przy każdym otwarciu. Łączy obie tabele po tytule gry; edycje w arkuszu pojawiają się po odświeżeniu witryny.

## Arkusz i logotypy

Edytuj [arkusz PS3 DNS](https://docs.google.com/spreadsheets/d/1Oj3D-jTXuEPmC4b21FQ1I-K8JTJYQRkKkK4cBhTaHxs/edit?usp=sharing). Nie zmieniaj wierszy nagłówków `Gra` ani `PS3 Online Multiplayer Games`.

W pierwszej tabeli możesz dodać nagłówki w pustych kolumnach po prawej stronie:

- `Logo URL` — bezpośredni adres HTTPS do logotypu gry, najlepiej PNG z przezroczystym tłem lub SVG. Strona używa tylko adresów wpisanych w arkuszu; nie szuka automatycznie przypadkowych grafik. Jeśli adresu brakuje albo obraz nie działa, karta pokazuje nazwę gry.
- `Liczba graczy PS3` — opcjonalna wartość ręczna dla gier, których źródła nie obsługują automatycznego licznika.
- `Kategoria` — opcjonalna kategoria, która zastąpi kategorię rozpoznawaną przez stronę.

Wpisuj wartości w wierszu danej gry. Udostępnianie arkusza musi pozostać ustawione na „Każda osoba mająca link”. Nie umieszczaj tam danych poufnych. Prywatne odnośniki `discord.com/channels/...` nie są pokazywane; widoczne są tylko publiczne zaproszenia.

## Automatyczne liczniki

GitHub Actions odświeża liczby co 15 minut i publikuje snapshot w `data/live-counts.json`. Strona pobiera go z GitHub, niezależnie od odświeżania samej strony. Automatyczne liczniki obejmują TDU World (wyłącznie licznik PS3) i serwery BFBC2 z PS Restored (wyłącznie profile PSN). Buzz! Revival zostanie dodany do automatycznego odczytu, gdy będzie wpisany w arkuszu. Strona pokazuje czas ostatniego odczytu oraz osobne liczby dla serwerów BFBC2.

Liczników PS Rewired i Arcadii nie pokazujemy jako PS3-only, bo ich strony nie rozdzielają wiarygodnie konsoli od RPCS3. Endpoint Destination Home obecnie nie odpowiada. Jeśli licznik nie jest dostępny automatycznie, można wpisać jego wartość w kolumnie `Liczba graczy PS3`; strona oznaczy ją jako wartość z arkusza, nie jako live.

Workflow potrzebuje uprawnienia zapisu zawartości repozytorium (`Settings → Actions → General → Workflow permissions → Read and write permissions`). Nie zmienia ustawień GitHub Pages. Strona jest niezależnym projektem społecznościowym, niepowiązanym z Sony Interactive Entertainment.
