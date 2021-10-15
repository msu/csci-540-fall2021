# MongoDB

Build the mongo server:

    $ docker build -t adv-db/mongo .

Run the container

    $ docker run --net=host -p 27017:27017 adv-db/mongo

Note, you will likely need to update the clients image, which we built the
first week of class.  In the file "../client/Dockerfile" change the line:

    RUN apt-get install -y \
        postgresql-client

To

    RUN apt-get install -y \
        postgresql-client \
        mongodb-clients

(Be sure to not forget the '\' at the end of the line for the postgres client)

Assuming that you have built the client, we can get a mongo shell to work with
the `my-addb-database` database by running the following command:

    $ docker run --net=host -it adv-db/clients mongo my-advdb-database

We can make sure all went okay by issuing the following commands in the mongo
shell

    > db.test.insert({ hello: "world!" })
    > show collections
    test
    > db.test.find()
    { "_id" : ObjectId("5d7f14f7fdca980a8c073775"), "hello" : "world!" }

Now we are all good.  Let's get to hacking!


