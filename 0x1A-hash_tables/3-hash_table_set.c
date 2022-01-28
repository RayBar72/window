#include "hash_tables.h"




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
    hash_node_t *new = NULL, *recorre = NULL;

    if (!ht || !key || !value || value[0] == '\0')
        return(0);
    /*Generando índice*/
    index = key_index((unsigned char *)key, ht->size);

    /*Buscando si nodo ocupado*/
    if (ht->array[index] == NULL)
    {
        /*Null: iguala valores del nodo*/
        ht->array[index]->key = strdup(key);
            if (!ht->array[index]->key)
                return (0);
        ht->array[index]->value = strdup(value);
        ht->array[index]->next = NULL;
        return (1); 
    }
    else
    {
        /*Crea malloc*/
        new = malloc(sizeof(new));
        if (!new)
            return (0);
        new->key = key;
        new->value = NULL;
        recorre = ht->array[index];
        while (recorre)
        {
            recorre->next = 
        }
        

        
    }




}