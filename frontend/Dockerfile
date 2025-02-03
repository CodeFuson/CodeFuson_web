# Use official Node.js image from Docker Hub
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Copy the React app
COPY . /app/

# Build the React app
RUN npm run build

# Expose port 3000 for React app
EXPOSE 3000

# Serve the React app using serve package (after build)
CMD ["npx", "serve", "build"]
