#include <stdio.h>

int main(void)
{
    char words[101] = {'\0'};
    scanf("%s", words);

    int i = 0;
    while (words[i] != '\0')
    {
        printf("%c", (int)words[i] < 97 ? words[i] + 32 : words[i] - 32);
        i++;
    }

    return 0;
}