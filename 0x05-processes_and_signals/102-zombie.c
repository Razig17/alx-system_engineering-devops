#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int infinite_while(void);
/**
 * infinite_while - Runs an infinite while loop
 *
 * Return: Always 0
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
 * main - Creates five zombie processes
 *
 * Return: Always 0
 */

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			sleep(1);
			exit(0);
		}
	}
	infinite_while();

	return (0);
}
