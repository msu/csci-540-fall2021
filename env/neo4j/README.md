# Neo4j

Build the neo4j server:

    $ docker build -t adv-db/neo4j .

Run the container. Notice that we don't specify the network on this one as we
will use the web browser.  Assume that we are running from the directory
containing this file:

    $ docker run \
        -p 7474:7474 -p 7687:7687 \
        -v ${PWD}/data:/data \
        -e NEO4J_AUTH=none  adv-db/neo4j

Open up your web browser to [http://localhost:7474](http://localhost:7474).

Run a simple query:

    MATCH (n) RETURN n;

Now we are all good.  Let's get to hacking!



