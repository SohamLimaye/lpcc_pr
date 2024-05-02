%{
#include <stdio.h>
%}

%%

"{"                 { printf("<LEFT_BRACE>\n"); }
"}"                 { printf("<RIGHT_BRACE>\n"); }
"char"              { printf("<KEYWORD_CHAR>\n"); }
"="                 { printf("<ASSIGN_OP>\n"); }
"printf"            { printf("<PRINTF_FUNC>\n"); }
"("                 { printf("<LEFT_PAREN>\n"); }
")"                 { printf("<RIGHT_PAREN>\n"); }
";"                 { printf("<SEMICOLON>\n"); }
\"[^\"]*\"          { printf("<STRING_LITERAL>\n"); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("<IDENTIFIER>\n"); }
[ \t\n]+            { /* Ignore whitespace */ }
.                   { printf("<INVALID_CHARACTER>\n"); }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}

