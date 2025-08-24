import argparse

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.example_fast_api.src.common.config import config
from services.example_fast_api.src.service.dependency_injection.container import Container
from services.example_fast_api.src.service.patients import patients_router


def setup_app(app: FastAPI):
    app.container = Container()
    app.container.wire(
        modules=[
            # token,
            patients_router,
        ])

    app.include_router(patients_router.router)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers=["Content-Disposition"],  # Expose the Content-Disposition header to the client
    )


example_fast_api_app = FastAPI()
setup_app(app=example_fast_api_app)


@example_fast_api_app.get('/')
@example_fast_api_app.get('/health_check')
async def health_check():
    return {'message': 'success'}


@example_fast_api_app.get('/environment')
async def environment():
    return {'message': config.environment}


if __name__ == '__main__':
    # Pull in any args
    parser = argparse.ArgumentParser(description='Process the command line arguments.')
    parser.add_argument('--num_workers', type=int, help='Number of workers')
    parser.add_argument('--host_address', type=str, help='Host address')
    parser.add_argument('--port', type=int, help='Port number')
    parser.add_argument('--ssl_keyfile', type=str, help='Path to SSL key file')
    parser.add_argument('--ssl_certfile', type=str, help='Path to SSL certificate file')
    args = parser.parse_args()
    num_workers = 4 if args.num_workers is None else args.num_workers
    host_address = '0.0.0.0' if args.host_address is None else args.host_address
    port = 8002 if args.port is None else args.port
    ssl_keyfile = args.ssl_keyfile
    ssl_certfile = args.ssl_certfile

    print(f'Running app with environment set to: {config.environment}')

    uvicorn.run(
        app='services.example_fast_api.src.service.app:example_fast_api_app',
        host=host_address,
        port=port,
        workers=num_workers,
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
    )
