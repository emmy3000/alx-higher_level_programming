#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/*
* C function that prints some basic info about Python lists.
*
* The size of the list using PyList_Size
* The amount of memory that has been allocated to the list using ((PyListObject *)p)->allocated
* For each element in the list:
* (1) The type of the object using item->ob_type->tp_name
* (2) The size of the object using Py_SIZE(item)
*
*/

void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);

	PyObject *item;
	PyTypeObject *type;
	int i, size_object;

	// Cast to PyListObject to access the "allocated" field
	PyListObject *list = (PyListObject *) p;
	int allocated = list->allocated;
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = item->ob_type;
		printf("Element %d: %s\n", i, type->tp_name);
		size_object = (int)Py_SIZE(item);
		printf("Element %d: %d\n", i, size_object);
	}
}
