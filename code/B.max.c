#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max_weapon_strength(char *L, char *R) {
    int max_strength = 0;
    int min_length = strlen(L) < strlen(R) ? strlen(L) : strlen(R);
    
    for (int i = 0; i < min_length; i++) {
        int diff = abs(L[i] - R[i]);
        max_strength += diff;
    }
    
    if (strlen(L) > strlen(R)) {
        max_strength += atoi(L + min_length);
    } else if (strlen(R) > strlen(L)) {
        max_strength += atoi(R + min_length);
    }
    
    return max_strength;
}

int main() {
    int t;
    scanf("%d", &t);

    // Process each test case
    for (int i = 0; i < t; i++) {
        char L[105], R[105];
        scanf("%s %s", L, R);
        int result = max_weapon_strength(L, R);
        printf("%d\n", result);
    }

    return 0;
}
