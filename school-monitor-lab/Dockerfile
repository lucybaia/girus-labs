FROM python:3.9-slim

WORKDIR /usr/src/app

# Copy the new script
COPY monitor.py .

# Setting a default environment variable
ENV SCHOOL_NAME="CEUB Integrator Project"

CMD ["python", "monitor.py"]