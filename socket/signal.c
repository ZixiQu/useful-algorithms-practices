#include <stdio.h> 
#include <stdlib.h> 
#include <signal.h>
#include <unistd.h>


// 参考资料：http://c.biancheng.net/cpp/u/hs9/

int x = 0;
int num = 0;

void handler(int sig) {
	
	if (sig == SIGTERM)
	{
		x++;
	}

    fprintf(stdout, 
    	"signal %d has been handle... x is %d\n", 
    	sig, x);

    if (x > 5)
    {
    	signal(SIGTERM, SIG_DFL); // 恢复默认处理方式
    }
    

}

void handler2(int sig) {
	num++;
    fprintf(stdout, 
    	"get alarm signal ... num is %d\n", num);
    //alarm(5);
    
}


int main(int argc, char const *argv[])
{
	// SGIGKILL 和 SIGSTOP 不能被篡改

	// kill(pid, sig) // 向指定线程 传递指定 信号

	// alarm(time) // 有间隔的传递信号

	// pause() // 让线程停止，直到收到信号,恢复运行（不抵消信号）

	// sigaction
	// 有一种结构体 叫做 sigaction
	// struct sigaction act
	// act.sa_handler 存储 handler函数
	// act.sa_flags 在处理信号时，某些其他的操作，默认0
	// act.sa_mask 存储一个信号的集合，表示在信号处理时，搁置的信号

	struct sigaction act;
    act.sa_handler = handler;
    act.sa_flags = 0;
    sigemptyset(&act.sa_mask);  // 初始化，让 act.sa_mask 存储空集合


	// 有一个函数 叫做 sigaction
	// sigaction(SIGINT,&act,&oldact);
	// 对指定信号，绑定指定的行为模式。旧有的行为模式，会被存入oldact指针

    sigaction(SIGINT, &act, NULL);


	signal(SIGTERM, *handler);

	// signal(SIGTERM, SIG_IGN); // 无视指定信号

	
	// alarm(5);	

	printf("parent pid is %d\n", getpid());

	// for (;;)
	// {
	// 	sleep(2);

	// 	printf("wait...singal....\n");
		
	// }



	int pid = fork();
	if (pid == 0)
	{	
		signal(SIGALRM, *handler2);
		pause();
		for (;;)
		{
			sleep(2);
			printf("wait...singal....\n");	
		}

		exit(0);
	}


	printf("child pid is %d\n", pid);
	for (;;)
	{
		sleep(5);
		kill(pid,SIGALRM);
	}



	return 0;
}