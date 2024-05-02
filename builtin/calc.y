%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
%}

%union {
    int num;
    char *func;
}

%token <num> NUM
%token <func> FUNC

%%

stmt_list: stmt_list stmt
         | stmt
         ;

stmt: expr '\n'    { printf("Result: %d\n", $1); }
    | '\n'          { ; }
    ;

expr: NUM           { $$ = $1; }
    | FUNC '(' expr ')' { 
        if(strcmp($1, "sqrt") == 0)
            $$ = sqrt($3);
        else if(strcmp($1, "abs") == 0)
            $$ = abs($3);
        // Add more functions here
    }
    | expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { 
        if($3 == 0) {
            fprintf(stderr, "Division by zero\n");
            exit(1);
        }
        $$ = $1 / $3; 
    }
    | '(' expr ')'  { $$ = $2; }
    ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    exit(1);
}

