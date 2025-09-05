int makeTheIntegerZero(int num1, int num2) {
    int k = 1;
    
    // Loop infinito até encontrar solução ou determinar impossibilidade
    while (1) {
        // Calcula o resultado após k operações
        // Usa long long para evitar overflow
        long long x = (long long)num1 - (long long)num2 * k;
        
        // Se x < k, é impossível satisfazer a condição x >= k
        // Retorna -1 indicando que não há solução
        if (x < k) {
            return -1;
        }
        
        // Verifica se k >= número de bits 1 em x
        // __builtin_popcountll conta os bits 1 em um long long
        if (k >= __builtin_popcountll(x)) {
            return k;  // Encontrou a solução mínima
        }
        
        // Incrementa k e tenta novamente
        k++;
    }
}