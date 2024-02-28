#ifndef PASCAL_H
#define PASCAL_H

#define MAXSIZE 30
#define MAXSIZETOFILL 10

void puckxit();
void fill_pascal_matrix(int pascal_matrix[MAXSIZE][MAXSIZE], int pas_size_to_calc);
void print_matrix(int matrix[MAXSIZETOFILL][MAXSIZETOFILL], int pas_size_to_calc);
void print_pascal_matrix_last_row(int pascal_matrix[MAXSIZE][MAXSIZE], int pas_size_to_calc);

#endif