# moje.hkfree.org — požadavky

## Účel
Self-service portál pro uživatele a členy hkfree.org na doméně moje.hkfree.org. Rozhraní a obsah jsou v češtině.

## Požadované funkce
Po přihlášení uživatel uvidí:
- Osobní údaje: jméno, příjmení, adresu, telefon a e-mail. Prozatím pouze kontrola/zobrazení; možnost editace nebyla zadána.
- Platební údaje: číslo účtu, variabilní symbol, částku a splatnost.
- Parametry připojení: IP adresu, výchozí bránu, masku sítě a DNS servery.
- Odkazy na vygenerované daňové doklady.
- Odkaz na změnu hesla.

## Aktuální etapa: statický návrh
- HTML a CSS bez backendu, sestavení a aplikačního frameworku.
- Twitter Bootstrap: lokálně uložená verze 5.3.8, včetně jeho JS pro dialog změny hesla.
- Responzivní přehled po přihlášení. Skutečné přihlášení, autorizace, načítání údajů, změna hesla a generování/stahování PDF nejsou součástí této etapy.
- Fiktivní osobní, platební a síťová data; viditelně označit ukázkový obsah. IP adresy z dokumentačních rozsahů. Nepoužívat údaje z návrhu k platbě.
- Odkazy na doklady vedou na HTML ukázku; dialog změny hesla má neaktivní formulář a vysvětlení.
- Vzhled navazuje na https://druzstvo.hkfree.org a zdrojáky /root/hkfree_druzstvo: původní logo, červená #cc0000, antracit #191c22, bílá a světle šedé plochy. Ovládání a rozložení využívá Bootstrap.
- Lokální assety, bez nutnosti externí CDN při prohlížení.
- Přístupné názvy, ovládání klávesnicí, viditelný focus a čitelnost na mobilu.
- Vývojový HTTP server na dostupném rozhraní 192.168.x.x a náhodném volném portu.

## Rozhodnutí pro první návrh
- Jeden přehled se sekcemi a boční navigací; mobilní navigace se vodorovně posouvá.
- Platba je v přehledu nejvýraznější, vedle osobních údajů; níže připojení a doklady.
- Částka 290 Kč vychází z veřejného webu, ale i ta je v návrhu pouze ukázková.
- Příští období je prosinec 2026, ukázková splatnost 25. listopadu předem.

## Před implementací backendu upřesnit
- Zdroj dat, API a způsob přihlašování; rozdíly rolí člen/uživatel.
- Více připojení na účtu a případné IPv6.
- Reálná pravidla plateb, období a dokladů.
- Proces změny hesla a případných oprav osobních údajů.
- Přístup k údajům a dokladům musí být na serveru omezen na oprávněného uživatele. Statický prototyp žádnou ochranu přihlášením neposkytuje.
