.PHONY: clean install

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install .
	. venv/bin/activate; pip install tox
	. venv/bin/activate; pip install twine

test: install
	. venv/bin/activate; \
  tox

release: install
	. venv/bin/activate; python setup.py sdist bdist_wheel
	. venv/bin/activate; twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	. venv/bin/activate; twine upload dist/*

clean:
	rm -rf dist
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete

