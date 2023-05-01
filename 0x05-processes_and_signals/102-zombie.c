#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


/**
 * infinite_while - function that creates the infinite loop of the program
 * Return: Always zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - an entry point of a function to create 5 zombie processes
 * Return: Always zero
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: ZOMBIE_PID");
	}
	infinite_while();
	return (0);
}
