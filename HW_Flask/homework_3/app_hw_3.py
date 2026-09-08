from decimal import Decimal
from sqlalchemy import create_engine, String, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    in_stock: Mapped[bool]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))


engine = create_engine('sqlite://')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

with Session() as session:

    new_category = Category(name='Toys', description='sports equipment, construction sets, soft toys')
    session.add(new_category)
    session.flush()

    new_product = Product(name='Ball', price=Decimal('23.50'), in_stock=True, category_id=new_category.id)

    session.add(new_product)

    session.commit()

    # categories = session.query(Category).all()
    # for category in categories:
    #     print(category.id)
    #     print(category.name)
    #     print(category.description)
    #
    # products = session.query(Product).all()
    #
    # for product in products:
    #     print("\n", product.id)
    #     print(product.name)
    #     print(product.price)
    #     print(product.in_stock)
    #     print(product.category_id)








