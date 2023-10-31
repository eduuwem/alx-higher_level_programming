#include "lists.h"

/**
 * insert_add_node - inserts a number into a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * # Author - Tolulope Fakunle
 * Return: address of the new element or NULL if it fails
 */
listint_t insert_add_node(listint_t **head, int n)
{
	listint_t *node = *head, *new;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
        	return (NULL);
	new->n = n;

	if (node == NULL || node-> n >= n)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < n)
		node = node->next;
	
	new->next = node->next;
	node->next = new;

	return (new);
}
