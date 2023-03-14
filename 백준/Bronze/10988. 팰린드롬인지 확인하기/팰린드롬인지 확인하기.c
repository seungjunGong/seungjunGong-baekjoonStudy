#include <stdio.h>
#include <string.h>

int main(void){


    char word[100];

    scanf("%s", word);

    int i = 0, end = strlen(word), res = 1;

    while (i < (int)end / 2){
        if (word[i] != word[end - 1 - i]){
            res = 0;
        }
        i++;
    }

    printf("%d", res);
}