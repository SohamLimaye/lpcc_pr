%{
#include "y.tab.h"
%}

%%
[a-z]   { return yytext[0]; }
[A-Z]   { return yytext[0] + 32; }
\n      { return yytext[0]; }
.       { return yytext[0]; }

int yywrap() {
    return 1;
}

