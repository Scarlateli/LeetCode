#!/usr/bin/env bash
set -euo pipefail

REPO="Scarlateli/LeetCode"
OUT="README.md"

# mapa ext -> linguagem
declare -A MAP=(
  [sql]="SQL" [c]="C" [h]="C"
  [java]="Java" [py]="Python" [cpp]="C++"
  [js]="JavaScript" [ts]="TypeScript"
  [go]="Go" [rb]="Ruby" [kt]="Kotlin" [cs]="C#" [php]="PHP"
)

# badges do repo
badge_top="![top language](https://img.shields.io/github/languages/top/${REPO})"
badge_count="![languages](https://img.shields.io/github/languages/count/${REPO})"
badge_last="![last commit](https://img.shields.io/github/last-commit/${REPO})"
badge_size="![repo size](https://img.shields.io/github/repo-size/${REPO})"

# linguagens encontradas no repo (recursivo)
declare -A found
while IFS= read -r -d '' f; do
  ext="${f##*.}"; [[ ${MAP[$ext]+x} ]] && found["${MAP[$ext]}"]=1 || true
done < <(find . -type f -not -path "./.git/*" -not -path "./scripts/*" -not -path "./.github/*" -print0)

langs=""
for lang in "${!found[@]}"; do
  slug="${lang// /%20}"
  langs+=" ![${lang}](https://img.shields.io/badge/${slug}-%20-informational)"
done

# lista de problemas (pastas 0000-*)
problems=""
while IFS= read -r dir; do
  base="$(basename "$dir")"
  title="$(echo "$base" | sed -E 's/^([0-9]+)/\1./; s/-/ /g')"

  # linguagens usadas nesta pasta (recursivo)
  declare -A pl=()
  while IFS= read -r -d '' cf; do
    ext="${cf##*.}"; [[ ${MAP[$ext]+x} ]] && pl["${MAP[$ext]}"]=1 || true
  done < <(find "$dir" -type f -print0)

  ll=""; for k in "${!pl[@]}"; do ll+="$k, "; done; ll="${ll%, }"
  [[ -z "$ll" ]] && ll="—"

  link="$(echo "$dir" | sed 's/ /%20/g')"
  problems+="- [${title}](${link}) — ${ll}\n"
done < <(find . -maxdepth 1 -type d -name "[0-9][0-9][0-9][0-9]-*" | sort)

cat > "$OUT" <<MD
# LeetCode

${badge_top} ${badge_count} ${badge_last} ${badge_size}${langs}

Repositório com **meus problemas resolvidos do LeetCode**.  
As soluções vêm do **LeetHub v2** e o README é **gerado automaticamente**.

---

## 📋 Problemas resolvidos
${problems:-_Nenhum problema encontrado no padrão \`0000-nome-do-problema\` na raiz._}
MD
