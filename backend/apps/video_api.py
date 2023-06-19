from fastapi import APIRouter, Depends, UploadFile, Form, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from backend.utils.utils import get_current_user
from backend.database import get_session
from backend.models.users import User
from backend.utils.s3_utils import upload_file
from backend.settings import BUCKET_NAME
from backend.models.DAL import VideoDal, UserDal, LikeDal, CommentDal
from backend.schemas.videos import VideoUpload, VideoRead

video_router = APIRouter(tags=["video"], prefix="/video")


@video_router.post("/upload")
async def upload_video(user_id: User = Depends(get_current_user), file: UploadFile = File(...),
                       title: str = Form(...),
                       description: str = Form(...),
                       session: AsyncSession = Depends(get_session)):
    async with session.begin():
        user_dal = UserDal(session)
        cur_user = await user_dal.get_user_by_id(user_id)
        if cur_user is None:
            raise HTTPException(status_code=400, detail="User account not found!")
        if title == "" or title.isspace():
            raise HTTPException(status_code=400, detail='No title')

        filename = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
        result = await upload_file(file, filename)

        if not result:
            raise HTTPException(status_code=400, detail='Upload error')

        video = VideoUpload(title=title, description=description, user_id=cur_user.id, filename=filename)
        video_dal = VideoDal(session)
        await video_dal.add_video(video)
        return {"Hello": "world"}


@video_router.get("/watch")
async def get_video(video_id: int,  session: AsyncSession = Depends(get_session)):
    async with session.begin():
        video_dal = VideoDal(session)
        video = await video_dal.get_video_by_id(video_id)

        if video is None:
            raise HTTPException(status_code=404, detail="Video not found!")

        return VideoRead(title=video.title, description=video.description,
                         link=f"https://storage.yandexcloud.net/{BUCKET_NAME}/{video.link}",
                         user_id=video.user_id,
                         created_at=video.published_at,
                         like_count=video.like_count)


@video_router.get("/")
async def get_videos(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        video_dal = VideoDal(session)
        videos = await video_dal.get_videos()

        return videos


@video_router.get("/comments")
async def get_comments(video_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        comm_dal = CommentDal(session)
        comms = await comm_dal.get_comments(video_id)
        return comms


@video_router.post("/like")
async def get_like(video_id: int, user_id: User = Depends(get_current_user),
                   session: AsyncSession = Depends(get_session)):
    async with session.begin():
        video_dal = VideoDal(session)
        video = await video_dal.get_video_by_id(video_id)
        if video is None:
            raise HTTPException(status_code=404, detail="Video not found!")

        user_dal = UserDal(session)
        cur_user = await user_dal.get_user_by_id(user_id)
        if cur_user is None:
            raise HTTPException(status_code=400, detail="User account not found!")

        like_dal = LikeDal(session)
        return await like_dal.update_like(video_id, user_id)


@video_router.get("/like")
async def check_is_like(video_id: int, user_id: User = Depends(get_current_user),
                   session: AsyncSession = Depends(get_session)):
    async with session.begin():
        video_dal = VideoDal(session)
        video = await video_dal.get_video_by_id(video_id)
        if video is None:
            raise HTTPException(status_code=404, detail="Video not found!")

        user_dal = UserDal(session)
        cur_user = await user_dal.get_user_by_id(user_id)
        if cur_user is None:
            raise HTTPException(status_code=400, detail="User account not found!")

        like_dal = LikeDal(session)
        return {"isLiked": await like_dal.check_like(video_id, user_id)}


@video_router.post("/comment")
async def add_comment(video_id: int, content: str = Form(...),
                      user_id: User = Depends(get_current_user),
                      session: AsyncSession = Depends(get_session)):
    async with session.begin():
        video_dal = VideoDal(session)
        video = await video_dal.get_video_by_id(video_id)
        if video is None:
            raise HTTPException(status_code=404, detail="Video not found!")

        user_dal = UserDal(session)
        cur_user = await user_dal.get_user_by_id(user_id)
        if cur_user is None:
            raise HTTPException(status_code=400, detail="User account not found!")

        com_dal = CommentDal(session)
        await com_dal.add_comment(content, video_id, user_id)



