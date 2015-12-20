.PHONY: develop install clean

install develop: %:
	pip --quiet install -r $<
	python setup.py $(SETUPFLAGS) $* $(PYTHONFLAGS)

clean:
	rm -rf *.egg-info build dist
