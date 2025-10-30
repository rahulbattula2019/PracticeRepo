# Commands to Install MongoDB server

1. sudo apt update

2. sudo apt install -y curl gnupg

3. curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

4. echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

5. sudo apt update

6. sudo apt install -y mongodb-org

7. mkdir -p ~/data/db

8. mkdir -p ~/data/log

9. mongod --dbpath ~/data/db --logpath ~/data/log/mongod.log --fork

10. pgrep mongod


## Configuration to modify the root user password:

1. ps aux | egrep 'mongod|mongos'

2. mongod --dbpath /home/codespace/data/db --logpath /home/codespace/data/log/mongod.log --fork

3. mongosh

4. use admin

5. db.createUser({
  user: "root",
  pwd: "password",
  roles: [ { role: "root", db: "admin" } ]
})

6. mongosh -u root -p 'password' --authenticationDatabase admin


### Connect via extension
mongodb://root:password@127.0.0.1:27017/?authSource=admin&directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh

