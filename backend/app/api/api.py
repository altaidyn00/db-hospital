from fastapi import APIRouter
from app.api.v1 import country, doctor, disease_type, disease, user, discover, public_servant, record, specialize

router = APIRouter()

router.include_router(country.router, prefix="/v1", tags=["countries"])
router.include_router(doctor.router, prefix="/v1", tags=["doctors"])
router.include_router(disease_type.router, prefix="/v1", tags=["disease_types"])
router.include_router(disease.router, prefix="/v1", tags=["diseases"])
router.include_router(user.router, prefix="/v1", tags=["users"])
router.include_router(discover.router, prefix="/v1", tags=["discovers"])
router.include_router(public_servant.router, prefix="/v1", tags=["public_servants"])
router.include_router(record.router, prefix="/v1", tags=["records"])
router.include_router(specialize.router, prefix="/v1", tags=["specializes"])



