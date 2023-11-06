#include "lists.h"

/**
 * reverse_listint_recursive - this function reverses a linked list
 * @head: pointer first node to linked list
 *
 * Return: pointer to the first node in the new list
 */

void reverse_listint_recursive(listint_t **head)
{
   listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
  {
    next = current->next;
    current->next = prev;
    prev = current;
    current = next;
  }

  *head = prev;
}


/**
 * is_palindrome - checked linked list if it is a palindrome
 * @head: double pointer linked list
 *
 * Return: 1 if it is true, 0 if false
 */

int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (fast)
  {
    fast = fast->next;
    if (fast)
    {
      fast = fast->next;
      slow = slow->next;
    }
  }

  reverse_listint_recursive(&slow);

  dup = slow;

  while (dup && temp)
  {
    if (temp->n == dup->n)
    {
      dup = dup->next;
      temp = temp->next;
    }
    else
      return (0);
  }

  return (1);
}                                                                                   
