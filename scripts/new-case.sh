#!/usr/bin/env bash
# Create a new (git-ignored) client case folder.
# Usage: scripts/new-case.sh "ahmed-spouse-2026"
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
NAME="${1:?Usage: new-case.sh <short-client-name>}"
SLUG="$(echo "$NAME" | tr '[:upper:] ' '[:lower:]-' | tr -cd 'a-z0-9-_')"
CASE="$REPO/cases/$SLUG"

if [ -d "$CASE" ]; then
  echo "ℹ️  Case already exists: $CASE"
  exit 0
fi

mkdir -p "$CASE"/{uploads,working,report}
cp "$REPO/templates/client-intake.md" "$CASE/intake.md"
cat > "$CASE/working/sources.md" <<EOF
# Sources checked for $SLUG
| date | url | quote / figure |
|---|---|---|
EOF

echo "✅ Created $CASE"
echo "   uploads/  ← put client files here"
echo "   working/  ← extracted text, notes, sources.md"
echo "   report/   ← REVIEW.md, CHECKLIST.md, COVER_LETTER_vN.md"
