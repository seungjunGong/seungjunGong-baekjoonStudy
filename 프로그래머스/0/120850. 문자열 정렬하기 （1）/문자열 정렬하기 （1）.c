#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int cmp(const int* a, const int* b) {
    return (*a - *b);
}

char* solution(const char* my_string) {
    int n = strlen(my_string);
    int* answer = NULL;    
    int j = 0;
    
    for (int i = 0; i < n; i++) {
        if (isdigit(my_string[i])) {
            answer = realloc(answer, sizeof(int) * (j + 1));
            answer[j] = my_string[i] - '0'; // 문자 -> 숫자로 바꾸는 방법 
            j++;
        }
    }
    
    qsort(answer, j, sizeof(int), cmp);
    
    return answer;
}