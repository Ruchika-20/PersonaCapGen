from app import app,host,port

if __name__ == "__main__":
    app.run(host=host, port=port,debug=True)