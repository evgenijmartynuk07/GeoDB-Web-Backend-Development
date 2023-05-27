from django.core.management.base import BaseCommand
from django.db import connections, DEFAULT_DB_ALIAS
from django.db.utils import OperationalError
from django.contrib.gis.db.backends.postgis.base import DatabaseWrapper as PostGISDatabaseWrapper
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections[DEFAULT_DB_ALIAS]
                db_conn.connect()
                if isinstance(db_conn, PostGISDatabaseWrapper):
                    cursor = db_conn.cursor()
                    cursor.execute("SELECT PostGIS_version()")
                    postgis_version = cursor.fetchone()[0]
                    self.stdout.write(self.style.SUCCESS(f"PostGIS version: {postgis_version}"))
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
