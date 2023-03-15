#include <stdio.h>


int main(void) {

    double res = 0;
    double score_sum = 0;

    for (int i = 0; i < 20; i++) {
        char name[50];
        char credit[5];
        double score;

        scanf("%s %lf %s", name, &score, credit);

        if (credit[0] == 'A') {
            res += score * (credit[1] == '+' ? 4.5 : 4.0);
        }
        else if (credit[0] == 'B') {
            res += score * (credit[1] == '+' ? 3.5 : 3.0);
        }
        else if (credit[0] == 'C') {
            res += score * (credit[1] == '+' ? 2.5 : 2.0);
        }
        else if (credit[0] == 'D') {
            res += score * (credit[1] == '+' ? 1.5 : 1.0);
        } 
        if (credit[0] != 'P') {
            score_sum += score;
        }

    }

    printf("%lf", res / score_sum);

}