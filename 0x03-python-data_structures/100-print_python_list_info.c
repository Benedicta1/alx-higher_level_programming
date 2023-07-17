#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - This prints info about python lists
 * @p: This is the address of pyobject struct
 */
void print_python_list_info(PyObject *p)
{
	int a;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (a = 0; a < Py_SIZE(p); a++)
		printf("Element %d: %s\n", a, Py_TYPE(PyList_GetItem(p, a))->tp_name);
}
