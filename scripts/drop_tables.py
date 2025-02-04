from app.database import engine, Base

# Drop all tables in the database
Base.metadata.drop_all(bind=engine)
