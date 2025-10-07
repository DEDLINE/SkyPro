import pytest
from sqlalchemy import text
from db_connect import engine


@pytest.fixture(scope="module")
def db_session():
    with engine.begin() as connection:
        yield connection


@pytest.fixture
def clean_up_student(db_session):
    created_ids = []

    def _cleanup_id(student_id):
        if student_id not in created_ids:
            created_ids.append(student_id)

    yield _cleanup_id

    if created_ids:
        delete_sql = text("DELETE FROM students WHERE id = ANY(:ids)")
        db_session.execute(delete_sql, {"ids": created_ids})


def test_student_creation(db_session, clean_up_student):
    test_name = "Анна Тестова"

    insert_sql = text("INSERT INTO students (name) VALUES (:name)"
                      " RETURNING id")
    result = db_session.execute(insert_sql, {"name": test_name})

    student_id = result.scalar()
    clean_up_student(student_id)

    select_sql = text("SELECT name FROM students WHERE id = :id")
    result = db_session.execute(select_sql, {"id": student_id}).scalar()

    assert result == test_name, "Студент не был создан или имя не совпадает."


def test_student_update(db_session, clean_up_student):
    initial_name = "Старый Имя"
    new_name = "Новое Имя Обновление"

    insert_sql = text("INSERT INTO students (name) VALUES (:name)"
                      " RETURNING id")
    student_id = (db_session.execute(insert_sql, {"name": initial_name})
                  .scalar())
    clean_up_student(student_id)

    update_sql = text("UPDATE students SET name = :new_name WHERE id = :id")
    db_session.execute(update_sql, {"new_name": new_name, "id": student_id})

    select_sql = text("SELECT name FROM students WHERE id = :id")
    updated_name = db_session.execute(select_sql, {"id": student_id}).scalar()

    assert updated_name == new_name, "Имя студента не было обновлено."


def test_student_soft_delete(db_session, clean_up_student):
    test_name = "Удаляемый Студент"

    insert_sql = text("INSERT INTO students (name) VALUES (:name)"
                      " RETURNING id")
    student_id = db_session.execute(insert_sql, {"name": test_name}).scalar()
    clean_up_student(student_id)

    delete_sql = text("UPDATE students SET is_deleted = TRUE WHERE id = :id")
    db_session.execute(delete_sql, {"id": student_id})

    select_sql = text("SELECT is_deleted FROM students WHERE id = :id")
    is_deleted = db_session.execute(select_sql, {"id": student_id}).scalar()

    assert is_deleted is True, ("Запись не была помечена как удаленная"
                                " (is_deleted = TRUE).")
