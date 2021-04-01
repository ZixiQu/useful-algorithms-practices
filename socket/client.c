#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/select.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>

#define PORT 54321
#define MAXSIZE 100

int main(){
    int client_soc = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server;
    
    server.sin_family = AF_INET;
    memset(&server.sin_zero, 0, 8);
    server.sin_port = htons(54321);

    struct addrinfo *result;
    getaddrinfo("192.168.0.14", NULL, NULL, &result);
    server.sin_addr = ((struct sockaddr_in *) result->ai_addr)->sin_addr;

    connect(client_soc, (struct sockaddr *)&server, sizeof(struct sockaddr_in));
    
    char buf[100];

    read(client_soc, buf, 100);
    buf[17] = '\0';
    printf("something%s \n", buf);
    
    fd_set fdset;
    buf[0] = '\0';
    while (1){
        FD_ZERO(&fdset);
        FD_SET(client_soc, &fdset);
        FD_SET(STDIN_FILENO, &fdset);

        int ready = select(client_soc + 1, &fdset, NULL, NULL, NULL);
        if (ready == -1){
            perror("select");\
            exit(1);
        }
        if (FD_ISSET(STDIN_FILENO, &fdset)){
            int num_byte = read(STDIN_FILENO, buf, MAXSIZE);
            write(client_soc, buf, num_byte);
        }
        if (FD_ISSET(client_soc, &fdset)){
            int num_byte = read(client_soc, buf, MAXSIZE);
            write(STDIN_FILENO, buf, num_byte);   
        }
        buf[0] = '\0';
    }

    return 0;
}