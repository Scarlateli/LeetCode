#include <stdlib.h>

typedef struct Node {
    int key;
    int idx;
    struct Node* next;
} Node;

static int hashFunc(int key, int cap) {
    long long k = key;
    if (k < 0) k = -k;
    return (int)(k % cap);
}

static Node** newBuckets(int cap) {
    return (Node**)calloc(cap, sizeof(Node*));
}

static Node* findInBucket(Node* head, int key) {
    for (Node* cur = head; cur != NULL; cur = cur->next) {
        if (cur->key == key) return cur;
    }
    return NULL;
}

static void insertInBucket(Node** buckets, int cap, int key, int idx) {
    int h = hashFunc(key, cap);
    Node* n = (Node*)malloc(sizeof(Node));
    n->key = key;
    n->idx = idx;
    n->next = buckets[h];
    buckets[h] = n;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));
    int cap = numsSize * 2 + 1;
    Node** buckets = newBuckets(cap);

    for (int i = 0; i < numsSize; i++) {
        int need = target - nums[i];
        int h = hashFunc(need, cap);
        Node* hit = findInBucket(buckets[h], need);
        if (hit) {
            result[0] = hit->idx;
            result[1] = i;
            free(buckets);
            return result;
        }
        insertInBucket(buckets, cap, nums[i], i);
    }

    *returnSize = 0;
    free(result);
    free(buckets);
    return NULL;
}
