#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* reverse_listint - Reverses a singly-linked listint_t list.
* @head: A pointer to the starting node of the list to reverse.
*
* Return: A pointer to the head of the reversed list.
*/
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
* Return: 1, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (0);
listint_t *slow = *head, *fast = *head, *prev_slow = *head;
listint_t *mid = NULL;
int result = 1;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow, slow = slow->next;
}
if (fast != NULL)
{
mid = slow;
slow = slow->next;
}
prev_slow->next = NULL;
reverse_listint(&slow);
listint_t *temp1 = *head, *temp2 = slow;
while (temp1 != NULL && temp2 != NULL)
{
if (temp1->n != temp2->n)
{
result = 0;
break;
}
temp1 = temp1->next;
temp2 = temp2->next;
}
reverse_listint(&slow);
if (mid != NULL)
{
prev_slow->next = mid;
mid->next = slow;
}
else
{
prev_slow->next = slow;
}
return (result);
}
