int maximum69Number (int num) {
    //Converte o número em string (9669 → "9669"). (%d)
    //Troca o primeiro 6 encontrado por 9.
    //Converte de volta para número inteiro. (atoi)
    //Retorna o maior número possível.
    
    char s[12];
    snprintf(s, sizeof(s), "%d", num);
    for (int i = 0; s[i]; i++) {
        if (s[i] == '6') { s[i] = '9'; break; }
    }
    return atoi(s);
}
