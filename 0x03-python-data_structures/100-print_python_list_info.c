#include "listobject.h"
#include "object.h"
void print_python_list_info(PyObject *p)
{
	int a, b;

	b = PyList_Size(p)
	for (a = 0 ; a < b ; a++)
		printf("[*] Size of the Python List = %d", b);
}
