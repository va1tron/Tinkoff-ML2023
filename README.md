# Решение для вступительного задания Тинькофф

Решение находится в файле [compare.py](/compare.py)

## Запуск

Для запуска небходимо использовать данную комманду:

```bash
python3 compare.py <file1> <file2>
```

## Принцип работы

При сравнении файлов используются расстояние Левенштейна. Перед началом работы, весь текст очищается от комментариев, строк документации, табуляции и пробелов, а также приводится к нижнему регистру. После этого сравниваются строки, которые получились в результате очистки.
