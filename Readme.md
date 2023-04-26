# HTTP Stats

> **Version:** 0.1.0 **Date:** 04.26.2023 **Author:** Olcay Davut Cabbas
>
> **Email:** [olcay.d.cabbas@gmail.com]

### Requirements
* The number of flows of HTTP traffic.
* The total number of bytes transmitted in HTTP traffic.
* The top hostname visited in HTTP traffic.

## Features

command-line program that takes the path of the input PCAP file as a command-line
argument and prints the above information to the standard output in a human-readable format.

## Dockerfile

docker build -t olcay/http_analyse .

### Basic Usage
```
docker run -e MY_VAR=<pcap_name> <image_id>
```