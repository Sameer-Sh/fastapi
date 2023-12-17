# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
 
# from app.core import config
# from app.core.database import init_pg_db
# from app.services.battleship.battleship_router import router as battleship_router

 
# app = FastAPI(**config.APP_CONFIGS)
 
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.on_event("startup")
# async def startup_event():
#     print("View The Docs On : http://127.0.0.1:8000/docs")

# @app.get('/')
# async def health_check():
#     return {
#         'message' : 'Welcome To Python Project'
#     }  

# @app.get('/heath-check')
# async def health_check():
#     return {
#         'status' : 'ok'
#     }


# app.include_router(battleship_router)



from app.services.market_place.interactions.BuyerServices import BuyerServices
from app.services.market_place.interactions.CartServices import CartServices
from app.services.market_place.interactions.ProductServices import ProductServices
from app.services.market_place.CommandInterpreter import CommandInterpreter
from app.services.market_place.models.MarketPlace import MarketPlace


def main():
    buyer_service = BuyerServices()
    product_service = ProductServices()
    cart_service = CartServices()
    market_place = MarketPlace(buyer_service, product_service, cart_service)

    print("Enter commands. Type 'exit' to quit.")
    
    while True:
        command = input()

        if command == "exit":
            break

        CommandInterpreter.interpret_command(market_place, command)

if __name__ == "__main__":
    main()
