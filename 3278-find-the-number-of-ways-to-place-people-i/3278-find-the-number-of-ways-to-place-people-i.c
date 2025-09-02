int numberOfPairs(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize; // leetcode passa isso mas eu não uso
    int n = pointsSize;
    int ans = 0; // contador de pares válidos

    // loop para escolher o primeiro ponto (A)
    for (int i = 0; i < n; ++i) {
        int xi = points[i][0];
        int yi = points[i][1];

        // loop para escolher o segundo ponto (B)
        for (int j = 0; j < n; ++j) {
            if (i == j) continue; // não pode ser o mesmo ponto

            int xj = points[j][0];
            int yj = points[j][1];

            // condição para A estar "upper-left" de B (ou na mesma linha/coluna):
            // A precisa estar à esquerda (ou igual no x) e acima (ou igual no y)
            if (xi <= xj && yi >= yj) {
                // defino os limites do retângulo/linha entre A e B
                int xmin = xi, xmax = xj;
                int ymin = yj, ymax = yi;

                int valido = 1; // assumo que é válido até achar um ponto bloqueando

                // checo todos os outros pontos (k) pra ver se algum está dentro do retângulo
                for (int k = 0; k < n; ++k) {
                    if (k == i || k == j) continue; // pulo os cantos

                    int xk = points[k][0];
                    int yk = points[k][1];

                    // se k cair dentro ou na borda do retângulo, então esse par (i,j) não serve
                    if (xmin <= xk && xk <= xmax && ymin <= yk && yk <= ymax) {
                        valido = 0;
                        break;
                    }
                }

                // se nenhum ponto bloqueou, conto esse par como válido
                if (valido) ans++;
            }
        }
    }

    return ans;
}
