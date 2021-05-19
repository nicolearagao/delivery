install:
	pip install -e .['dev']

clean:
	pip uninstall delivery

test:
	pytest ./tests/ -v

