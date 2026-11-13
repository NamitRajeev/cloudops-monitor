

\# CloudOps Monitor



A beginner DevOps project demonstrating application development, version control, automated testing, CI configuration and Docker packaging.



\## Technologies Used

\- Python

\- Flask

\- Git and GitHub

\- Pytest

\- GitHub Actions

\- Docker



\## Application Endpoints



| Endpoint | Purpose |

|---|---|

| `/` | Application information |

| `/health` | Application health check |

| `/system` | System information |



\## Automated Testing



Tests are written using Pytest.



Run locally with:



```bash

python -m pytest -v

```



\## CI Pipeline



A GitHub Actions workflow is configured to install dependencies and run automated tests when code is pushed to the main branch or a pull request targets it.



\## Docker



A Dockerfile and `.dockerignore` are included to prepare the application for containerization.



\*\*Note:\*\* Docker image building and container execution have not yet been verified.



