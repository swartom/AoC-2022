#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILE "input.txt"

int main()
{

    FILE *f = fopen(INPUT_FILE, "rb");
    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);

    char *lines = malloc(fsize + 1);
    fread(lines, fsize, 1, f);
    printf("%s",lines);

    
    fclose(f);
}