#include  <stdio.h>#include <string.h>#include  <stdlib.h>#include  <sys/types.h>#include  <sys/stat.h>#include  <fcntl.h>#include  <unistd.h>int main(int argc, char **argv){    int rc = (1024*1024*10);    char *ptr_buf;    int i4Loop;    int i4LoopMax = 10;    int i4Delay = 5;  /* Seconds. */    ptr_buf = malloc(rc);    for( i4Loop = 0; i4Loop < i4LoopMax; i4Loop++) {      memset(ptr_buf, i4Loop, rc);      printf("%s: Proc %s Init %d: %d Bytes\n", argv[0], argv[1], (i4Loop+1), rc);      sleep(i4Delay);    }    free(ptr_buf);    return 0;}