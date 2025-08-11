#!/usr/bin/env bash
set -euo pipefail

REPO="Scarlateli/LeetCode"
OUT="README.md"

# Descobre linguagens por extensões presentes
declare -A MAP=( \
  [sql]="SQL" [c]="C" [h]="C" [java]="Java" [py]="Python" [cpp]="C++" \
  [js]="JavaScript" [ts]="TypeScript" [go]="Go" [rb]="Ruby" [kt]="Kotlin" [cs]="C#" [php]="PHP" \
)
declare -A found

# Procura extensões no repo (ignora .git e scripts/)
while IFS= read -r -d '' f; do
  ext="${f##*.}"
  [[ -n "${MAP[$ext]:-}" ]] && found["${MAP[$ext]}"]=1 || true
done < <(find . -type f \
  -not -path "./.git/*" -not -path "./scripts/*" -not -path "./.github/*" \
  \( -name "*.sql" -o -name "*.c" -o -name "*.h" -o -name "*.java" -o -name "*.py" -o -name "*.cpp" \
     -name "*.js" -o -name "*.ts" -o -name "*.go" -o -name "*.rb" -o -name "*.kt" -o -name "*.cs" -o -name "*.php" \) \
  -print0)

# Monta badges individuais das linguagens detectadas
lang_badges=""
for lang in "${!found[@]}"; do
  # badge simples, sem cor fixa
  slug="$(echo "$lang" | sed 's/ /%20/g')"
  lang_badges+=" ![${lang}](https://img.shields.io/badge/Language-${slug}-informational)"
done

# Badges do repo
badge_top="![top language](https://img.shields.io/github/languages/top/${REPO})"
badge_count="![languages](https://img.shields.io/github/languages/count/${REPO})"
badge_last="![last commit](https://img.shields.io/github/last-commit/${REPO})"
badge_size="![repo size](https://img.shields.io/github/repo-size/${REPO})"

# Lista problemas (pastas do LeetHub tipo 0123-nome-do-problema)
problems_md=""
while IFS= read -r dir; do
  base="$(basename "$dir")"
  title="$(echo "$base" | sed -E 's/^([0-9]+)/\1./; s/-/ /g')"
  url_enc="$(echo "$dir" | sed 's/ /%20/g')"

  # Linguagens usadas dentro da pasta
  declare -A pmap=()
  while IFS= read -r codef; do
    ext="${codef##*.}"
    [[ -n "${MAP[$ext]:-}" ]] && pmap["${MAP[$ext]}"]=1 || true
  done < <(find "$dir" -maxdepth 1 -type f -print)

  langs_line=""
  for k in "${!pmap[@]}"; do langs_line+="${k}, "; done
  langs_line="$(echo "$langs_line" | sed 's/, $//')"
  [[ -z "$langs_line" ]] && langs_line="—"

  problems_md+="- [${title}](${url_enc}) — ${langs_line}\n"
done < <(find . -maxdepth 1 -type d -name "[0-9][0-9][0-9][0-9]-*" | sort)

cat > "$OUT" <<MD
# LeetCode

${badge_top} ${badge_count} ${badge_last} ${badge_size}${lang_badges}

Repositório com **meus problemas resolvidos do LeetCode**.
As soluções são enviadas automaticamente pelo **LeetHub v2** e este README é **gerado automaticamente** para mostrar as linguagens usadas e a lista de problemas.

---

## 📋 Problemas resolvidos
${problems_md:-_Ainda não há problemas listados aqui._}

> Dica: as pastas originais do LeetHub (ex.: `0123-nome-do-problema/`) são mantidas na raiz.  
> Este README se atualiza sozinho a cada novo push.

MD
