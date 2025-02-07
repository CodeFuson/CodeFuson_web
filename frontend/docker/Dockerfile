FROM node:lts-slim

WORKDIR /srv/app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npx", "serve", "-s", "build", "localhost:3000"]
