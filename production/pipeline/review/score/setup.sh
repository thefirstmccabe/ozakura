#!/bin/bash
# Set up the scored builds in a scratch folder: sparse worktrees at each commit (old review reports excluded),
# cold-reader packets made with each build's own reader_view.py (so names and glosses show as they did then),
# the dialogue brief from that commit, and today's lint. Usage: setup.sh SCRATCH_DIR   (run from anywhere in the repo)
set -e
S=${1:?scratch dir}; mkdir -p "$S"/readers "$S"/briefs "$S"/lint
REPO=$(git rev-parse --show-toplevel); K="$REPO/production/pipeline/review/score"; LINT="$REPO/production/pipeline/vn/script_lint.py"
python3 - "$K/builds.json" <<'PY' > "$S/builds.tsv"
import json,sys
for b in json.load(open(sys.argv[1]))["builds"]:
    print("\t".join([b["id"], b["sha"], str(b["chapter"]), ",".join(b["scripts"]), b["split"], b.get("reader_view_from") or b["id"], b.get("brief") or ""]))
PY
cd "$REPO"
while IFS=$'\t' read -r id sha ch scripts split rvfrom brief; do
  git cat-file -e "$sha" 2>/dev/null || git fetch -q --depth=1 origin "$sha"
  [ -d "$S/$id" ] || { git worktree add -q --no-checkout --detach "$S/$id" "$sha"
    (cd "$S/$id" && git sparse-checkout set --no-cone /v2/ /story/ /production/pilot-v2/ '!/production/pilot-v2/reviews/' /production/pipeline/ /production/refs/ /production/design/ /CLAUDE.md && git checkout -q "$sha"); }
  [ -n "$brief" ] && git show "$sha:$brief" > "$S/briefs/$id.md"
done < "$S/builds.tsv"
while IFS=$'\t' read -r id sha ch scripts split rvfrom brief; do
  W="$S/$id/production/pilot-v2/script"; srcs=(); for f in ${scripts//,/ }; do srcs+=("$W/$f"); done
  for r in 1 2 3; do d="$S/readers/$id/r$r"; rm -rf "$d"; mkdir -p "$d"
    python3 "$S/$rvfrom/production/pipeline/vn/reader_view.py" "$d" "${srcs[@]}" --split "$split" --cg-dir "$S/$id/v2/img/bg" >/dev/null; done
  last="${srcs[${#srcs[@]}-1]}"; python3 "$LINT" --chapter "$ch" "$last" > "$S/lint/$id.txt" 2>&1 || true
  echo "$id: $(ls "$S/readers/$id/r1" | grep -c part) parts; lint $(tail -1 "$S/lint/$id.txt")"
done < "$S/builds.tsv"
