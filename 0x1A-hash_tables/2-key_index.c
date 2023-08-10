#include "hash_tables.h"
/**
  * key_index - gives the index of a key.
  * @key: the key
  * @size: size of the array of the hash table
  * Return:index at which key/value pair should be stored in hash table array
  */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int hash_value = hash_djb2(key);
	unsigned long int index = hash_value % size;

	if (index >= size)
	{
		index = index % size;
	}
	return (index);
}
