#!/usr/bin/env bash
# Install the immigration-advisor skill into Hermes by symlinking (git pull = instant update).
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
DEST="$HERMES_HOME/skills/legal/immigration-advisor"

mkdir -p "$(dirname "$DEST")"
if [ -e "$DEST" ] && [ ! -L "$DEST" ]; then
  echo "⚠️  $DEST exists and is not a symlink — move it away first." >&2
  exit 1
fi
ln -sfn "$REPO/skills/immigration-advisor" "$DEST"

# Record repo location for the skill ($LEGAL_ADVISOR_HOME)
ENV_FILE="$HERMES_HOME/.env"
touch "$ENV_FILE"
if grep -q '^LEGAL_ADVISOR_HOME=' "$ENV_FILE"; then
  sed -i.bak "s|^LEGAL_ADVISOR_HOME=.*|LEGAL_ADVISOR_HOME=$REPO|" "$ENV_FILE" && rm -f "$ENV_FILE.bak"
else
  echo "LEGAL_ADVISOR_HOME=$REPO" >> "$ENV_FILE"
fi

mkdir -p "$REPO/cases"
chmod +x "$REPO"/scripts/*.sh "$REPO"/scripts/*.py 2>/dev/null || true

echo "✅ Skill linked: $DEST -> $REPO/skills/immigration-advisor"
echo "✅ LEGAL_ADVISOR_HOME=$REPO written to $ENV_FILE"
echo "➡️  Restart Hermes (or start a new session), then say: 'review my spouse visa docs'"
