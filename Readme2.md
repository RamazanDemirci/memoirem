

-- git commit reset
git reset --hard <hash-code>

-- remote branch force push
git push --force origin <branch-name>


- display service logs
docker-compose logs -f service_name

-start service
docker-compose start -f service_name

- docker makemigrations
docker-compose run --rm backend python manage.py makemigrations

- docker migrate
docker-compose run --rm backend python manage.py migrate

- create superuser
docker-compose run --rm backend python manage.py createsuperuser


- django boilerplate refs
https://github.com/vintasoftware/django-react-boilerplate

- django tests refs 
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/

