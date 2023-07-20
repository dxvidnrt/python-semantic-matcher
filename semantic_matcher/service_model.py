from typing import Optional, List

from pydantic import BaseModel

import matcher


class MatchRequest(BaseModel):
    """
    Request body for the :func:`service.SemanticMatchingService.get_match`

    :ivar semantic_id: The semantic ID that we want to find matches for
    :ivar local_only: If `True`, only check at the local service and do not request other services
    :ivar name: Optional name of the resolved semantic ID for NLP matching
    :ivar definition: Optional definition of the resolved semantic ID for NLP matching
    """
    semantic_id: str
    local_only: bool = True
    name: Optional[str] = None
    definition: Optional[str] = None


class MatchResponse(BaseModel):
    matches: List[matcher.SemanticMatch]