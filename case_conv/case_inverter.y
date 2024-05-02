%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token LETTER NEWLINE

%%
input: /* empty */
     | input line
     ;

line: '\n'   { printf("\n"); }
    | expression '\n' { printf("\n"); }
    ;

expression: LETTER { printf("%c", $1); }
          | expression LETTER { printf("%c", $2); }
          ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}

