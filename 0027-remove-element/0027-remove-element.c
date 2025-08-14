int removeElement(int* nums, int numsSize, int val) {
    // integer array -> nums 
    // integer --> val
    // remover val em nums in place --> os numeros que entrarao na outra array sao diferentes de val
    // numeros diferentes --> K

    int k = 0;
    for(int i=0; i < numsSize; i++){
        if (nums[i] != val) {
            nums[k] = nums[i]; 
            k++;
        }
       
    }
    return k;


    
    
    
}