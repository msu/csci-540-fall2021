# adapted from
# https://hub.docker.com/r/adaminspace/hbase/~/dockerfile/
#
# Start with latest CentOS image
FROM centos:7

MAINTAINER David Millman david.millman@montana.edu

# Switch to root user
USER root

# Update yum
RUN yum update -y

# Install tar
RUN yum install -y tar

# Install java
RUN yum install -y java-1.7.0-openjdk-devel

## Install hbase from local
RUN mkdir /usr/local/hbase
ADD https://archive.apache.org/dist/hbase/1.2.6/hbase-1.2.6-bin.tar.gz /usr/local/hbase/
WORKDIR /usr/local/hbase
RUN tar -xvzf /usr/local/hbase/hbase-1.2.6-bin.tar.gz

# Set JAVA_HOME (used by HBase)
ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk

# Add hbase to path
ENV PATH /usr/local/hbase/hbase-1.2.6/bin:$PATH

# Insert config file from local
ADD hbase-site.xml /usr/local/hbase/hbase-1.2.6/conf/hbase-site.xml

# EXPOSE PORTS
# zookeeper
EXPOSE 2181

# hbase.master.port
EXPOSE 16000

# hbase.master.info.port (http)
EXPOSE 16010

# hbase.regionserver.port
EXPOSE 16020

# hbase.regionserver.info.port (http)
EXPOSE 16030

# hbase.rest.port
EXPOSE 8080

# install bzcat
RUN yum install -y bzip2

# Start HBase
CMD hbase master start
