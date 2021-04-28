# make file
freeze:
	pip-compile -r --no-index --output-file=requirements.txt requirements/requirements-prod.in
	pip-compile -r --no-index --output-file=requirements-test.txt requirements/requirements-test.in

install:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements.txt

install-test:
	pip install pip-tools
	pip-sync requirements.txt

src_package: clean
	python3 setup.py sdist bdist_wheel
	echo "Spark job package successfully created!"

clean:
	rm -rf dist/ build/ poc_pyspark_docker.egg-info/ || true

run-tests:
	pytest