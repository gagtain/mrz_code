# MRZ checking
### Суть
проект направлен на валидацию, генерацию, сравнение mrz кода

### Как использовать
На момент данного комита, проект может валидировать все предоставленные данные для теста из папки MRZ

Пример работы приложения

```python
json_mrz_data = load_data('MRZ/2x36/1.json')
mrz = get_mrz_in_json(json=json_mrz_data)
mrz_class = MrzClass(mrz)
mrz_class.print_table()
```
Вывод:
```
surname | BERTHIER
name | 
country | FRA
nationality | 858
birth_date | 651206
expiry_date | <<<<<<
sex | F
document_type | ID
document_number | 880692310285
optional_data | 512068F
birth_date_hash | 8
expiry_date_hash | 6
document_number_hash | 8
final_hash | 6
ident BERTHIER<<<<<<<<<<<<<<<<<
document_type | True
country | True
birth_date | True
sex | True
identifier | True
document_number | True
total_validate: True
```