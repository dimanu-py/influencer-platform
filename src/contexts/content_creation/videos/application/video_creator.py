from src.contexts.content_creation.videos.application.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.content_creation.videos.domain.video import Video
from src.contexts.content_creation.videos.domain.video_repository import VideoRepository


class VideoCreator:
    repository: VideoRepository

    def __init__(self, repository: VideoRepository) -> None:
        self.repository = repository

    def __call__(self, command: CreateVideoCommand) -> None:
        video = Video.create(command.id, command.title, command.description)
        self.repository.save(video)
