# PS3 Revival Hub

Statyczna strona katalogowa dla społecznościowych projektów online gier PlayStation 3. Głównym źródłem danych jest publiczny eksport CSV z arkusza Google Sheets. Strona pobiera go przy każdym otwarciu, łączy obie tabele według tytułu gry i pokazuje zmienione dane bez przebudowywania strony. `data/games.json` jest kopią zapasową na wypadek chwilowej niedostępności arkusza.

## Edytowanie danych

Edytuj [arkusz PS3 DNS](https://docs.google.com/spreadsheets/d/1Oj3D-jTXuEPmC4b21FQ1I-K8JTJYQRkKkK4cBhTaHxs/edit?usp=sharing). Nie zmieniaj wierszy nagłówków `Gra` ani `PS3 Online Multiplayer Games`, bo strona używa ich do rozpoznania dwóch sekcji. Zapisz zmiany; po odświeżeniu strony aktualny arkusz zostanie pobrany ponownie. Link **Edytuj arkusz** prowadzi z witryny prosto do arkusza.

Arkusz musi pozostać udostępniony osobom mającym link. Witryna korzysta z publicznego eksportu CSV, więc nie wymaga klucza API ani logowania. Nie umieszczaj w nim danych poufnych. Prywatne odnośniki `discord.com/channels/...` nie są wyświetlane; widoczne są tylko publiczne zaproszenia Discord.

## Co zawiera strona

- wyszukiwarkę gier i projektów oraz filtry gatunku i statusu;
- karty gier z okładkami pobieranymi na żądanie z Wikimedia, jeśli są dostępne;
- projekty, odnośniki do ich stron i statusów oraz publiczne linki społeczności;
- osobne pola DNS i przyciski kopiowania;
- czytelne opisy statusów niepotwierdzonych i lokalnych adresów testowych.

Statusy są informacjami społecznościowymi i mogą się zmieniać. DNS sam nie gwarantuje działania gry; projekt może wymagać aktywnych serwerów lub dodatkowej konfiguracji. Strona jest niezależnym projektem i nie jest powiązana z Sony Interactive Entertainment.

## GitHub Pages

Repozytorium publikuje stronę z plików w głównym katalogu. Włączone już GitHub Pages aktualizuje witrynę po zmianie opublikowanej gałęzi. Adres: <https://tycuuu.github.io/ps3-revival-hub/>.

