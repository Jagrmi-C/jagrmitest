from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1989@localhost/jagrmi', echo=True)
