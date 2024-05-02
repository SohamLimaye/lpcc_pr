%{
#include <stdio.h>
%}

%option noyywrap

%%

[ \t\n]+              ; // Ignore whitespace and newlines
[a-zA-Z]+             { printf("Word: %s\n", yytext); } // Identify words

[,.?!;:]              { printf("Punctuation: %s\n", yytext); } // Identify punctuation
is|am|are|was|were    { printf("Verb: %s\n", yytext); } // Identify verbs
a|an|the             { printf("Article: %s\n", yytext); } // Identify articles
cat|dog|house        { printf("Noun: %s\n", yytext); } // Identify nouns
big|small|red        { printf("Adjective: %s\n", yytext); } // Identify adjectives
quick|slow|lazy      { printf("Adverb: %s\n", yytext); } // Identify adverbs
and|or|but           { printf("Conjunction: %s\n", yytext); } // Identify conjunctions

.                     { printf("Unknown: %s\n", yytext); } // Identify unknown tokens

%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    yyin = input_file;
    yylex();

    fclose(input_file);
    return 0;
}

