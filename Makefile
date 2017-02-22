up:
	# bring up the services
	docker-compose up -d

sync: up
	# set up the database tablea
	docker-compose exec cartoview python manage.py migrate
	docker-compose exec cartoview python manage.py loaddata sample_admin.json
	docker-compose exec cartoview python manage.py loaddata json/default_oauth_apps.json
	docker-compose exec cartoview python manage.py loaddata app_stores.json


prepare_manager: up
        #make migration for app_manager
	docker-compose exec cartoview python manage.py makemigrations app_manager
migrate_people: up
	docker-compose exec cartoview python manage.py migrate people
migrate:
	docker-compose exec cartoview python manage.py migrate --noinput
wait:
	sleep 5
logs:
	docker-compose logs --follow
down:
	docker-compose down
reset: down up wait sync
