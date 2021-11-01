# Redis setup

Rebuild the clients container.  For the repo root run

    docker build -t adv-db/clients env/client/

Build the Redis container.

    docker build -t adv-db/redis .

Run the redis container.

    docker run --net=host -p 6379:6379 adv-db/redis

And Run the client

    docker run --net=host -v ${PWD}/env/redis/mnt:/mnt/ -it adv-db/clients redis-cli

From the `redis-cli` make sure all is working:

    127.0.0.1:6379> PING
    PONG

Now we are all good.  Let's get to hacking!


