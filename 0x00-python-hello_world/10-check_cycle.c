#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *lion, *monkey;

	if (list == NULL || list->next == NULL)
		return (0);

	lion = list->next;
	monkey = list->next->next;

	while (lion && monkey && monkey->next)
	{
		if (lion  == monkey)
			return (1);

		lion = lion->next;
		monkey = monkey->next->next;
	}

	return (0);
}
