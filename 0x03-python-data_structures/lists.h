#ifndef LISTS_H
#define LISTS_H

#include <unistd.h>

/**
 * struct listint_s - This is a singly linked list
 * @n: This is an integer
 * @next: This points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
int pal(listint_t **start, listint_t *end);

#endif /* LISTS_H */
