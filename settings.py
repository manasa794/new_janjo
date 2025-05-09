pip install dj-database-url
 import dj-database-url
 import os
 DATABASES = {
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_koj7_user:u9x4Vk40rFihJvZi8i7qEDdEBl30GEiy@dpg-d0epek49c44c738a76v0-a.oregon-postgres.render.com/test_db_koj7"))
}
