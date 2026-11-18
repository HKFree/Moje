# moje.hkfree.org

Statický návrh samoobslužného portálu hkfree.org v Bootstrapu. Obsahuje platební QR a fiktivní data; přihlášení, změna hesla a PDF doklady zatím nejsou napojené.

Spuštění z kořene projektu (bez instalace a sestavení):

```sh
python3 -m http.server 38471 --bind 0.0.0.0 --directory public
```

Náhled: http://localhost:38471/ nebo IP serveru se stejným portem.

[Požadavky](requirements.md) · [Instrukce pro agenty](AGENTS.md)

Rozsáhlejší dokumentace patří do samostatných souborů v `doc/`.
