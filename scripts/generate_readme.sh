#!/usr/bin/env bash
set -euo pipefail

REPO="Scarlateli/LeetCode"
OUT="README.md"

map_ext_to_lang() {
  case "$1" in
    sql) echo "SQL" ;;
    c|h) echo "C" ;;
    java) echo "Java" ;;
    py) echo "Python" ;;
    cpp) echo "C++" ;;
    js) echo "JavaScript" ;;
    ts) echo "TypeScript" ;;
    go) echo "Go" ;;
    rb) echo "Ruby" ;;
    kt) echo "Kotlin" ;;
    cs) echo "C#" ;;
    php) echo "PHP" ;;
    *) echo "" ;;
  esac
}

badge_top="![top language](https://img.shields.io/github/languages/top/${REPO})"
badge_count="![languages](https://img.shields.io/github/languages/count/${REPO})"
badge_last="![last commit](https://img.shields.io/github/last-commit/${REPO})"
badge_size="![repo size](https://img.shields.io/github/repo-size/${REPO})"

# Linguagens usadas dentro das pastas de problemas (./0000-*)
langs_tmp="$(mktemp)"
find . -maxdepth 2 -type f -regex './[0-9][0-9][0-9][0-9]-[^/]+/.*' \
  -not -path "./.git/*" -not -path "./.github/*" -not -path "./scripts/*" \
  | awk -F. '{print tolower($NF)}' \
  | while read -r ext; do
      lang="$(map_ext_to_lang "$ext")"
      [ -n "$lang" ] && echo "$lang"
    done \
  | sort -u > "$langs_tmp"

# Monta badges de linguagens detectadas
langs_badges=""
while read -r L; do
  [ -z "$L" ] && continue
  slug="$(echo "$L" | sed 's/ /%20/g')"
  langs_badges="${langs_badges} ![${L}](https://img.shields.io/badge/${slug}-%20-informational)"
done < "$langs_tmp"

# Lista de problemas com linguagens
problems_tmp="$(mktemp)"
find . -maxdepth 1 -type d -regex './[0-9][0-9][0-9][0-9]-.*' | sort > "$problems_tmp"

{
  echo "# LeetCode"
  echo
  echo "${badge_top} ${badge_count} ${badge_last} ${badge_size}${langs_badges}"
  echo
  echo "Repositório com **meus problemas resolvidos do LeetCode**."
  echo "As soluções são sincronizadas pelo **LeetHub v2**. Este README é **gerado automaticamente**."
  echo
  echo "---"
  echo
  echo "## 📋 Problemas resolvidos"
  if [ ! -s "$problems_tmp" ]; then
    echo "_Nenhum problema encontrado no padrão \`0000-nome-do-problema\` na raiz._"
  else
    while read -r dir; do
      base="$(basename "$dir")"
      title="$(echo "$base" | sed -E 's/^([0-9]+)/\1./; s/-/ /g')"
      # linguagens por problema
      pl_tmp="$(mktemp)"
      find "$dir" -type f \
        | awk -F. '{print tolower($NF)}' \
        | while read -r ext; do
            lang="$(map_ext_to_lang "$ext")"
            [ -n "$lang" ] && echo "$lang"
          done | sort -u > "$pl_tmp"
      langs_line="$(paste -sd', ' "$pl_tmp")"
      [ -z "$langs_line" ] && langs_line="—"
      link="$(echo "$dir" | sed 's/ /%20/g')"
      echo "- [${title}](${link}) — ${langs_line}"
      rm -f "$pl_tmp"
    done < "$problems_tmp"
  fi
} > "$OUT"

rm -f "$langs_tmp" "$problems_tmp"
