%{
#include "y.tab.h"
%}

%%
[0-9]+      { yylval.num = atoi(yytext); return NUM; }
[a-zA-Z]+   { yylval.func = strdup(yytext); return FUNC; }
[-+*/()=]   { return yytext[0]; }
[ \t\n]     ; /* skip whitespace */
.           { yyerror("Invalid character"); }

%%

int yywrap() {
    return 1;
}

