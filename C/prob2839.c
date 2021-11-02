#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(){
    int input;
    int cnt = 0;

    scanf("%d", &input);

    while(input > 0){
        if (input % 5 == 0){
            input -= 5;
            cnt++;
        } else if (input % 3 == 0) {
            input -= 3;
            cnt++;
        } else if (input > 5) {
            input -= 5;
            cnt++;
        } else {
            cnt = -1;
            break;
        }
    }
    printf("%d", cnt);
    return 0;
}
