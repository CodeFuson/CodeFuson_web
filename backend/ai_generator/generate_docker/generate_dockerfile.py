import os


def generate_dockerfile(frontend_folder):
    dockerfile_content = """
# Use Node.js image as base
FROM node:16-slim

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json /app/
RUN npm install

# Install missing dependencies (like web-vitals)
RUN npm install web-vitals

# Copy all files to container
COPY . /app/

# Build the React app
RUN npm run build

# Expose the port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
    """

    with open(os.path.join(frontend_folder, "Dockerfile"), "w") as f:
        f.write(dockerfile_content)