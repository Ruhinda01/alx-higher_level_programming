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
	cheetah = list;
	while (snail != NULL && cheetah != NULL && cheetah->next != NULL)
	{
		snail = snail->next;
		cheetah = cheetah->next->next;
		if (snail == cheetah)
			return (1);
	}
	return (0);
}
