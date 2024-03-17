#include "lists.h"

/**
 * is_palindrome - check if palind or not
 *
 * @head: head for list
 *
 * Return: 0 if it is not a palind
 * 1 if it is a palind
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - to know if is a palind
 *
 * @head: head for list
 * @end: end for list
 *
 * Return: 0 if not palind and 1 if is palind
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
