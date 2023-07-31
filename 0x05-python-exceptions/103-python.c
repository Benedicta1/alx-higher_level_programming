#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
/**
 * print_python_bytes - This print python things
 * @p: This is a pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	size_t a, c;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *)(p))->ob_sval, a = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", a, str);
	a >= 10 ? a = 10 : a++;
	printf("  first %ld bytes: ", a);
	for (c = 0; c < a - 1; c++)
		printf("%02hhx ", str[c]);
	printf("%02hhx\n", str[c]);
}
/**
 * print_python_float - This print python things
 * @p: This is a pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
	char *str;
	double e;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	e = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(e, 'q', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_list -This  print python things
 * @p: This is a pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	size_t b, size, c;
	const char *t;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	b = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, b);
	for (c = 0; c < size; c++)
	{
		s = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", z, s);
		!strcmp(t, "bytes") ? print_python_bytes(list->ob_item[z]) : (void)s;
		!strcmp(t, "float") ? print_python_float(list->ob_item[z]) : (void)s;
	}
}
