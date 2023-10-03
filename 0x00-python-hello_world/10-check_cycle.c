#include "lists.h"
/**
 * check_cycle - checks for cycles in singly linked list
 * @list: linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *snail, *cheetah;

	snail = list;
	cheetah = list->next;
	while (snail != cheetah)
	{
		if (cheetah == NULL || cheetah->next == NULL)
			return (0);
		snail = snail->next;
		cheetah = cheetah->next->next;
	}
	return (1);
}
