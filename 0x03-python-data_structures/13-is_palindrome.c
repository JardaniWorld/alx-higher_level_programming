#include "lists.h"

/**
 * is_palindrome - This function checks if a singly linked list
 * is a palindrome
 *
 * @head: specifies the start of the node
 * Return: Always 0. (Success)
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *temp = *head;
	int head_val, tail_val;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	head_val = (*head)->n;

	while (current)
	{
		if ((current->next)->next == NULL)
		{
			tail_val = (current->next)->n;
			current->next = NULL;

			if (head_val != tail_val)
				return (0);
			temp = temp->next;

			if (!temp)
				break;
			head_val = temp->n;
			current = temp;
		}
		else
			current = current->next;
	}
	return(1);
}
