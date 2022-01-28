#include "hash_tables.h"

/**
 * hash_table_create - function that creates a hash table
 * @size: size of the array
 * Return: pointer to new hash table or NULL
 */

hash_table_t *hash_table_create(unsigned long int size)
{

	hash_table_t *table = NULL;
	unsigned long int i = 0;

	if (size < 1)
		return (NULL);
	table = malloc(sizeof(*table));
	if (!table)
		return (NULL);
	table->array = malloc(sizeof(table->array) * size);
	if (!table->array)
	{
		free(table);
		return (NULL);
	}
	table->size = size;
	for (i = 0; i < size; i++)
		table->array[i] = NULL;
	return (table);
}
