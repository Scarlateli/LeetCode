int removeDuplicates(int* nums, int numsSize) {
    // Se o array tiver 2 ou menos elementos, não tem risco de ter mais de 2 iguais
    if (numsSize <= 2) return numsSize;

    // k vai marcar até onde já temos o array "limpo" (sem mais de 2 repetições)
    // Começa em 2 porque os dois primeiros elementos sempre podem ficar
    int k = 2;

    // Começamos do terceiro elemento (índice 2) e vamos até o final
    for (int i = 2; i < numsSize; i++) {
        // Só vamos copiar o número atual se ele for diferente do que está
        // duas posições atrás. Isso evita ter mais de 2 repetições.
        if (nums[i] != nums[k - 2]) {
            nums[k] = nums[i]; // Coloca o número na posição certa
            k++;               // Avança o tamanho válido
        }
        // Se for igual a nums[k-2], significa que já temos 2 desse número,
        // então ignoramos
    }

    // No final, k é a quantidade de elementos que ficaram no array "limpo"
    return k;
}