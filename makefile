.PHONY: black

lint:
	python3 -m pylint advent/

black:
	python3 -m black advent/