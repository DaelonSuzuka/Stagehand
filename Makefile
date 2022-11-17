# **************************************************************************** #
# General Make configuration

# This suppresses make's command echoing. This suppression produces a cleaner output. 
# If you need to see the full commands being issued by make, comment this out.
MAKEFLAGS += -s

# **************************************************************************** #

APP_FOLDER := app
APP_MAIN = $(APP_FOLDER)/main.py
APP_INFO := $(APP_FOLDER)/app_info.py

# load the project variables
ifneq (,$(wildcard $(APP_INFO)))
include $(APP_INFO)

# remove extra quotes
AppName := $(patsubst "%",%,$(AppName))
AppVersion := $(patsubst "%",%,$(AppVersion))
AppPublisher := $(patsubst "%",%,$(AppPublisher))
AppExeName := $(patsubst "%",%,$(AppExeName))
AppIconName := $(patsubst "%",%,$(AppIconName))
AppId := $(patsubst "%",%,$(AppId))

# export them for InnoSetup
export
endif

# **************************************************************************** #
# Development Targets

# run the application
run: venv
	$(VENV_PYTHON) $(APP_MAIN)

# run the application in pdb
debug: venv
	$(VENV_PYTHON) -m pdb $(APP_MAIN)

# **************************************************************************** #
# Utility Targets

# open the qtawesome icon browser
qta: venv
	$(VENV)/qta-browser

obs: venv
	$(VENV_PYTHON) app/plugins/obs_core/gen.py

# build all the plugins into zips
plugins: venv
	$(VENV_PYTHON) tools/plugins.py build

clean_plugins: venv
	$(VENV_PYTHON) tools/plugins.py clean


# **************************************************************************** #
# Build Targets

# build a self-contained onefile executable 
onefile: venv plugins
	$(VENV_PYINSTALLER) -y onefile.spec

# build a one folder bundle 
bundle: venv plugins
	$(VENV_PYINSTALLER) -y bundle.spec

# run the bundled executable
run_bundle:
ifeq ($(OS),Windows_NT)
	dist/$(AppName)/$(AppName).exe
else
	dist/$(AppName)/$(AppName)
endif

# **************************************************************************** #
# Release Targets

# wrap the bundle into a zip file
zip:
	$(PYTHON) -m zipfile -c dist/$(AppName)-$(AppVersion)-portable.zip dist/$(AppName)/

# build an installer with InnoSetup
installer:
	iscc "installer.iss"

# remove the various build outputs
clean:
	-@ $(RM) build
	-@ $(RM) dist

# **************************************************************************** #
# python venv settings
VENV_NAME := .venv
REQUIREMENTS := requirements.txt

ifeq ($(OS),Windows_NT)
	VENV_DIR := $(VENV_NAME)
	VENV_CANARY_DIR := $(VENV_DIR)\canary
	VENV_CANARY_FILE := $(VENV_CANARY_DIR)\$(REQUIREMENTS)
	VENV_TMP_DIR := $(VENV_DIR)\tmp
	VENV_TMP_FREEZE := $(VENV_TMP_DIR)\freeze.txt
	VENV := $(VENV_DIR)\Scripts
	PYTHON := python
	VENV_PYTHON := $(VENV)\$(PYTHON)
	VENV_PYINSTALLER := $(VENV)\pyinstaller
	RM := -rd /s /q 
	CP := copy
else
	VENV_DIR := $(VENV_NAME)
	VENV_CANARY_DIR := $(VENV_DIR)/canary
	VENV_CANARY_FILE := $(VENV_CANARY_DIR)/$(REQUIREMENTS)
	VENV_TMP_DIR := $(VENV_DIR)/tmp
	VENV_TMP_FREEZE := $(VENV_TMP_DIR)/freeze.txt
	VENV := $(VENV_DIR)/bin
	PYTHON := python3
	VENV_PYTHON := $(VENV)/$(PYTHON)
	VENV_PYINSTALLER := $(VENV)/pyinstaller
	RM := rm -rf 
	CP := cp
endif

# Add this as a requirement to any make target that relies on the venv
.PHONY: venv
venv: $(VENV_DIR) $(VENV_CANARY_FILE)

# Create the venv if it doesn't exist
$(VENV_DIR):
	$(PYTHON) -m venv $(VENV_DIR)

# Update the venv if the canary is out of date
$(VENV_CANARY_FILE): $(REQUIREMENTS)
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -r $(REQUIREMENTS)
	-$(RM) $(VENV_CANARY_DIR)
	-mkdir $(VENV_CANARY_DIR)
	-$(CP) $(REQUIREMENTS) $(VENV_CANARY_FILE)

# forcibly update the canary file
canary: $(VENV_CANARY_DIR)
	$(CP) $(REQUIREMENTS) $(VENV_CANARY_FILE)

# update requirements.txt to match the state of the venv
freeze_reqs: venv
	$(VENV_PYTHON) -m pip freeze > $(REQUIREMENTS)

# try to update the venv - expirimental feature, don't rely on it
update_venv: venv
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install --upgrade -r $(REQUIREMENTS)
	-$(RM) $(VENV_CANARY_DIR)
	-mkdir $(VENV_CANARY_DIR)
	-$(CP) $(REQUIREMENTS) $(VENV_CANARY_FILE)

# remove all packages from the venv
clean_venv:
	$(RM) $(VENV_CANARY_DIR)
	mkdir $(VENV_TMP_DIR)
	$(VENV_PYTHON) -m pip freeze > $(VENV_TMP_FREEZE)
	$(VENV_PYTHON) -m pip uninstall -y -r $(VENV_TMP_FREEZE)
	$(RM) $(VENV_TMP_DIR)

# clean the venv and rebuild it
reset_venv: clean_venv update_venv

# **************************************************************************** #
# expirimental, probably not reliable

# If the first argument is "pip"...
ifeq (pip,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "pip"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)
endif

# forward pip commands to the venv
pip: venv
	$(VENV_PYTHON) -m pip $(RUN_ARGS)
