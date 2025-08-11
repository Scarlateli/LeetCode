#!/usr/bin/env bash
set -euo pipefail
REPO="Scarlateli/LeetCode"
OUT="README.md"

badge_top="![Top Language](https://img.shields.io/github/languages/top/${REPO})"
badge_count="![Languages Count](https://img.shields.io/github/languages/count/${REPO})"
badge_last="![Last Commit](https://img.shields.io/github/last-commit/${REPO})"
badge_size="![Repo Size](https://img.shields.io/github/repo-size/${REPO})"

cat > "$OUT" <<MD
# LeetCode

${badge_top} ${badge_count} ${badge_last} ${badge_size}

Soluções via **LeetHub v2** organizadas por **Linguagem → Tópico**.

---

## 🔎 Navegação por Linguagem e Tópico
MD

gen_section () {
  local lang="$1"
  [ -d "$lang" ] || return 0
  find "$lang" -mindepth 1 -maxdepth 1 -type d | sort | while read -r topic_dir; do
    topic="$(basename "$topic_dir")"
    topic_url="${topic// /%20}"
    echo -e "\n### ${lang} → ${topic}" >> "$OUT"
    find "$topic_dir" -type f \( \
      -name "*.sql" -o -name "*.c" -o -name "*.h" \
      -o -name "*.py" -o -name "*.java" -o -name "*.cpp" \
      -o -name "*.js" -o -name "*.ts" -o -name "*.go" \
      -o -name "*.rb" -o -name "*.kt" -o -name "*.cs" \
      -o -name "*.php" \) | sort | while read -r file; do
      base="$(basename "$file")"
      name="${base%.*}"
      title="$(echo "$name" | sed -E 's/^([0-9]+)/\1./; s/-/ /g')"
      file_url="$(echo "$file" | sed 's/ /%20/g')"
      echo "- [${title}](${file_url})" >> "$OUT"
    done
  done
}

for lang in SQL C Java Python "C++" JavaScript TypeScript Go Ruby Kotlin "C#" PHP; do
  gen_section "$lang"
done

cat >> "$OUT" <<'MD'

---

## 📁 Estrutura sugerida

