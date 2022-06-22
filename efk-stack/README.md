# Introduction to Fluentd

## Collecting logs from files

Reading logs from a file we need an application that writes logs to a file.  
Lets start one:

```sh
cd monitoring\logging\fluentd\introduction\

docker-compose up -d file-myapp

```

To collect the logs, lets start fluentd

```sh
docker-compose up -d fluentd
```

## Collecting logs over HTTP (incoming)

```sh
cd monitoring\logging\fluentd\introduction\

docker-compose up -d http-myapp

```
