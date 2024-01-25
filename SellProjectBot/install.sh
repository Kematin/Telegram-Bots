# install api (check .env.prod file before start)
cd projects-api
docker build -t project_api .
docker-compose up -d

# install admin panel
cd ..
cd admin-client
docker build -t admin_panel .
docker-compose up -d

# install telegram bot
# cd ..
# cd sell-projects-bot
# docker build -t project_bot .
# docker-compose up -d
