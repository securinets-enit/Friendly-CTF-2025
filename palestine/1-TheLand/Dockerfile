# Use Alpine as the base image
FROM alpine:latest

# Update and upgrade Alpine packages, and install socat
RUN apk update && \
    apk upgrade && \
    apk add socat bash

# Create a non-root user "ctfplayer" with home directory and shell
RUN adduser -h /home/ctfplayer -s /bin/bash -D ctfplayer -u 1001

# Set the working directory to /home/ctfplayer
WORKDIR /home/ctfplayer

# Copy the necessary files into the container
COPY ./flag.txt /home/ctfplayer/flag.txt
COPY ./asker /home/ctfplayer/asker

# Give execute permissions to the "asker" binary
RUN chmod +x ./asker

# Switch to non-root user "ctfplayer"
USER ctfplayer

# Expose the port
EXPOSE 1338

# Use socat to listen on TCP port 1338 and execute the "asker" binary
CMD socat TCP-LISTEN:1338,reuseaddr,fork EXEC:"./asker"
