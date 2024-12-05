import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.content_creation.videos.application.video_creator import VideoCreator
from src.contexts.content_creation.videos.domain.video import Video
from src.contexts.content_creation.videos.domain.video_repository import VideoRepository


@pytest.mark.unit
class VideoModuleUnitTestConfig:
    def setup_method(self) -> None:
        self.repository = Spy(VideoRepository)
        self.video_creator = VideoCreator(self.repository)

    def should_have_saved(self, video: Video):
        expect(self.repository.save).to(have_been_called_with(video))