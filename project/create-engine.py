from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import pandas as pd

Base = declarative_base()

class Crawler(Base):
    __tablename__ = "crawl-movies"

    show_name = Column("Show-name", String, primary_key= True)
    latest_episode = Column("Latest-episode", String)
    critic_score = Column("Critic-score", String)
    audience_score = Column("Audience-score", String)

    def __init__(self, showname, latest_ep, critic_sc, audience_sc):
        self.show_name = showname
        self.latest_episode = latest_ep
        self.critic_score = critic_sc
        self.audience_score = audience_sc

    def __repr__(self):
        return f"({self.show_name} {self.latest_episode} {self.critic_score} {self.audience_score})"
    
engine = create_engine("sqlite:///PractiseDB.db", echo=True)
Base.metadata.create_all(bind=engine)

file_name = "Browser automation and Webscraping/project/crawl-movies.csv"

df = pd.read_csv(file_name)
df.to_sql(con=engine, name=Crawler.__tablename__, if_exists="append", index=False)
session = sessionmaker()
session.configure(bind=engine)
s = session()

# results = s.query(Crawler).limit(10).all()
# for r in results:
#     print(r)