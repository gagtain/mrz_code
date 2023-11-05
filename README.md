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
name | CORINNE       
country | FRA
birth_date | 651206
sex | F
document_type | ID
document_number | 880692310285
optional_data | 
birth_date_hash | 8
expiry_date_hash | 6
document_number_hash | 8
final_hash | 6
document_type | True
country | True
birth_date | True
sex | True
identifier | True
document_number | True
date_of_issuse | True
date_of_issuse_val | 8806
validate_data
document_type | True
nationality | False
country | True
birth_date | True
sex | True
identifier | True
document_number | True
optional_data | True
optional_data_2 | True
final_hash | True
document_number_hash | True
birth_date_hash | True
total_validate: True
mrz [{'mrz_code': 'IDFRABERTHIER<<<<<<<<<<<<<<<<<<<<<<<\n8806923102858CORINNE<<<<<<<6512068F6', 'generated_mrz_code': 'IDFRABERTHIER<<<<<<<<<<<<<<<<<<<<<<<\n8806923102858CORINNE<<<<<<<6512068F6', 'status': True}]
```