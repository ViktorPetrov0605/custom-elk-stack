FROM docker.elastic.co/logstash/logstash:8.16.0

# Install required plugins
RUN logstash-plugin install logstash-codec-sflow logstash-filter-cidr logstash-filter-fingerprint logstash-filter-translate

# Set Java heap
ENV LS_JAVA_OPTS="-Xms2g -Xmx2g"