#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has cycle in it
  * @list: pointer to the list
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	do
	{
		if (fast == NULL || fast->next == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
	} while (slow != fast);
	return (1);
}
