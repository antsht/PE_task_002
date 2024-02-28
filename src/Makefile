BUILD_PATH=../bin/
CC=gcc
CFLAGS=-g -Wall -Wextra -Werror
EXTRAFLAGS=-fsanitize=leak -fsanitize=address -fsanitize=undefined -fsanitize=unreachable -fno-sanitize-recover -fstack-protector 

all: check rebuild

build: clean pascal_triangle pascal_matrix

rebuild: clean_all pascal_triangle pascal_matrix clean

pascal_triangle: clean pascal_triangle.c pascal.c 
	$(CC) $(CFLAGS) pascal_triangle.c pascal.c -o  $(BUILD_PATH)pascal_triangle 
	$(CC) $(CFLAGS) $(EXTRAFLAGS)  pascal_triangle.c pascal.c -o  $(BUILD_PATH)pascal_triangle_extra 

pascal_matrix: clean pascal_matrix.c pascal.c
	$(CC) $(CFLAGS) pascal_matrix.c pascal.c -o  $(BUILD_PATH)pascal_matrix 
	$(CC) $(CFLAGS) $(EXTRAFLAGS)  pascal_matrix.c pascal.c -o  $(BUILD_PATH)pascal_matrix_extra 

clean_all:
	rm -rf *.o *.a *.so $(BUILD_PATH)*
	
clean:
	rm -rf *.o *.a

check:
	clang-format -n *.c
#	clang-format -n *.h
	cppcheck --enable=all --suppress=missingIncludeSystem *.c *.h

run:
	valgrind --tool=memcheck --leak-check=yes --track-origins=yes $(BUILD_PATH)pascal_triangle
	valgrind --tool=memcheck --leak-check=yes --track-origins=yes $(BUILD_PATH)pascal_matrix

run_no_valgrind:
	$(BUILD_PATH)pascal_triangle_extra
	$(BUILD_PATH)pascal_matrix_extra



