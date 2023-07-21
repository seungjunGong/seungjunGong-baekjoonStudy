#include <stdio.h>

char rot13(char c)
{
    if ('A' <= c && 'Z' >= c)
        return 'A' + (c - 'A' + 13) % 26;
    else if ('a' <= c && 'z' >= c)
        return 'a' + (c - 'a' + 13) % 26;
    return c;
}

int main(void)
{
    char s[100];
    scanf("%[^\n]s", s);

    for (int i = 0; s[i] != '\0'; i++)
        printf("%c", rot13(s[i]));
    return 0;
}