dc := docker-compose run -w /opt/ws/ wspkg
all: clean build lint test package runtest
clean:
	find . -type d -iname '__pycache__' -exec rm -rf {} \; | true
	find . -type f -iname '*.pyc' -delete | true
	rm -rf build/* | true
	rm -rf dist/* | true
build:
	$(dc) build
lint:
	$(dc) autopep8 --in-place --aggressive ws/*.py
	$(dc) flake8 ws/
	$(dc) autopep8 --in-place --aggressive run-ws
	$(dc) flake8 run-ws
package:
	$(dc) python setup.py sdist bdist_wheel
runtest:
	$(dc) python -m pytest test/
	$(dc) /bin/bash -c "pip install dist/ws-*-py3*.whl && run-ws"
