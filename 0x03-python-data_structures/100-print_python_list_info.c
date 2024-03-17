#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about lists in python
 *
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int ele;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (ele = 0; ele < Py_SIZE(p); ele++)
		printf("Element %d: %s\n", ele, Py_TYPE(PyList_GetItem(p, ele))->tp_name);
}
