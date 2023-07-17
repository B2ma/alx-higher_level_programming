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
listint_t *slow = *head, *fast = *head;
listint_t *previous = NULL, *temp = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (0);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next, temp = slow, slow = slow->next;
}
if (fast != NULL)
slow = slow->next;
if (slow != NULL && slow->next == NULL && slow->n != (*head)->n)
return (0);
while (slow != NULL)
{
temp = slow->next;
slow->next = previous;
previous = slow, slow = temp;
}
slow = *head;
while (previous != NULL)
{
if (slow->n != previous->n)
{
is_palindrome = 0;
break;
}
slow = slow->next, previous = previous->next;
}
previous = NULL;
while (*head != NULL)
{
temp = (*head)->next;
(*head)->next = previous;
previous = *head, *head = temp;
}
*head = previous;
return (is_palindrome);
}
