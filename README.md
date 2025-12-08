# QR Code Generator with API

## Installation
- [Installation with uv](https://github.com/SergiyOlishchuk/QR_code_generator_with_API?tab=readme-ov-file#installation-with-uv)
- [Installation with pip.](https://github.com/SergiyOlishchuk/QR_code_generator_with_API/edit/master/README.md#installation-with-pip)
- [Installation with docker.](https://github.com/SergiyOlishchuk/QR_code_generator_with_API/edit/master/README.md#installation-with-docker) (recommended)

### Installation with uv
1. Rename '.env.example' file to '.env'.
2. Clone the project.
3. Go to project folder.
4. Run `uv sync`.
5. Run `uv run python -m src.main`.

### Installation with pip
1. Rename '.env.example' file to '.env'.
2. Clone the project.
3. Go to project folder.
4. Create virtual environment. For example `python3 -m venv .venv` (use `py` or `python` on **Windows**)
5. Activate virtual environment:
    - *on Linux and macOS* `source .venv/bin/activate`
    - *on Windows* `.venv\Scripts\activate.bat` for CMD or `.\.venv\Scripts\Activate.ps1` for PowerShell.
6. Run `python3 -m src.main` (use `py` or `python` on **Windows**)

### Installation with docker
1. Rename '.env.example' file to '.env'.
2. Build the image `docker build -t my-image .`.
3. Run the container
    - Default: `docker run -d -p 7080:8080 --name my-project my-image` (7080 - **port on host**)
    - With .env file (recommended): `docker run -d -p 7080:8080 --env-file .env --name my-project my-image` (7080 - **port on host**, 8080 - **port defined in .env file**)
4. Stop and remove the container
    - `docker stop my-project`
    - `docker rm my-project`
5. Remove image
    - `docker rmi my-image`
