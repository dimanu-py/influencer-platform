from dataclasses import dataclass

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


@dataclass(frozen=True)
class VideoCreatedDomainEvent(DomainEvent):
    id: str
    title: str
    description: str