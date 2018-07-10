# Python Flask API with Elasticsearch

Prerequisites :
- docker
- docker-compose

##

### Start environment with docker
Ensure the following settings on your machine: 
```
sudo sysctl -w vm.max_map_count=2262144
```
Then :
```
make start
```

##

### Install project dependencies :
```
make install
```

##

### Full commands list
```
make help :
 help:            Help command
 start:           Start docker containers
 stop:            Stop docker containers
 destroy:         Remove docker containers
 install:         Install python dependencies
 install@docker:  Install python dependencies on Docker host
```

##

### Technical test
- [French version](docs/technical_test_fr.md)
- [English version](docs/technical_test_en.md)