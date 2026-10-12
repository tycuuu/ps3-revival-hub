# PS3 Revival Hub — gotowy pakiet

## Pliki
- `index.html` — klasyczna strona retro, wyszukiwarka, filtry i kopiowanie adresów DNS.
- `config.js` — ustawiony na nowy opublikowany link CSV.
- `README.md` — instrukcja.

## Źródło danych
`https://docs.google.com/spreadsheets/d/e/2PACX-1vRtl-fj4jqAcie8rGQ0iI7HMg5C3JnzaUFZYbP9twG4YYK93OlqeVNOYjfswwhx0g/pub?gid=1640242559&single=true&output=csv`

## Wgranie na GitHub Pages
1. Otwórz repozytorium `tycuuu/ps3-revival-hub`.
2. Zastąp istniejący `index.html` plikiem z tego pakietu.
3. Zastąp istniejący `config.js` plikiem z tego pakietu.
4. Zapisz przez Commit changes.

## Oczekiwane nagłówki CSV
Strona rozpoznaje m.in.:
- `Gra`
- `Projekt / serwer`
- `Główny adres DNS` (obsługuje też wariant `DNS główny`)
- `Inne działające adresy DNS`
- `Platforma`
- `Status / pewność` lub `Status`
- `Uwagi` / `Uwagi / pewność`
- `Źródło / instrukcja`

## Uwaga
Nie udało się niezależnie odczytać zawartości nowego CSV w tym środowisku, więc przed publikacją nie mogłem potwierdzić rzeczywistych nagłówków ani danych. Jeśli karta używa innych nazw kolumn, dostosuj nagłówki albo napisz, jakie są, a dopasuję parser.
