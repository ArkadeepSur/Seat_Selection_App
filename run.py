from app import create_app, socketio

app = create_app()

print("APP URL MAP: ")
print(app.url_map)  # This prints all available routes

if __name__ == "__main__":
    socketio.run(app, debug=True)