#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/select.h>
#include <stdio.h>
#include <string.h>


#define PORT 54321

int main(){
    int server_soc = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = INADDR_ANY;
    memset(&(addr.sin_zero), 0, 8);
    
    bind(server_soc, (struct sockaddr *) &addr, sizeof(struct sockaddr_in));

    if (listen(server_soc, 2) < 0){
        perror("listen");
        close(server_soc);
        exit(1);
    }

    struct sockaddr_in addr_in;
    addr_in.sin_family = AF_INET;
    memset(&(addr_in.sin_zero), 0, 8);
    unsigned int client_size = sizeof(struct sockaddr_in);

    int client_fd = accept(server_soc, (struct sockaddr *) &addr_in, &client_size);
    if (client_fd == -1){
        perror("accept");
        close(client_fd);
        exit(1);
    }

    write(client_fd, "hi from client \r\n", 17);

    return 0;

}