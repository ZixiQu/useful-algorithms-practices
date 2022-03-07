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

static char get_request[] =
    "GET /index.html HTTP/1.0\r\n"
    "Host: www-net.cs.umass.edu\r\n"
    "User-Agent: Firefox/3.6.10\r\n"
    "Accept: text/html,application/xhtml+xml\r\n"
    "Accept-Language: en-us,en;q=0.5\r\n"
    "Accept-Encoding: gzip,deflate\r\n"
    "Accept-Charset: ISO-8859-1,utf-8;q=0.7\r\n"
    "Keep-Alive: 115\r\n"
    "\r\n"
    "\n";


int main(){
    int client_soc = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server;
    
    server.sin_family = AF_INET;
    memset(&server.sin_zero, 0, 8);
    server.sin_port = htons(54321);

    struct addrinfo *result;
    getaddrinfo("127.0.0.1", NULL, NULL, &result);
    server.sin_addr = ((struct sockaddr_in *) result->ai_addr)->sin_addr;

    connect(client_soc, (struct sockaddr *)&server, sizeof(struct sockaddr_in));
    
    char buf[100];

    read(client_soc, buf, 100);
    buf[17] = '\0';
    printf("something%s \n", buf);
    
    fd_set fdset;
    buf[0] = '\0';

    FD_ZERO(&fdset);
    FD_SET(client_soc, &fdset);
    FD_SET(STDIN_FILENO, &fdset);

    int ready = select(client_soc + 1, &fdset, NULL, NULL, NULL);
    if (ready == -1){
        perror("select");\
        exit(1);
    }
    if (FD_ISSET(client_soc, &fdset)){
        int num_byte = read(client_soc, buf, MAXSIZE);
        write(STDIN_FILENO, get_request, 1000);   
    }
    else{
        printf("client socket is not ready\n");
    }
    buf[0] = '\0';


    return 0;
}