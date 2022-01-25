release: python manage.py migrate
release: python manage.py collectstatic
web: gunicorn TRF_sudoku_solver.wsgi --log-file -