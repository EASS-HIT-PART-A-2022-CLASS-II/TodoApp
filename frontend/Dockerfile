FROM node:14

COPY ./package.json /package.json

RUN npm install

COPY ./ /

CMD ["npm", "start"]
