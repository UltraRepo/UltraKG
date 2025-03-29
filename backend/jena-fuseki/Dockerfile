FROM openjdk:17
RUN curl -O https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-4.8.0.tar.gz  && tar -xzf apache-jena-fuseki-*.tar.gz  && mv apache-jena-fuseki-* /jena-fuseki
WORKDIR /jena-fuseki
EXPOSE 3030
CMD ["./fuseki-server"]
