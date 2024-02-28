#include <stdio.h>
#include <stdlib.h>

#include "pascal.h"

int main(void) {
    int pas_size_to_calc = 0;
    int size_to_fill = -1;
    if (scanf("%d", &size_to_fill) != 1 || !(size_to_fill >= 1 && size_to_fill <= MAXSIZETOFILL)) puckxit();
    getchar();

    int pascal_triangle[MAXSIZE][MAXSIZE] = {0};
    int pascal_matrix[MAXSIZETOFILL][MAXSIZETOFILL] = {0};
    while (pas_size_to_calc * (pas_size_to_calc + 1) < 2 * size_to_fill * size_to_fill) {
        pas_size_to_calc++;
    }
    fill_pascal_matrix(pascal_triangle, pas_size_to_calc);

    int curr_index = 0;
    for (int i = 0; i < pas_size_to_calc; i++)
        for (int j = 0; j < pas_size_to_calc; j++) {
            if (pascal_triangle[i][j] != 0) {
                pascal_matrix[curr_index / size_to_fill][curr_index % size_to_fill] = pascal_triangle[i][j];
                curr_index++;
            }
        }

    print_matrix(pascal_matrix, size_to_fill);

    return 0;
}
