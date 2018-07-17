rem call activate py27
rem for distributed testing rem pip install pytest-xdist
py.test --cov-report html --cov --doctest-modules --cache-clear
rem --verbose
pause