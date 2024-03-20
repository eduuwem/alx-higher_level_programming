#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size;
	int b;
	char *byte_data = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &byte_data, &size);

	printf("  size: %li\n", size);
	printf("  byte data: %s\n", byte_data);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (b = 0; b <= size && b < 10; b++)
		printf(" %02hhx", trying_str[b]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int b;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (b = 0; b < size; b++)
        {
                type = (list->ob_item[b])->ob_type->tp_name;
		printf("Element %i: %s\n", b, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[bb]);
        }
}

