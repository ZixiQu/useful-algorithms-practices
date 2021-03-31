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

int main(){
    int client_soc = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server;
    
    server.sin_family = AF_INET;
    memset(&server.sin_zero, 0, 8);
    server.sin_port = htons(54321);

    struct addrinfo *result;
    getaddrinfo("142.1.46.85", NULL, NULL, &result);
    server.sin_addr = ((struct sockaddr_in *) result->ai_addr)->sin_addr;

    connect(client_soc, (struct sockaddr *)&server, sizeof(struct sockaddr_in));
    
    char buf[100];

    read(client_soc, buf, 100);
    buf[17] = '\0';
    printf("information from server: %s\n", buf);

    // write();
}