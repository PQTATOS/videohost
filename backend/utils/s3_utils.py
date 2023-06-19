import aioboto3
from fastapi import UploadFile
from backend.settings import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, BUCKET_NAME


s3_session = aioboto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


async def upload_file(file: UploadFile, filename: str) -> bool:
    upload_info = False
    async with s3_session.client('s3', endpoint_url="https://storage.yandexcloud.net") as s3:
        try:
            await s3.upload_fileobj(file, BUCKET_NAME, filename)
            upload_info = True
        except Exception:
            pass
        return upload_info



