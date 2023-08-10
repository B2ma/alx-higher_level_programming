#include "hash_tables.h"

/**
  * hash_table_create - creates a hash table
  * @size: size of the array
  * Return: pointer to created hash table, Null otherwise
  */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table = NULL;
	hash_node_t **array = NULL;
	unsigned long int i;

	table = (hash_table_t*) malloc(sizeof(hash_table_t));
	if (table == NULL)
	{
		return (NULL);
	}
	array = (hash_node_t**)malloc(size * sizeof(hash_node_t*));
	if (array == NULL)
	{
		free (table);
		return (NULL);
	}
	table->size = size;
	table->array = array;

	for(i = 0; i < table->size; i++)
	{
		table->array[i] = NULL;
	}
	return table;
}
