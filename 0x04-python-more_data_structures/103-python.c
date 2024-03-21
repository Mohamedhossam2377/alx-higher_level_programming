#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print some basic info about Python lists
 *
 * @p: a Pyobject list object
 */
void print_python_list(PyObject *p)
{
	int s, allo, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size;
	allo = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", allo);

	for (i = 0; i < s; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}

}

/**
 * print_python_bytes - print basic info about python byte objects
 *
 * @p: a Pyobject byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, s;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", s);
	for (i = 0; i < s; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}
