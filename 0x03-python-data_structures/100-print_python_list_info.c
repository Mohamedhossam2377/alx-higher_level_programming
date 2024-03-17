#include <object.h>
#include <listobject.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about lists in python
 *
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PylistObject *)p;

	prinft("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
