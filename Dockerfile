# Use lightweight Python base
FROM python:3.11-slim

# Install OS dependencies for Playwright and cron
RUN apt-get update && apt-get install -y \
	wget \
	curl \
	xvfb \
	cron \
	&& rm -rf /var/lib/apt/lists/*

# Install Playwright and browser
RUN pip install playwright && playwright install --with-deps chromium

# Set working dir
WORKDIR /app

# Copy project files (TODO: check this)
COPY . .

# Install python dependencies
RUN pip install -r requirements.txt

# Copy and register cron job
COPY cronjob /etc/cron.d/app-cron
RUN chmod 0644 /etc/cron.d/app-cron && crontab /etc/cron.d/app-cron

# Keep cron running in the foreground (TODO: good idea?)
CMD ["cron", "-f"]


