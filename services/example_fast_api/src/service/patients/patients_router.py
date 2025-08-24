from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from services.example_fast_api.src.domain.patients.definitions.models import Patient
from services.example_fast_api.src.service.dependency_injection.container import Container
from services.example_fast_api.src.service.patients.use_cases.get_patients_use_case import GetPatientsUseCase

router = APIRouter()


@router.get('/patients', response_model=list[Patient])
@inject
async def patients_get(
        max_age: int,
        get_patients_use_case: GetPatientsUseCase = Depends(
            Provide[Container.get_patients_use_case]),
) -> list[Patient]:
    return get_patients_use_case.execute(max_age=max_age)
