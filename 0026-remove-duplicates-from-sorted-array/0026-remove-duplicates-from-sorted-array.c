int removeDuplicates(int* nums, int numsSize) {
    // integer arry nums -> sorted non-decreasing order 
    // remove duplicates in place
    // unique elements of nums = k
    // i=1
    // k=1 --> nums[0]
    if(numsSize == 0) {
        return 0;
    }
    int k=0; // pointer k - unique elements
    for (int i=1; i < numsSize; i++) {
        if (nums[k] != nums[i]) {
            k++;
            nums[k] = nums[i]; // move o unique element para a proxima posiçao
        }
    }
    return k+1; // retorna o tamanho do array com os unique elements


    
}