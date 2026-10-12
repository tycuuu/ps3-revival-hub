# PS3 Revival Hub — start

To jest statyczna strona do hostowania na GitHub Pages. Ma wyszukiwarkę, filtry, karty gier i kopiowanie DNS. Bez podłączenia arkusza pokazuje przykładowe dane demonstracyjne.

## 1. Przygotuj kartę publiczną w Google Sheets

1. Otwórz swój arkusz.
2. Dodaj nową kartę o nazwie dokładnie `PUBLICZNE DNS`.
3. W pierwszym wierszu ustaw nagłówki (zachowaj nazwy):
   - `Gra`
   - `Projekt / serwer`
   - `DNS — jedna kolumna`
   - `Platforma`
   - `Status`
   - `Uwagi / pewność`
   - `Źródło / instrukcja`
4. Przenieś/skopiuj do niej wyłącznie informacje, które chcesz publikować. Nie dodawaj prywatnych notatek.
5. W Google Sheets wybierz **Plik → Udostępnij → Opublikuj w internecie**.
6. Wybierz tylko kartę `PUBLICZNE DNS`, a format publikacji ustaw na **CSV**. Nie publikuj całego skoroszytu.
7. Skopiuj wygenerowany link CSV.

Uwaga: publikowanie w internecie oznacza, że zawartość tej karty może być publicznie dostępna. Nie dawaj odwiedzającym uprawnień edycji. Jeśli chcesz mieć cały arkusz prywatny, nie włączaj „każdy z linkiem może edytować”.

## 2. Podłącz stronę do arkusza

Otwórz `config.js` i wpisz link CSV:

```js
window.PS3_REVIVAL_CONFIG = {
  csvUrl: "WKLEJ_TUTAJ_LINK_CSV"
};
```

Zapisz plik. Strona pobierze aktualne dane z CSV przy otwarciu/odświeżeniu. Możesz później dodać automatyczne odświeżanie.

## 3. Opublikuj stronę na GitHub Pages

1. Zaloguj się do GitHub i utwórz nowe publiczne repozytorium, np. `ps3-revival-hub`.
2. Wgraj `index.html`, `config.js` oraz `README.md` do głównego katalogu repozytorium.
3. Otwórz **Settings → Pages**.
4. W sekcji build/deployment wybierz **Deploy from a branch**, branch `main`, folder `/ (root)`, zapisz.
5. Po zakończeniu wdrożenia GitHub pokaże adres strony w sekcji Pages.

## 4. Discord

Na start przypnij link do strony w kanale `#baza-dns-ps3`. Potem możesz dodać webhook do kanału `#nowe-reaktywacje` albo bota z komendą `/dns`.

## Jak strona rozpoznaje kolumny

Rozpoznaje polskie nagłówki powyżej i alternatywne nagłówki `Game`, `Project`, `DNS`, `Platform`, `Status`, `Notes`, `URL`. Adresy niepotwierdzone nie mają przycisku kopiowania.

## Ważne

- Strona nie potwierdza automatycznie, że DNS lub serwer faktycznie działa — pokazuje status wpisany w arkuszu.
- Nie umieszczaj kluczy API ani haseł w plikach strony.
- Aktualizacje widoczne są po ponownym pobraniu CSV; cache przeglądarki może czasem opóźnić zmianę.
