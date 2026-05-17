# 1. Use the official, lightweight Python image as our base OS
FROM python:3.10-slim

# 2. Tell Docker to do all following work inside an /app folder
WORKDIR /app

# 3. Copy just the requirements file first (this makes building faster later)
COPY requirements.txt .

# 4. Install your Python libraries inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your backend code into the container
COPY . .

# 6. Expose port 5000 so the outside world can talk to your API
EXPOSE 5000

# 7. The command to start your Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]