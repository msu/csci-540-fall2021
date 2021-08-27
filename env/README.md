# Setting up your environment

In the first part of the semester, we will get some hands on experience with
multiple NoSQL systems.  To avoid some of the challenges in running on multiple
environments, I will (hopefully) be able to provide you with a set of containers
that you can run on your system.

This document will help you get setup and going.  Install docker for your
environment [see install docs](https://docs.docker.com/install/).

If you are running a version of Windows that does not meet the minimal
requirements of docker, then you may have to use docker toolbox. See the [docker
windows installation
directions](https://docs.docker.com/toolbox/toolbox_install_windows/).

## Setting up the client

Note, I am planning on building one container called client that contains most
of the clients for interacting with the database (but we will see how that
goes). The client container will change throughout the semester so you may need
to rebuild it periodically.  To build the client:

    cd client
    docker build -t adv-db/clients .

## Setting up Postgres

Building is similar to other containers:

    cd postgres
    docker build -t adv-db/postgres .

And to run the container

    docker run --net=host -p 5432:5432 adv-db/postgres

Assuming that you have built the client, we can get a psql shell by running the
following commands

    docker run --net=host -it adv-db/clients psql -h localhost -U postgres postgres

To make sure everything worked, in the clients shell run a few "erronius" commands
that produce an error and you should see error messages in the adv-db/postgres
container. For example when I run

    postgres=# not-a-command;

I see the following error in the container running postgres

    2019-08-28 02:07:14.921 UTC [64] STATEMENT:  not-a-command;

You should be good to go!

## Setting up hbase

Check out the README.md in the hbase directory

## Tips

You may want to access files from your local machine in the client container,
which is the work flow that I was using during my demos in class.  To access
content from the host machine in a container, we will need to link a directory
on the host with the container.  We can link the directory with the `-v` option.
For example, if I wanted to link the directory `/home/dlm/adv-db` on my host
machine with `/mnt/` in the container I would run

    docker run --net=host -v /home/dlm/adv-db:/mnt/ \
        -it adv-db/clients bash

This will start a bash shell in the container.  If you navigate over to `/mnt`
in the container, you will see the contents of `/home/dlm/adv-db`!

**Pro Tip**: You can even use a sub-shell to mount the current
directory.  So, in class, when I am working on a file locally and then running
the script though postgres in the container, I was running

    docker run --net=host -v $(pwd):/mnt/ \
        -it adv-db/clients \
        psql -h localhost -U postgres -d advdb -f /mnt/day1.sql


