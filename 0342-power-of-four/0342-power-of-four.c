bool isPowerOfFour(int n) {
    // n > 0, potência de 2, e posição do bit único é par
    return (n > 0) &&
           (n & (n - 1)) == 0 &&     // garante que é potência de 2
           (n & 0x55555555) != 0;    // garante que está em posição par

}