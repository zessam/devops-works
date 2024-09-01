#!/bin/bash

# PostgreSQL connection parameters
HOST="database-host"
USER="suser"
DBS=("database-name") # list of databases 

# Loop through databases and dump each one except the excluded ones
for DB in "${DBS[@]}"; do
    if [[ "$DB" != "rdsadmin" && "$DB" != "chatwoot_production" ]]; then
        echo "Dumping schema and data for database: $DB"

        # Dump schema only
        pg_dump -h "$HOST" -U "$USER" -d "$DB" -F c --no-owner --no-acl --schema-only -f "${DB}_schema.dump"
        
        # Dump data only
        pg_dump -h "$HOST" -U "$USER" -d "$DB" -F c --no-owner --no-acl --data-only -f "${DB}_data.dump"
    else
        echo "Skipping database: $DB"
    fi
done
