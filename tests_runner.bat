call activate py27
pytest --cov-report html --cov --doctest-modules --cache-clear

call activate py36
pytest --cov-report html --cov --doctest-modules --cache-clear

pause