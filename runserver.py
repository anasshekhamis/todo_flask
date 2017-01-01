from todo import app
from todo.config import ProductionConfig

app.config.from_object(ProductionConfig)

if __name__ == '__main__':
    app.run()