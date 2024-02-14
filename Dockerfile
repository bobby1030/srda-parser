FROM python:3.11-bookworm

# Set the working directory in the container
RUN mkdir /app
WORKDIR /app

COPY ./backend /app/backend
COPY ./resources /app/resources

# Install Python dependencies
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Set the command to run the application
CMD ["./backend/init.sh"]
