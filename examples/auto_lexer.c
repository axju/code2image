#include<stdio.h>
#include<time.h>
#include<windows.h>
#include <stdlib.h>

int main(){
  struct tm *tmp;
  time_t s;

  for(;;){
    s = time(NULL);
    tmp = localtime(&t);
    printf("%d:%0d:%d\n", tmp->tm_hour, tmp->tm_min, tmp->tm_sec);
    Sleep(1000);
    system ("cls");
  }

  return 0;
}
