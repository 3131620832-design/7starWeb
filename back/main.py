'''
Author: shiyugui 1960272852@qq.com
Date: 2025-10-30 14:38:35
LastEditors: shiyugui 1960272852@qq.com
LastEditTime: 2025-10-30 14:52:56
FilePath: \\7stars\\7starWeb\\back\\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="7starWeb")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        workers=4
    )
