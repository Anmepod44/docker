# vulnerable-app2/Dockerfile

FROM node:latest

RUN apt-get update && apt-get install -y \
    vim \
    wget \
    net-tools \
    nmap \
    apache2

WORKDIR /usr/src/app
COPY . .

RUN npm install

CMD ["node", "server.js"]
