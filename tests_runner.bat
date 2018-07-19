call activate py27
py.test --cov-report html --cov --doctest-modules --cache-clear

call activate py36
py.test --cov-report html --cov --doctest-modules --cache-clear

pause