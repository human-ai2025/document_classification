# Use a base image
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel

WORKDIR /user

COPY build_run/deploy/req.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

# Copy the code and script file into the container
COPY src build_run/deploy/startup.sh ./

# Make the script executable
RUN chmod +x startup.sh

EXPOSE 8501

# Run the script when the container starts
ENTRYPOINT ["./startup.sh"]