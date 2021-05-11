.PHONY: deps lint publish push tox

deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install pyserial black flake8 flit pylint tox tox-gh-actions

lint:  ## Lint and static-check
	python -m flake8 icerok_server
	python -m pylint icerok_server

publish:  ## Publish to PyPi
	python -m flit publish

push:  ## Push code with tags
	git push && git push --tags

tox:   ## Run tox
	python -m tox
