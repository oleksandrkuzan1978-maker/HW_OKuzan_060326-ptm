from decimal import Decimal
from sqlalchemy import create_engine, String, Numeric, ForeignKey
from sqlalchemy.orm import selectinload
from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    in_stock: Mapped[bool]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship(back_populates='products')


    def __str__(self) -> str:
        return f'Product: name: {self.name}; price: {self.price}; availability: {self.in_stock}; category_id: {self.category_id}'

    def __repr__(self) -> str:
        return f'Product: name: {self.name}; price: {self.price}; availability: {self.in_stock}; category_id: {self.category_id}'


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    products: Mapped[list['Product']] = relationship(back_populates='category')

    def __str__(self) -> str:
        return f'Category: {self.name}; {self.description}'

    def __repr__(self) -> str:
        return f'Category: {self.name}; {self.description}'


engine = create_engine('sqlite://')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

file_category = 'data_categories.csv'
file_product = 'data_products.csv'


def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line


with Session() as session:
    # 2_1. Загружаем категории
    for line in read_lines(file_category):
        name, descript = (part.strip() for part in line.split(","))
        session.add(Category(name=name, description=descript))

    session.flush()

    categories = {
        category.name: category.id
        for category in session.scalars(select(Category))
    }

    # 2_2. Загружаем продукты
    for line in read_lines(file_product):
        name, price, in_stock, category_name = (
        part.strip() for part in line.split(",")
    )

        category_id = categories[category_name]

        session.add(Product(
            name=name,
            price=Decimal(price),
            in_stock=in_stock == "True",
            category_id=category_id
        ))

    session.commit()


    # Задача 2 Чтение данных
    # Извлеките все записи из таблицы categories.
    # Для каждой категории извлеките
    # и выведите все связанные с ней продукты,
    # включая их названия и цены.

    query = select(Category).options(
        selectinload(Category.products)
    )

    categories = session.scalars(query) #.all()

    for category in categories:
        print(f'Категория: {category.name}')

        for product in category.products:
            print(f'\t{product.name} — {product.price}')


    # Задача 3 Обновление данных
    # Найдите в таблице products
    # первый продукт с названием "Смартфон".
    # Замените цену этого продукта на 349.99.
    query = select(Product).where(Product.name == "Смартфон").order_by(Product.id).limit(1)
    product = session.scalar(query)
    if product:
        product.price = Decimal("349.99")
        session.commit()

    print(f"\nРезультат задачи №3:\n\t", product)


    # Задача 4 Агрегация и группировка
    # Используя агрегирующие функции и группировку,
    # подсчитайте общее количество продуктов в каждой категории.
    query = select(Category.name, func.count(Product.id)
                    ).join(Product, Category.id == Product.category_id
                           ).group_by(Category.id, Category.name).order_by(Category.id)

    prod_by_cat = session.execute(query)

    print(f"\nРезультат задачи №4:")
    for category_name, count in prod_by_cat:
        print(f'\tКатегория: "{category_name}", кол-во наименований товаров: {count}')


    # Задача 5 Группировка с фильтрацией
    # Отфильтруйте и выведите только те категории,
    # в которых более одного продукта
    query = select(Category.name, func.count(Product.id)
                    ).join(Product, Category.id == Product.category_id
                           ).group_by(Category.id).having(func.count(Product.id) > 1)
    cat_more_one = session.execute(query)


    print(f"\nРезультат задачи №5:")
    for category_name, count in cat_more_one:
        print(f'\tКатегория: "{category_name}", кол-во товаров: {count}')











