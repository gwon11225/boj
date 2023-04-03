#include <stdio.h>

int main(){
  
  char s[100] = { 0 };
  scanf("%s", s);
  
  for(int i = 'a'; i <= 'z'; i++){
    for(int j = 0; j < 100; j++){
      if(i == s[j]){
        printf("%d ", j);
        break;
      }
      if(j == 99){
        printf("-1 ");
      }
    }
  }
    
}