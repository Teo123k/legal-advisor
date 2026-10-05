# 🇪🇺 Europe — Phase 3 (planned)

Structure prepared so EU countries plug in the same way as the UK.

## Layers of EU immigration law
1. **EU law (applies across member states)**
   - Directive 2004/38/EC (Free Movement / Citizens' Rights) — family of EU citizens who *move*
   - Directive 2003/86/EC (Family Reunification) — third-country nationals sponsoring family
     (not applicable in Denmark and Ireland)
   - Directive 2003/109/EC (Long-term residents), EU Blue Card Directive (EU) 2021/1883
   - Schengen Borders Code / Visa Code (short stays)
   - CJEU case law (e.g. *Metock* C-127/08, *Zambrano* C-34/09, *Chavez-Vilchez* C-133/15, *Chakroun* C-578/08) — `verify` before use
2. **National law** — each country implements and adds its own spouse-visa rules (income, language,
   integration tests, age limits).
3. **ECHR Art. 8** — applies in all Council of Europe states (ECtHR case law: *Jeunesse v Netherlands*, etc.).

## Planned folder layout
```
eu/
  _eu-law/            directives, CJEU case law, Art 8 ECtHR
  ireland/            (common UK-adjacent demand; not bound by 2003/86)
  germany/            Ehegattennachzug (§§ 27–30 AufenthG), A1 German
  france/             regroupement familial / conjoint de Français
  netherlands/        partner (MVV), civic integration exam
  spain/              reagrupación familiar / tarjeta comunitaria
  italy/  portugal/  ...
```
Each country folder copies the UK route structure (`../uk/README.md`).

## Priority order (suggested — confirm with owner)
1. Ireland 2. Germany 3. Netherlands 4. France 5. Spain 6. Portugal 7. Italy
