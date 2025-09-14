from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word: str) -> str:
            return ''.join('*' if c in vowels else c for c in word.lower())

        # case-insensitive map (first occurrence kept)
        casempp = {}
        # vowel-error map
        vowmpp = {}

        for word in wordlist:
            lower = word.lower()
            if lower not in casempp:
                casempp[lower] = word
            dv = devowel(lower)
            if dv not in vowmpp:
                vowmpp[dv] = word

        res = []
        for query in queries:
            if query in wordlist:  # exact match
                res.append(query)
            elif query.lower() in casempp:  # case-insensitive match
                res.append(casempp[query.lower()])
            else:  # vowel-error match
                dv = devowel(query)
                if dv in vowmpp:
                    res.append(vowmpp[dv])
                else:
                    res.append("")
        return res