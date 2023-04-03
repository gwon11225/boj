#include <iostream>

using namespace std;

int main()
{
    char word[101];
    cin >> word;
    int a = 0;
    int count = 0;
    while(word[a] != 0){
        if((word[a] == 'c') && (word[a+1] == '=')){
            count++;
            a += 2;
            continue;
        }
        else if((word[a] == 'c') && (word[a+1] == '-')){
            count++;
            a += 2;
            continue;
        }
        else if((word[a] == 'd' && word[a+1] == 'z') && (word[a+2] == '=')){
            count++;
            a += 3;
            continue;
        }
        else if((word[a] == 'd') && (word[a+1] == '-')){
            count++;
            a += 2;
            continue;
        }
        else if((word[a] == 'l') && (word[a+1] == 'j')){
            count++;
            a += 2;
            continue;
        }
        else if((word[a] == 'n') && (word[a+1] == 'j')){
            count++;
            a += 2;
            continue;
        }
        else if((word[a] == 's') && (word[a+1] == '=')){
            count++;
            a += 2;
            continue;
        }
        else if((word[a] == 'z') && (word[a+1] == '=')){
            count++;
            a += 2;
            continue;
        }
        else{
            count++;
            a++;
        }
    }
    cout << count;
}