# QR Code Generator with API

## Installation
- [Installation with uv.](#Installation with uv)
- [Installation with pip.](#Installation with pip)
- [Installation with docker.](#Installation with docker)

## Installation with uv
1. Clone the project.
2. Go to project folder.
3. Run `uv sync`.
4. Run `uv run python -m src.main`.

## Installation with pip
1. Clone the project.
2. Go to project folder.
3. Create virtual environment. For example `python3 -m venv .venv` (use `py` or `python` on **Windows**)
4. Activate virtual environment:
    - *on Linux and macOS* `source .venv/bin/activate`
    - *on Windows* `.venv\Scripts\activate.bat` for CMD or `.\.venv\Scripts\Activate.ps1` for PowerShell.
5. Run `python3 -m src.main` (use `py` or `python` on **Windows**)

## Installation with docker
1. Build the image `docker build -t my-image .`.
2. Run the container
    - Default: `docker run -d -p 7080:8080 --name my-project my-image` (7080 - **port on host**)
    - With .env file (recommended): `docker run -d -p 7080:8080 --env-file .env --name my-project my-image` (7080 - **port on host**, 8080 - **port defined in .env file**)
3. Stop and remove the container
    - `docker stop my-project`
    - `docker rm my-project`
4. Remove image
    - `docker rmi my-image`