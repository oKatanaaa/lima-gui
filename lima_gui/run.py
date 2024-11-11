import uvicorn

def main():
    uvicorn.run("lima_gui.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()