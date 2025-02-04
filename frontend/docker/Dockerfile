# Use official Node.js image from Docker Hub
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package files first to optimize caching
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the React app
COPY . .

# Build the React app
RUN npm run build

# Expose port 3000 for React app
EXPOSE 3000

# Serve the React app using serve package
CMD ["npx", "serve", "-s", "build"]
