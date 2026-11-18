# Instrukce pro agenty

## Kontext a jazyk
- Projekt je moje.hkfree.org, samoobslužný portál uživatelů a členů hkfree.org.
- Komunikuj s uživatelem česky. Rozhraní i dokumentaci piš česky.
- Před úpravami si přečti requirements.md a stávající soubory. Udržuj požadavky a přijatá rozhodnutí aktuální.

## Aktuální rozsah
- Zatím statické HTML/CSS, bez backendu a bez build kroku. Nepřidávej framework nebo skutečné přihlášení bez zadání.
- Veřejně servírované soubory jsou pouze v public/. Dokumentace a Git nesmí být kořenem webserveru.
- Zachovej Bootstrap (lokální soubory v public/assets/vendor/bootstrap/ a jeho licenci). Vlastní styly jsou v public/assets/style.css.
- Statický prototyp obsahuje pouze zřetelně označené fiktivní údaje. Nevkládej skutečná osobní data, přístupové údaje ani tajemství.
- Nepředstírej úspěšné změny hesla, platby či existenci skutečných dokladů. Ukázkové interakce srozumitelně označ.

## Vzhled
- Navaž na druzstvo.hkfree.org, referenční zdroj je /root/hkfree_druzstvo (pouze reference, neupravovat v rámci tohoto projektu).
- Zachovej logo hkfree.org, červenou #cc0000 a antracit #191c22, bílé karty a Bootstrap komponenty.
- Stránky musí fungovat na mobilu i desktopu; ověř horizontální přetečení, klávesnici, dialogy a odkazy. Uživatelské údaje nejsou editovatelné, dokud to nebude zadáno.

## Ověření a náhled
- Spuštění: python3 -m http.server PORT --bind 0.0.0.0 --directory public
- Vyber volný port a zjisti skutečnou IP příkazem ip -4 addr. Ověř HTTP odpověď přes tuto adresu.
- Při zadání náhledu nech vývojový server běžet a sděl uživateli přesnou URL. Nepublikuj do Sites nebo jiné produkce bez zadání.
- Pro tento statický návrh stačí kontrola HTTP, lokálních odkazů a assetů a vizuální/klávesnicové ověření desktopu a mobilu, je-li prohlížeč dostupný. Nezaváděj testovací framework kvůli drobným vizuálním úpravám.
- Při změně fungování aktualizuj README.md. Neměň cizí soubory a neprováděj nevyžádaný commit/push.

## Dokumentace
- README.md udržuj stručné: účel projektu, spuštění a odkazy na související dokumentaci. Nevypisuj v něm přehled jednotlivých souborů.
- Rozsáhlejší tematickou dokumentaci piš do samostatných souborů v doc/ a podle potřeby na ni odkazuj z README.md.
