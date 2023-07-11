#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to insert
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *a_node = *head, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
new->next = NULL;
if (a_node == NULL || a_node->n >= number)
{
new->next = a_node;
*head = new;
return (new);
}
while (a_node && a_node->next && a_node->next->n < number)
{
a_node = a_node->next;
}
new->next = a_node->next;
a_node->next = new;
return (new);
}
