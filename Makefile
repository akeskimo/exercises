ROOTPATH := $(shell pwd)
PYTHONPIP := $(ROOTPATH)/env/bin/pip3

install: requirements.txt
	rm -rf $(ROOTPATH)/env
	virtualenv -p python3 env
	$(PYTHONPIP) install -U setuptools pip
	$(PYTHONPIP) install -r requirements.txt
