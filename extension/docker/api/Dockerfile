FROM node:18-alpine3.15

RUN mkdir -p /usr/api
WORKDIR /usr/api
COPY . .

RUN npm install

CMD ["node", "server.js"]