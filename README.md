# Sprint_4_qa_python
Описание тестовых функций для класса BooksCollector
develop
1. Проверка добавления книг
- Тест test_add_new_book_add_two_books:
Проверяет, что книги добавляются в коллекцию.

- Тест test_add_new_book_invalid_length:
Проверяет, что книги с некорректной длиной названия не добавляются.

- Тест test_add_new_book_duplicate:
Проверяет, что дубликаты книг не добавляются.

2. Книги с возрастным рейтингом отсутствуют в списке книг для детей
- Тест test_get_books_for_children_correct_genre:
Проверяет, что книги с жанрами из genre_age_rating не попадают в список для детей.

- Тест test_get_books_for_children_adult_rating:
Дополнительно проверяет, что книги с "взрослыми" жанрами не включаются в список для детей.

- Тест test_get_books_for_children:
Проверяет, что книга с детским жанром ("Мультфильмы") попадает в список для детей.

3. У добавленной книги нет жанра
- Тест test_new_book_has_no_genre:
Проверяет, что у новой книги жанр по умолчанию пустой.

4. Проверка других методов:
- Тест test_books_genre_fav_dict_is_empty:
Проверяет, что при создании объекта коллекции словарь книг и список избранных пусты.

- Тест test_genre_list_is_not_empty:
Проверяет, что список жанров инициализирован корректно.

- Тест test_genre_age_rating_list_is_not_empty:
Проверяет, что список жанров с возрастным рейтингом инициализирован корректно.

- Тест test_add_book_with_genre_and_rating:
Проверяет установку жанра для книги.

- Тест test_add_book_in_favorites_when_books_in_list:
Проверяет добавление книги в избранное.

- Тест test_add_book_in_favorites_when_book_not_in_list:
Проверяет, что нельзя добавить в избранное книгу, которой нет в коллекции.

- Тест test_delete_book_from_favorites:
Проверяет удаление книги из избранного.

- Тест test_delete_book_from_favorites_no_name_in_list:
Проверяет, что нельзя удалить из избранного книгу, которой там нет.

- Тест test_get_list_of_favorites_books_not_empty:
Проверяет, что список избранных книг не пуст после добавления книг.

- Тест test_get_list_of_favorites_books_empty_list:
Проверяет, что список избранных книг пуст после удаления всех книг.
main
