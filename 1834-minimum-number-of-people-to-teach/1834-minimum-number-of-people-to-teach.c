int minimumTeachings(int n, int** languages, int languagesSize, int* languagesColSize, int** friendships, int friendshipsSize, int* friendshipsColSize) {
    int m = languagesSize;

    char *knows = (char*)calloc((size_t)(m + 1) * (n + 1), sizeof(char));
    for (int i = 0; i < m; i++) {
        for (int k = 0; k < languagesColSize[i]; k++) {
            int lang = languages[i][k];
            knows[(i + 1) * (n + 1) + lang] = 1;
        }
    }

    char *need = (char*)calloc(m + 1, sizeof(char));

    for (int i = 0; i < friendshipsSize; i++) {
        int u = friendships[i][0];
        int v = friendships[i][1];

        int share = 0;
        for (int k = 0; k < languagesColSize[u - 1] && !share; k++) {
            int lang = languages[u - 1][k];
            if (knows[v * (n + 1) + lang]) share = 1;
        }

        if (!share) {
            need[u] = 1;
            need[v] = 1;
        }
    }

    int ans = m;
    for (int L = 1; L <= n; L++) {
        int teach = 0;
        for (int u = 1; u <= m; u++) {
            if (need[u] && !knows[u * (n + 1) + L]) teach++;
        }
        if (teach < ans) ans = teach;
    }

    free(knows);
    free(need);
    return ans;


}