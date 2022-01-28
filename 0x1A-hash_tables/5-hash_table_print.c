#include "hash_tables.h"
/**
 * hash_table_print - function that prints a hash table
 * @:ht pointer
 */

void hash_table_print(const hash_table_t *ht)
{
	unsigned long int i = 0;
	hash_node_t *aimprimir = 0;
	int passed = 0;
	if (!ht)
		return;
	printf("{");
	for (i = 0; i < ht->size; i++)
	{
		aimprimir = ht->array[i];
		while (aimprimir)
		{
			if (passed)
				printf(",");
			printf("'%s': '%s'", aimprimir->key, aimprimir->value);
			passed = 1;
			aimprimir = aimprimir->next;
		}
	}
	printf("}\n");	
}
