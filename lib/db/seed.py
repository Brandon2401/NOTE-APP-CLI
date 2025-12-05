from faker import Faker
from models import Base, engine, session, Note

fake = Faker()

def seed_notes(n=5):
    print("Seeding notes...")

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    for _ in range(n):
        note = Note(
            title=fake.sentence(),
            body=fake.text(),
            tags="test,example"
        )
        session.add(note)

        session.commit()
        print("Database seeded successfully.")

        if __name__ == "__main__":
            seed_notes()