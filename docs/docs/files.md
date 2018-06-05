# Files description
* `docs/` — documentation
  * `api/` — api documentation
  * `files.md` — list of files and their description
  * `index.md` — main documentation entry point
* `img/` — readme images
  * `github-header.png` — GitHub readme header image
* `server/` — main executable server files
  * `config/` — configuration files for Django server
    * `common.py` — main configuration file
    * `local.py` — configuration file for local deployment
    * `production.py` — configuration file for production deployment
  * `manage.py` — `...`
  * `Dockerfile` — configuration for Docker
  * `requirements.txt` — file with needed packages
  * `wait_for_postgres.py` — `...`
  * `...`
* `.travis.yml` — configuration file for Travis CI
* `docker-compose.yml` — configuration file to run multiple containers
* `LICENSE` — MIT license file
* `mkdocs.yml` — `...`
* `README.md` — main readme of the repository
* `setup.cfg` — Python setup file