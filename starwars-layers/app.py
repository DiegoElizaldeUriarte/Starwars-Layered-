import os
import presentation

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)


if __name__ == "__main__":
    presentation.app.run(host="0.0.0.0", debug=True, port=port)
