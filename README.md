# PS3 Revival Hub — automatyczne grafiki

Pliki: `index.html`, `config.js`, `README.md`.

Strona najpierw używa grafiki z kolumny `Logo gry`, `Okładka`, `Image URL` lub podobnej, jeśli została podana. W przeciwnym razie próbuje automatycznie znaleźć grafikę przez publiczne API Wikipedii (bez klucza API). Wynik może być grafiką artykułu, a nie zawsze dokładną okładką pudełkową PS3.

SteamGridDB ma okładki i grafiki, ale wymaga klucza API. Nie wkładamy go do `index.html`, bo na GitHub Pages byłby publiczny. Aby mieć dokładne okładki PS3 dla wszystkich tytułów, można później uzupełnić kolumnę `Okładka` sprawdzonymi URL-ami.

Wgraj `index.html` i `config.js` do repozytorium `tycuuu/ps3-revival-hub`, zastępując poprzednie pliki.
