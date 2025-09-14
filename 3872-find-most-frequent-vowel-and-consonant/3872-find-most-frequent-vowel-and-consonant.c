int is_vowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int maxFreqSum(char* s) {
    int mp[26] = {0};
    for (int i = 0; s[i] != '\0'; i++) {
        mp[s[i] - 'a']++;
    }

    int vowel = 0, consonant = 0;
    for (char ch = 'a'; ch <= 'z'; ch++) {
        if (is_vowel(ch)) {
            vowel = fmax(vowel, mp[ch - 'a']);
        } else {
            consonant = fmax(consonant, mp[ch - 'a']);
        }
    }
    return vowel + consonant;
}