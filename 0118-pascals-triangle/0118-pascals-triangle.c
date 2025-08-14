/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int* returnSize, int** returnColumnSizes) {
    // O número de linhas que vamos retornar
    *returnSize = numRows;

    // Aloca o vetor que vai guardar o tamanho de cada linha
    *returnColumnSizes = malloc(numRows * sizeof(int));

    // Aloca o vetor de ponteiros para as linhas do triângulo
    int** triangle = malloc(numRows * sizeof(int*));

    for (int i = 0; i < numRows; i++) {
        // Tamanho da linha i é i+1
        (*returnColumnSizes)[i] = i + 1;

        // Aloca a linha
        triangle[i] = malloc((i + 1) * sizeof(int));

        // Primeiro e último elemento sempre 1
        triangle[i][0] = 1;
        triangle[i][i] = 1;

        // Preenche o meio da linha (se existir)
        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }

    return triangle;
}
