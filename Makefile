.PHONY: install test report

install:
	python -m pip install -e ".[dev]"

test:
	pytest -q

# Supply DATASET_DIR, for example:
# make report DATASET_DIR=data/raw/industrial-inspection-system
report:
	@test -n "$(DATASET_DIR)" || (echo "Set DATASET_DIR to the unpacked Kaggle dataset" && exit 1)
	mkdir -p artifacts
	python -m industrial_inspection.dataset_report "$(DATASET_DIR)" \
		--class-names bottle cap label liquid \
		--output artifacts/dataset_report.json
