bool hasIncreasingSubarrays(int* nums, int numsSize, int k) {
    int cnt = 1, precnt = 0, ans = 0;
    for (int i = 1; i < numsSize; ++i){
        if(nums[i] > nums[i-1]){
            ++cnt;
        } else {
            precnt = cnt;
            cnt = 1;
        }
        ans = fmax(ans, fmin(precnt,cnt));
        ans = fmax(ans, cnt / 2);
    }
    return ans >=k;
}