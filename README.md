# Exploration_MoscowTravelHack


### Концепция



### API

```text
-> GET /filters/ # получение статистики по пользователю
response:
{
  'orders': list[text] # Порядок в котором выводятся фильтры
  'filters'
  'default_filters': list[]
}
```

```text
-> POST /statistics/ # получение статистики по пользователю
response:
{
  
}
```