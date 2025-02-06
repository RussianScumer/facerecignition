from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/recognition")
async def recognition():
    try: 
        await recognition()
    except Exception as e:
        return {
            "response": "fail",
            "error": str(e)
        }
    return "success"