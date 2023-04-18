# Use an official Python image as the base image
FROM python:3.10-slim-buster

# copy the requirements file into the image
COPY . /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3000
EXPOSE 3000

# configure the container to run in an executed manner
CMD ["python", "app.py"]