# Haivision Log Reader

A lightweight and efficient utility designed to parse and analyze 24-hour status log files from the **Haivision Gateway**. This tool automates the process of extracting critical metrics, exporting structured data to CSV, and generating visual charts for comprehensive monitoring and troubleshooting.

## Features

- **Automated Parsing**: Quickly processes large 24-hour Haivision Gateway status log files.
- **Data Export**: Cleans and converts raw log data into easy-to-read, structured **CSV files** for custom analysis.
- **Data Visualization**: Automatically generates intuitive **charts and graphs** to display gateway performance and task status trends over time.
- **Lightweight & Fast**: A simple, no-fuss program built for quick diagnostics and operational insights.

## Getting Started

### Prerequisites

Before running the program, ensure you have the following installed:
- **Docker Engine** or **Docker Desktop**
- The official Docker image file archive (`.tar`) downloaded from the [Releases](https://github.com/pattwen/Haivision-Log-Reader/releases) page.

### Installation

1. Load the Docker image from the downloaded archive file:
   ```bash
   docker load -i haivision-log-reader.tar
   ```

2. Run the Docker container (replace `x.y.z` with your actual version tag):
   ```bash
   docker run -d -p 5678:5678 --name haivision-log-reader haivision-log-reader:x.y.z
   ```

## Usage

1. Open a web browser and visit `http://127.0.0.1:5678` (or your server's IP address and port).
2. Upload your Haivision Gateway log file (`.log`).
3. In the **Analysis Task List**, click **Start Analysis** and wait for a moment.
4. When the button text changes to **"View Results"**, click it to view the data trend charts and download the generated CSV file.
