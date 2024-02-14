FROM node:20-bookworm

# Set the working directory in the container
RUN mkdir /app
WORKDIR /app

COPY . .

# Install node dependencies and build the webui
RUN npm install && npm run build

# Set the command to run the application
CMD ["node", "build"]