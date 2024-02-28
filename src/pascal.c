#include "pascal.h"

#include <stdio.h>
#include <stdlib.h>

void puckxit() {
    fprintf(stderr, "Puck you, Verter!");
    exit(EXIT_FAILURE);
}

void fill_pascal_matrix(int pascal_matrix[MAXSIZE][MAXSIZE], int pas_size_to_calc) {
    for (int i = 0; i < pas_size_to_calc; i++) {
        pascal_matrix[i][0] = 1;
        pascal_matrix[i][i] = 1;
    }
    if (pas_size_to_calc > 2) {
        for (int i = 2; i < pas_size_to_calc; i++) {
            for (int j = 1; j < i; j++) {
                pascal_matrix[i][j] = pascal_matrix[i - 1][j - 1] + pascal_matrix[i - 1][j];
            }
        }
    }
}

void print_matrix(int matrix[MAXSIZETOFILL][MAXSIZETOFILL], int pas_size_to_calc) {
    for (int i = 0; i < pas_size_to_calc; i++) {
        for (int j = 0; j < pas_size_to_calc; j++) {
            printf("%d", matrix[i][j]);
            if (j != pas_size_to_calc - 1) printf(" ");
        }
        if (i != pas_size_to_calc - 1) printf("\n");
    }
}

void print_pascal_matrix_last_row(int pascal_matrix[MAXSIZE][MAXSIZE], int pas_size_to_calc) {
    for (int j = 0; j < pas_size_to_calc; j++) {
        printf("%d", pascal_matrix[pas_size_to_calc - 1][j]);
        if (j != pas_size_to_calc - 1) printf(" ");
    }
}
