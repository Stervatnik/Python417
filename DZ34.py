import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from faker import Faker
from faker.providers import person, date_time


fake = Faker('ru_RU')


Base = declarative_base()


class Sotrudnik(Base):
    __tablename__ = 'sotrudniki'

    id = Column(Integer, primary_key=True)
    familiya = Column(String)
    imya = Column(String)
    otchestvo = Column(String)
    data_rojdeniya = Column(Date)
    dolzhnost = Column(String)

    def __repr__(self):
        return f"<Sotrudnik(ФИО='{self.familiya} {self.imya} {self.otchestvo}', Дата рождения='{self.data_rojdeniya}', Должность='{self.dolzhnost}')>"


DATABASE_URL = "sqlite:///./sotrudniki.db"
engine = create_engine(DATABASE_URL, echo=True)


Base.metadata.create_all(engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


NUMBER_OF_RECORDS = 5


for _ in range(NUMBER_OF_RECORDS):
    f_name = fake.first_name()
    l_name = fake.last_name()
    patronymic = fake.middle_name()

    fake_sotrudnik = Sotrudnik(
        familiya=l_name,
        imya=f_name,
        otchestvo=patronymic,
        data_rojdeniya=fake.date_between(start_date='-60y', end_date='-20y'),
        dolzhnost=fake.job()
    )
    session.add(fake_sotrudnik)


session.commit()


sotrudniki = session.query(Sotrudnik).all()
print("Список сотрудников:")
for sotrudnik in sotrudniki:
    print(sotrudnik)


session.close()

print(f"\nБаза данных 'sotrudniki.db' успешно создана и заполнена в директории: {os.getcwd()}")