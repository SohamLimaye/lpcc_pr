%{
#include <stdio.h>
%}

%token LOWER UPPER

%%

input: /* empty */
     | input line
     ;

line: '\n'
    | UPPER
    | LOWER
    ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 0;
}

int yylex() {
    int c = getchar();
    if (c == EOF)
        return 0;
    if (c >= 'a' && c <= 'z') {
        yylval = c - 'a' + 1;
        return LOWER;
    }
    if (c >= 'A' && c <= 'Z') {
        yylval = c - 'A' + 1;
        return UPPER;
    }
    return c;
}

