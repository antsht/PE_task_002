#include <stdio.h>
#include <stdlib.h>

#include "pascal.h"

int main(void) {
    int pas_size_to_calc = -1;
    if (scanf("%d", &pas_size_to_calc) != 1 || !(pas_size_to_calc >= 1 && pas_size_to_calc <= MAXSIZE))
        puckxit();
    getchar();

    int pascal_triangle[MAXSIZE][MAXSIZE] = {0};
    fill_pascal_matrix(pascal_triangle, pas_size_to_calc);

    print_pascal_matrix_last_row(pascal_triangle, pas_size_to_calc);

    return 0;
}
