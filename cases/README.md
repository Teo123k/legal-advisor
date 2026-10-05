# cases/ — client workspace (git-ignored)

Everything in here except this README and `_example/` is **ignored by git** and never pushed.

```
cases/<client>/
  intake.md        answers to intake questions
  uploads/         original files the client sent
  working/         extracted text, notes, sources.md (what was checked, when)
  report/          REVIEW.md · CHECKLIST.md · COVER_LETTER_vN.md
```
Create one with `scripts/new-case.sh "<client-name>"`.
Delete a client's folder when the matter is closed (data minimisation).
