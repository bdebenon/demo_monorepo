import json

import pytest
import pytest_asyncio
from dependency_injector.providers import Singleton
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport

from services.example_fast_api.src.domain.patients.definitions.fakers import PatientProvider
from services.example_fast_api.src.domain.patients.definitions.models import Patient
from services.example_fast_api.src.infra.patients.in_memory_patients_repository import InMemoryPatientsRepository
from services.example_fast_api.src.service.app import setup_app


@pytest.fixture
def app():
    app_instance = FastAPI()
    setup_app(app=app_instance)
    app_instance.container.patients_repository.override(Singleton(InMemoryPatientsRepository))
    return app_instance


@pytest_asyncio.fixture
async def client(app: FastAPI):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


class TestPatientsRouter:
    patients = [
        PatientProvider.patient(age=60, name="John Wick"),
        PatientProvider.patient(age=45, name="Harry Potter"),
    ]

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_patients_get_one_result(self, app, client):
        # Arrange
        app.container.patients_repository(data=self.patients)

        # Act
        response = await client.get("/patients", params={"max_age": 45})

        # Assert
        assert response.status_code == 200
        results = json.loads(response.content)
        received_patients = [Patient(**result) for result in results]
        assert len(received_patients) == 1

    @pytest.mark.asyncio
    @pytest.mark.unit
    async def test_patients_get_all_results(self, app, client):
        # Arrange
        app.container.patients_repository(data=self.patients)

        # Act
        response = await client.get("/patients", params={"max_age": 100})

        # Assert
        assert response.status_code == 200
        results = json.loads(response.content)
        received_patients = [Patient(**result) for result in results]
        assert len(received_patients) == len(self.patients)
