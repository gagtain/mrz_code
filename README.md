# MRZ checking
### Суть
проект направлен на валидацию, генерацию, сравнение mrz кода

### Как использовать
На момент данного комита, проект может валидировать все предоставленные данные для теста из папки MRZ

Пример работы приложения

```python
json_mrz_data = load_data('MRZ/3x30/2_2.json')
mrz = get_mrz_in_json(json=json_mrz_data)
mrz_class = MrzClass(mrz)
print(mrz_class)
```