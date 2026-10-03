#!/usr/bin/env bash
# Instantiate a new project from _templates/project (+ optional pack) and register it.
# Usage: scripts/new-project.sh <slug> [--name "Display Name"] [--type business|markets|personal|other] [--pack stocks|crypto]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLUG="${1:-}"; shift || true
NAME=""; TYPE="business"; PACK="none"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name) NAME="$2"; shift 2 ;;
    --type) TYPE="$2"; shift 2 ;;
    --pack) PACK="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

[[ "$SLUG" =~ ^[a-z0-9][a-z0-9-]*$ ]] || { echo "slug must be lowercase letters, digits, dashes" >&2; exit 2; }
[[ "$PACK" =~ ^(none|stocks|crypto)$ ]] || { echo "pack must be stocks|crypto|none" >&2; exit 2; }
[[ -n "$NAME" ]] || NAME="$SLUG"
[[ "$PACK" != none ]] && TYPE="markets"

DEST="$ROOT/projects/$SLUG"
[[ -e "$DEST" ]] && { echo "refusing: $DEST already exists" >&2; exit 1; }

DATE="$(date +%Y-%m-%d)"
cp -R "$ROOT/_templates/project" "$DEST"

if [[ "$PACK" != none ]]; then
  PACKDIR="$ROOT/_templates/packs/$PACK"
  # Pack files override/add to the base; CLAUDE.append.md is appended to the project CLAUDE.md.
  (cd "$PACKDIR" && find . -type f ! -name CLAUDE.append.md) | while read -r f; do
    mkdir -p "$DEST/$(dirname "$f")"; cp "$PACKDIR/$f" "$DEST/$f"
  done
  cat "$PACKDIR/CLAUDE.append.md" >> "$DEST/CLAUDE.md"
fi

# Placeholder substitution (perl: identical behaviour on macOS and Linux).
export NAME SLUG DATE TYPE PACK
find "$DEST" -type f \( -name '*.md' -o -name '*.csv' \) -print0 | xargs -0 perl -pi -e '
  s/\{\{NAME\}\}/$ENV{NAME}/g; s/\{\{SLUG\}\}/$ENV{SLUG}/g; s/\{\{DATE\}\}/$ENV{DATE}/g;
  s/\{\{TYPE\}\}/$ENV{TYPE}/g; s/\{\{PACK\}\}/$ENV{PACK}/g;'

printf '| %s | %s | %s | %s | onboarding | ROOKAS | projects/%s | %s |\n' \
  "$SLUG" "$NAME" "$TYPE" "$PACK" "$SLUG" "$DATE" >> "$ROOT/_system/REGISTRY.md"

echo "created projects/$SLUG (type=$TYPE pack=$PACK) and registered it."
echo "next: run the /new-project onboarding interview to fill PROJECT_CONTEXT, OBJECTIVES, METRICS, data sources."
