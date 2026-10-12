# PS3 Revival Hub

Statyczna strona katalogowa dla społecznościowych projektów online gier PlayStation 3. Katalog jest przechowywany w `data/games.json`; strona nie pobiera już danych z Google Sheets. Zmiana bazy polega na edycji tego pliku i opublikowaniu zmian w repozytorium.

## Co zawiera strona

- wyszukiwarkę gier i projektów oraz filtry gatunku i statusu;
- karty gier z okładkami pobieranymi na żądanie z Wikimedia Commons/Wikipedii, jeśli są dostępne;
- projekty powiązane z grą, linki do ich stron i statusów oraz publiczne linki społeczności;
- osobne pola DNS i przyciski kopiowania;
- opisy ostrzegające o wpisach niepotwierdzonych i adresach testowych.

Strona jest niezależnym projektem społecznościowym i nie jest powiązana z Sony Interactive Entertainment. Statusy w katalogu są zgłoszeniami społeczności. DNS sam nie gwarantuje działania gry; projekt może wymagać aktywnych serwerów lub dodatkowej konfiguracji. Wewnętrzne odnośniki do prywatnych kanałów i wiadomości Discord nie są publikowane.

## Edycja katalogu

Edytuj `data/games.json`. Każdy wpis gry zawiera tytuł, platformę, gatunek, status, tytuł artykułu do wyszukania okładki oraz tablicę `projects`. Projekt może zawierać:

- `name` — nazwę projektu;
- `url`, `statusUrl`, `community` — opcjonalne publiczne odnośniki;
- `dns` i `alternates` — zgłoszone adresy;
- `note` — uwagi o stanie lub wymaganej konfiguracji.

Nie wpisuj prywatnych linków `discord.com/channels/...`. Zachowuj informację, czy adres jest lokalny lub wymaga weryfikacji.

GitHub Pages może serwować plik bez procesu budowania. Po włączeniu Pages w ustawieniach repozytorium zmiany w gałęzi publikacyjnej pojawią się na witrynie.
