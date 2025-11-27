from typing import TYPE_CHECKING
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from src.presentation.view_interfaz import ViewInterfaz
from src.domain.use_cases.dtos.user import UserData

if TYPE_CHECKING:
    from src.presentation.presenter import Presenter


class AddUserRequest(BaseModel):
    name: str
    email: str
    password: str
    street_address: str
    postal_code: str
    city: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    street_address: str
    postal_code: str
    city: str


class ApiView(ViewInterfaz):
    """API View that implements ViewInterfaz and provides HTTP endpoints."""

    def __init__(self):
        self.app = FastAPI(title="User Management API")
        self._messages: list[str] = []
        self._presenter: "Presenter" | None = None
        self._setup_routes()

    def _setup_routes(self):
        """Setup HTTP routes for the API."""

        @self.app.post("/users", response_model=UserResponse)
        async def add_user(request: AddUserRequest):
            """Add a new user via API."""
            if not self._presenter:
                raise HTTPException(status_code=500, detail="Presenter not initialized")

            user_data = UserData(
                name=request.name,
                email=request.email,
                password=request.password,
                street_address=request.street_address,
                postal_code=request.postal_code,
                city=request.city,
            )

            result = self._presenter.add_user(user_data)

            if not result["success"]:
                raise HTTPException(
                    status_code=400, detail=result["error"] or "Failed to add user"
                )

            user = result["user"]
            if not user:
                raise HTTPException(status_code=500, detail="User creation failed")

            return UserResponse(
                id=user.id,
                name=user.name,
                email=str(user.email),
                street_address=str(user.address.street_address),
                postal_code=str(user.address.postal_code),
                city=str(user.address.city),
            )

        @self.app.get("/users", response_model=list[UserResponse])
        async def list_users():
            """List all users via API."""
            if not self._presenter:
                raise HTTPException(status_code=500, detail="Presenter not initialized")

            result = self._presenter.list_users()

            if result["error"]:
                raise HTTPException(status_code=500, detail=result["error"])

            return [
                UserResponse(
                    id=user.id,
                    name=user.name,
                    email=str(user.email),
                    street_address=str(user.address.street_address),
                    postal_code=str(user.address.postal_code),
                    city=str(user.address.city),
                )
                for user in result["users"]
            ]

        @self.app.get("/health")
        async def health():
            """Health check endpoint."""
            return {"status": "ok"}

    def show(self, message: str) -> None:
        """Store messages (used by presenter for logging/debugging)."""
        self._messages.append(message)

    def get_input(self, prompt: str) -> str:
        """Not used in API context - data comes from HTTP requests."""
        # This method is required by the interface but not used in API context
        # In API, data comes from request body/parameters
        return ""

    def run(self, presenter: "Presenter") -> None:
        """Start the API server."""
        self._presenter = presenter

        uvicorn.run(self.app, host="0.0.0.0", port=8000)
