#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to head pointer
  * Return: 1, 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reverse = NULL;

	if (head == NULL || *head == NULL)
		return (0);
	while (current != NULL)
	{
		add_nodeint_end(&reverse, current->n);
		current = current->next;
	}
	current = *head;
	while (current != NULL && reverse != NULL)
	{
		if (current->n != reverse->n)
			return (0);
		current = current->next;
		reverse = reverse->next;
	}
	return (1);
}
