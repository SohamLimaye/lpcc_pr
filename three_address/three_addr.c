#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

// Structure to represent a token
typedef struct {
    char lexeme[MAX_SIZE];
    int token_type;
} Token;

// Token types
#define IDENTIFIER 1
#define OPERATOR 2
#define NUMBER 3
#define DELIMITER 4

// Function to get the next token from the input file
Token getNextToken(FILE *fp) {
    Token token;
    fscanf(fp, "%s", token.lexeme);

    if (strcmp(token.lexeme, "+") == 0 ||
        strcmp(token.lexeme, "-") == 0 ||
        strcmp(token.lexeme, "*") == 0 ||
        strcmp(token.lexeme, "/") == 0) {
        token.token_type = OPERATOR;
    } else if (strcmp(token.lexeme, ";") == 0) {
        token.token_type = DELIMITER;
    } else {
        // Assuming all other lexemes are identifiers or numbers
        // You may need to add more complex logic for real programs
        if (token.lexeme[0] >= '0' && token.lexeme[0] <= '9') {
            token.token_type = NUMBER;
        } else {
            token.token_type = IDENTIFIER;
        }
    }

    return token;
}

int main() {
    FILE *fp;
    fp = fopen("input.txt", "r");

    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    // Read tokens from the input file and generate three-address code
    Token token1, token2, token3, op;
    token1 = getNextToken(fp);
    op = getNextToken(fp);
    token2 = getNextToken(fp);
    token3 = getNextToken(fp);

    // Assuming the input file contains a single expression
    printf("Code:\n");
    printf("(%s, %s, %s, %s)\n", op.lexeme, token2.lexeme, token3.lexeme, token1.lexeme);

    fclose(fp);
    return 0;
}

