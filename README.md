# PS3 Revival Hub

Strona pobiera dane z publicznego eksportu CSV arkusza Google Sheets przy każdym otwarciu. Łączy obie tabele po tytule gry; edycje w arkuszu pojawią się po odświeżeniu witryny.

## Arkusz i logotypy

Edytuj [arkusz PS3 DNS](https://docs.google.com/spreadsheets/d/1Oj3D-jTXuEPmC4b21FQ1I-K8JTJYQRkKkK4cBhTaHxs/edit?usp=sharing). Nie zmieniaj wierszy nagłówków `Gra` ani `PS3 Online Multiplayer Games`.

W pierwszej tabeli możesz dodać nagłówki w pustych kolumnach po prawej stronie:

- `Logo URL` — bezpośredni adres HTTPS do logotypu gry (najlepiej PNG z przezroczystym tłem lub SVG). Strona wyświetla tylko grafiki wpisane w arkuszu; przy braku lub błędzie obrazka zostaje nazwa gry.
- `Liczba graczy PS3` — liczba do wyświetlenia przy grze. Aktualnie źródła nie pozwalają na bezpośrednie pobieranie liczników z przeglądarki, więc tę wartość trzeba aktualizować w arkuszu.
- `Kategoria` — opcjonalna kategoria, która zastąpi automatyczny filtr gatunku.

Po dodaniu nagłówka wpisuj wartości w tym samym wierszu co gra. Udostępnianie arkusza musi pozostać ustawione na „Każda osoba mająca link”. Nie umieszczaj tam danych poufnych. Prywatne odnośniki `discord.com/channels/...` nie są pokazywane na stronie; widoczne są jedynie publiczne zaproszenia.

## Liczniki online

Liczba graczy może być pokazana, jeśli jest dostępna jako kolumna `Liczba graczy PS3` w arkuszu. Nie oznaczam jej jako live, bo obecne strony liczników nie zezwalają na odczyt z domeny GitHub Pages przez przeglądarkę (brak CORS), a jeden z używanych endpointów zwraca 404. Automatyczne i aktualne liczniki wymagałyby osobnego serwera pośredniczącego, który pobiera dane i zapisuje je do arkusza lub publikuje jako plik.

Statusy i adresy DNS są informacjami społecznościowymi i mogą wymagać weryfikacji. DNS sam nie gwarantuje działania gry. Strona jest niezależnym projektem, niepowiązanym z Sony Interactive Entertainment.
