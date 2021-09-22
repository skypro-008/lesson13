# Задача 6

Создать 3 роута и 3 представления, которые будут представлять собой API (вызов метода по сути) со следующим функционалом:

### Получить пользователя по идентификатору

 /get_user/(pk)

Формат ответа:

```json 
{"id": 1, "name": "Ivan", "age": 34, "is_blocked": false}
```

---

### Получить всех пользователей

/get_users

Формат ответа:

```
[{"id": 1, "name": "Ivan", "age": 34, "is_blocked": false}, …]
```

---

### Создать пользователя

/create_user

Тело запроса:
```json
{"id": 1, "name": "Ivan", "age": 34, "is_blocked": false}
```