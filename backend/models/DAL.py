from backend.schemas.users import UserCreate
from backend.models.users import User

from backend.schemas.videos import VideoUpload, VideoPreview
from backend.models.videos import Video

from backend.models.likes import Like

from backend.models.comments import Comment
from backend.schemas.comments import CommentView

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import Union


class UserDal:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def create_user(self, body: UserCreate):
        new_user = User(email=body.email, username=body.username, hashed_password=body.hashed_password)
        self.session.add(new_user)
        await self.session.flush()
        return new_user

    async def get_user_by_email(self, email: str) -> Union[User, None]:
        res = await self.session.execute(select(User).where(User.email == email))
        user = res.fetchone()
        if user is None:
            return None
        return user[0]

    async def get_user_by_id(self, user_id: str) -> Union[User, None]:
        res = await self.session.execute(select(User).where(User.id == user_id))
        user = res.fetchone()
        if user is None:
            return None
        return user[0]


class VideoDal:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def add_video(self, body: VideoUpload):
        new_video = Video(title=body.title, description=body.description, link=body.filename, user_id=body.user_id)
        self.session.add(new_video)
        await self.session.flush()
        return new_video

    async def get_video_by_id(self, video_id: int) -> Union[Video, None]:
        res = await self.session.execute(select(Video).where(Video.id == video_id))
        video = res.fetchone()
        if video is None:
            return None
        return video[0]

    async def get_videos(self):
        res = await self.session.execute(select(Video))
        videos = res.fetchall()
        pre_videos = []
        for video in videos:
            pre_videos.append(VideoPreview.from_orm(video[0]))
        return pre_videos



class LikeDal:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def update_like(self, video_id: int, user_id: int):
        res = await self.session.execute(select(Like).where(Like.user_id == user_id).where(Like.video_id == video_id))
        like = res.fetchone()
        if like is None:
            self.session.add(Like(user_id=user_id, video_id=video_id))
            await self.session.flush()
            return {"status": "added"}
        else:
            await self.session.execute(delete(Like).where(Like.user_id == user_id).where(Like.video_id == video_id))
            await self.session.commit()
            return {"status": "deleted"}

    async def check_like(self, video_id: int, user_id: int):
        res = await self.session.execute(select(Like).where(Like.user_id == user_id).where(Like.video_id == video_id))
        like = res.fetchone()
        if like is None:
            return False

        return True


class CommentDal:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def add_comment(self, text: str, video_id: int, user_id: int):
        com = Comment(text=text, user_id=user_id, video_id=video_id)
        self.session.add(com)
        await self.session.flush()

    async def get_comments(self, video_id: int):
        res = await self.session.execute(select(Comment).where(Comment.video_id == video_id))
        comms = res.fetchall()
        pre_comms = []
        for com in comms:
            pre_comms.append(CommentView.from_orm(com[0]))
        return pre_comms
