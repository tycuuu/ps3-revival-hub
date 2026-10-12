# PS3 Revival Hub — styl PS Store

Wgraj `index.html` oraz `config.js` do głównego katalogu repozytorium GitHub Pages i zastąp istniejące pliki.

Strona pobiera dane z publicznego CSV ustawionego w `config.js`. Rozpoznaje kolumny:
- `Gra`
- `Projekt / serwer`
- `Główny adres DNS` (lub `DNS główny`)
- `Inne działające adresy DNS`
- `Platforma`
- `Status / pewność` lub `Status`
- `Uwagi` / `Uwagi / pewność`
- opcjonalnie `Logo gry` / `Okładka` / `Image URL` (pełny, publiczny URL do obrazka)
- opcjonalnie `Kategoria` / `Gatunek`

Jeśli podasz w arkuszu kolumnę `Logo gry` z publicznym linkiem do obrazka, karta pokaże grafikę. Jeśli jej brak, strona wyświetli stylizowany tytuł gry. Nie wbudowano niezweryfikowanych, przypadkowych logotypów.

Uwaga: nowy CSV nie został niezależnie odczytany w tym środowisku, więc nie potwierdzono nagłówków. Jeśli nazwy kolumn są inne, parser trzeba dopasować.
