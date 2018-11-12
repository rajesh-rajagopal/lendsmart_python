.PHONY: clean install

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install .

test: install
	. venv/bin/activate; \
  tox

release:
	. venv/bin/activate; python setup.py sdist upload
	. venv/bin/activate; python setup.py bdist_wheel upload


clean:
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete

