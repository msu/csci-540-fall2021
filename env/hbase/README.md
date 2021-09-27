# HBase

HBase uses a lot of systems to work, so configuring it can be a bit of a pain.
To make things easier, I have created a set of scripts that make working with
the hbase container a little easier.  These scripts are located in the `bin`
directory.  Let's set things up!

## Building the hbase container

From the directory containing this file run the following commands

    $ cd docker
    $ docker build -t adv-db/hbase .

Building may take a bit as it has to download the hbase binary, but you should
see a status bar to let you know you are making progress.  Assuming all goes
well you will see an output similar to:

    Successfully built 39a6a670319f
    Successfully tagged adv-db/hbase:latest

## Interacting with the containers

First, we will start up hbase with the command

    $ ./bin/hbase-start

Next, lets test that everything started correctly by getting an interactive
shell (similar to the postgres client, but for hbase)

    $ ./bin/hbase-shell

If all goes well you should see some output and then

    hbase(main):001:0>

Run the command

    hbase(main):001:0> version
    1.2.6, rUnknown, Mon May 29 02:25:32 CDT 2017

If you see `1.2.6` we are in business!

Sometimes, you may need to see the logs from hbase.  The command
`./bin/hbase-logs` allows you to see more information about what is going on.

Once you are done, you can stop hbase by running the script

    $ ./bin/hbase-stop

It may take a minute, but the container should stop and clean up after itself.


