#!/bin/bash

# Cloud SQL connection parameters
HOST="database-host"
USER="postgres"
DBS=("database-name") # list of databases 

# Loop through databases and restore each one
for DB in "${DBS[@]}"; do
    if [[ "$DB" != "rdsadmin" && "$DB" != "chatwoot_production" ]]; then
        echo "Restoring schema and data for database: $DB"

        # Restore schema
        pg_restore -h "$HOST="database-host"" -U "$USER" -d "$DB" --no-owner --no-acl "${DB}_schema.dump"

        # Restore data
        pg_restore -h "$HOST="database-host"" -U "$USER" -d "$DB" --no-owner --no-acl "${DB}_data.dump"
    else
        echo "Skipping database: $DB"
    fi
done
