#include "lists.h"

/**
 * insert_node - This nserts a number into a sorted singly-linked list.
 * @head: This reps the pointer to the head of the linked list.
 * @number: This is the  number to insert.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->a = number;

	if (node == NULL || node->a >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->a < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
