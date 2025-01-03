# Product Store API

## Описание проекта

Добро пожаловать в **Product Store API**! Этот проект представляет собой **API для магазина продуктов**, созданное с использованием **Django Rest Framework (DRF)**. Проект включает в себя различные модели данных для управления **категориями**, **подкатегориями**, **продуктами** и **корзинами**, предоставляя гибкие возможности для работы с товарным каталогом и корзинами пользователей.

### Основные особенности:

- **Аутентификация через JWT**: Реализована защита данных с помощью аутентификации через **JWT токены**, что позволяет безопасно управлять доступом к API.
- **Полный набор CRUD операций**: Для обработки запросов используется комбинация **ViewSets** и **APIView**:
  - **ViewSets** — для базовых CRUD операций с минимальными настройками.
  - **APIView** — когда требуется более глубокая настройка запросов, такие как сложная логика фильтрации или валидации.
- **Корзина пользователя**: Операции с корзиной доступны только авторизованным пользователям, и каждый пользователь может работать только со своей корзиной.
- **Документация OpenAPI**: Проект использует **drf-spectacular** для генерации документации в формате **OpenAPI**. Документация доступна по следующему адресу при локальном развертывании: [API Docs](http://127.0.0.1:8000/api/docs/).
- **Тесты**: Были добавлены несколько автотестов для проверки правильности работы методов GET и POST с корзинами, что гарантирует стабильную работу API.

## Стек технологий

- **Django** & **Django Rest Framework**: Основные фреймворки для реализации серверной логики и RESTful API.
- **JWT (JSON Web Tokens)**: Для обеспечения безопасности и аутентификации пользователей.
- **drf-spectacular**: Для автоматической генерации документации API.
- **pytest**: Для покрытия тестами и проверки правильности работы API.

## Установка и запуск

Чтобы развернуть проект локально, выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/project.git
