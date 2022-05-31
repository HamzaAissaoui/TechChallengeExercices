import os
from app import app


if __name__ == "__main__":
    app.run(debug=True , port=1234, host="0.0.0.0")
