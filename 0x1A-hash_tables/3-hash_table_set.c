#include "hash_tables.h"

/**
 * search_node - looks at hash ind. post for the existence
 * of node
 * 
 * @head: pointer to positiones
 * @key: of the node
 * @Return - pointer or string
 */
static hash_node_t *search_head(hash_node_t *head, char *key)
{
	while ((head))
	{
		if (strcmp(head->key, key))
			head = head->next;
		else
			return (head);		
	}
	return (NULL);
}


/**
 * set_node - Set the node object
 * @head: pointer to pointer
 * @key: key of the node
 * @value: value of node var
 * Return: pointer if success or NULL
 */
static hash_node_t *node_setting(hash_node_t **head, char *key, char *value)
{
	hash_node_t *new = malloc(sizeof(new));

	if (!new)
		return (NULL);
	new->key = key;
	new->value = value;
	new->next = *head;
	*head = new;
	return (new);
}



/**
 * hash_table_set - Function that adds an element to the hash table
 * @ht: hash table to be added or updated 
 * @key: key value 
 * @value: string 
 * Return: Success 1, other wise 0 
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int index = 0, counter = 0;
	hash_node_t *new = NULL, *search = NULL;
	char *var = NULL, *key_resp = NULL;

	if (!ht || !key || !value || value[0] == '\0')
		return(0);
	/*valor a introducir si lugar en lista está vacío*/
	var = strdup(value);
	if (!value)
		return (0);
	/*Generando índice*/
	index = key_index((unsigned char *)key, ht->size);
	/*Buscando si nodo ocupado*/
	search = search_head(ht->array[index], (char *)key);
	if (search)
		search->value = var;
	else
	{
		key_resp = strdup(key);
		if (!key_resp)
		{
			free(var);
			return (0);
		}
		search = node_setting(&(ht->array[index]), key_resp, var);
		if (!search)
		{
			free(key_resp);
			free(var);
			return (0);
		}
	}
}